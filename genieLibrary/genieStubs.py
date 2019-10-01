# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import os
import requests
import dpath.util
from genieLibrary import commonVariables

def getAllDeviceList(genieSERVERIP=commonVariables.DEFAULT_SERVERIP, geniePort=commonVariables.DEFAULT_PORT, genieTimeout=commonVariables.DEFAULT_CONNECTION_TIMEOUT):
    '''
    getAllDeviceList: Given URL and Port of genieACS, retrieving the list of all devices. To avoid endless trial, a timeout (in seconds) can be set for HTTP connection.
    '''
    deviceList = []
    devicegetURL = 'http://' + genieSERVERIP + ':' + geniePort + '/devices/'

    resultinfo = commonVariables.DEFAULT_MESSAGE_OK

    try :    
        rawData = requests.get(devicegetURL, timeout=genieTimeout)
        
        if rawData.status_code != 200 :
            resultinfo = str(rawData.status_code)
            deviceList = []
        else :
            rawDevices = rawData.json()
    
            for items in rawDevices :
#                print(items['_id'])
                deviceList.append(items['_id'])

    except BaseException as e :
        deviceList = []
        resultinfo = str(e)
    else :
        pass
    finally:
        pass

    return resultinfo, deviceList

def getAllElementsListFromFile(genieFrom=commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX):
    '''
    getAllElementsList: Retrieve the customized data elements as a list from specified file. 
    '''
    elementList = []
    elementDetailed = []
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    
    if not os.path.isfile(genieFrom) :
        resultinfo = commonVariables.DEFAULT_MESSAGE_FILE_NOT_FOUND
    else :
        with open(genieFrom, 'r') as f:
            curr_str = f.readline()
            while curr_str :
                curr_detailed = curr_str[:-1].split(commonVariables.DEFAULT_DELIMINATOR)
                elementList.append(curr_detailed[0])
                elementDetailed.append(curr_detailed)
                curr_str = f.readline()

    return resultinfo, elementList, elementDetailed

def getParameterValues(deviceList, valueList, genieSERVERIP=commonVariables.DEFAULT_SERVERIP, geniePort=commonVariables.DEFAULT_PORT, genieTimeout=commonVariables.DEFAULT_CONNECTION_TIMEOUT, genieConnectionRequest=True):
    '''
    getAllElementsList: do GetParameterValues from deviceList.
    '''
    parmValueList = {}
    
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    if type(deviceList) is not list or type(valueList) is not list :
        resultinfo = commonVariables.DEFAULT_MESSAGE_TYPE_MISMATCH
    elif len(deviceList) == 0 or len(valueList) == 0:
        resultinfo = commonVariables.DEFAULT_MESSAGE_EMPTY_CONTAINER
    else :
        valueList_str = '{ \"name\": \"getParameterValues\", \"parameterNames\" : ' + repr(valueList).replace('\'', '\"') + '}'
        
        for items in deviceList :
            valuegetURL = 'http://' + genieSERVERIP + ':' + geniePort + '/devices/' + items + '/tasks'
            
            if genieConnectionRequest :
                valuegetURL += '?connection_request'
            
#            print('valuegetURL = ', valuegetURL)
#            print('items =', items)
#            print('valueList =', valueList)
#            print('valueList_STR =', valueList_str)

            try :            
                rawData = requests.post(valuegetURL, data=valueList_str, timeout=genieTimeout)
#                print(rawData.text)
                if rawData.status_code != 200 :
                    resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
                parmValueList.update({items : rawData.status_code})
#                print('curr parmValueList = ', parmValueList)
            except BaseException as e :
                parmValueList.update({items : str(e)})
                resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
            else :
                pass
            finally:
                pass            

    return resultinfo, parmValueList

def queryParameterValues(deviceList, valueList, genieSERVERIP=commonVariables.DEFAULT_SERVERIP, geniePort=commonVariables.DEFAULT_PORT, genieTimeout=commonVariables.DEFAULT_CONNECTION_TIMEOUT):
    '''
    queryParameterValues: query database for current value of data model elements.
    '''
    parmValueList = []
    
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    if type(deviceList) is not list or type(valueList) is not list :
        resultinfo = commonVariables.DEFAULT_MESSAGE_TYPE_MISMATCH
    elif len(deviceList) == 0 or len(valueList) == 0:
        resultinfo = commonVariables.DEFAULT_MESSAGE_EMPTY_CONTAINER
    else :    
        projectionStr = ''
        for elements in valueList :
            projectionStr += elements
            projectionStr += ','
        
        projectionStr = projectionStr[:-1]
    
        for items in deviceList :
            current_result_list = []
            current_result_list.append(items)
            current_returned_pairs = {}
            valuegetURL = 'http://' + genieSERVERIP + ':' + geniePort + '/devices?query=%7B%22_id%22%3A%22' + items + '%22%7D&projection=' + projectionStr
#            print('projectionStr =', projectionStr)
            
            try :            
                rawData = requests.get(valuegetURL, timeout=genieTimeout)
#                print(rawData.text)
                if rawData.status_code != 200 :
                    resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
                current_result_list.append(rawData.status_code)
#                current_result_list.append(rawData.json())
#                parmValueList.update({items : rawData.status_code})
#                print('curr parmValueList = ', parmValueList)
#                print('****************', rawData.json()[0]['Device']['DeviceInfo']['AdditionalHardwareVersion']['_value'])

#                print('valueList -->>', valueList)
                for eles in valueList :
#                    print('---->>', eles)
                    path_pattern = eles.replace('.', '/') + '/_value'
#                    print('---->>', eles, 'to', path_pattern)
                    try :
                        current_returned_pairs.update({eles : dpath.util.get(rawData.json()[0], path_pattern)})
                    except KeyError as e :
                        current_returned_pairs.update({eles : None})
                    else :
                        pass
                    finally :
                        pass
                current_result_list.append(current_returned_pairs)
            except BaseException as e :
                current_result_list[1] = -1
                current_result_list.append(str(e))
                resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
            else :
                pass
            finally:
                parmValueList.append(current_result_list)

    return resultinfo, parmValueList

def setParameterValues(deviceList, whole_value_list, genieSERVERIP=commonVariables.DEFAULT_SERVERIP, geniePort=commonVariables.DEFAULT_PORT, genieTimeout=commonVariables.DEFAULT_CONNECTION_TIMEOUT, genieConnectionRequest=True):
    '''
    getAllElementsList: do setParameterValues from deviceList.
    '''
    parmValueList = {}
    changedElements = []
    
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    if type(deviceList) is not list or type(whole_value_list) is not list :
        resultinfo = commonVariables.DEFAULT_MESSAGE_TYPE_MISMATCH
    elif len(deviceList) == 0 or len(whole_value_list) == 0:
        resultinfo = commonVariables.DEFAULT_MESSAGE_EMPTY_CONTAINER
    else :
        
        setString = ''
        
        for keypairs in whole_value_list :

            curr_setting = '['
            
            if type(keypairs) is not list :
                continue
            elif len(keypairs) < 2 :
                continue
            else :
                curr_setting += '\"'
                curr_setting += keypairs[0]
                changedElements.append(keypairs[0])
                curr_setting += '\",\"'
                curr_setting += str(keypairs[1])
                curr_setting += '\"],'
        
                setString += curr_setting
        
        
        if len(setString) < 2 :
            resultinfo = commonVariables.DEFAULT_MESSAGE_EMPTY_CONTAINER
        else :
            setString = setString[:-1]

            for items in deviceList :
                setURL = 'http://' + genieSERVERIP + ':' + geniePort + '/devices/' + items + '/tasks'
            
                if genieConnectionRequest :
                    setURL += '?connection_request'
            
                setData = '{ \"name\": \"setParameterValues\", \"parameterValues\": [' + setString + '] }'
            
#                print('setURL =', setURL)
#                print('setData =', setData)
                
                try :
                    rawData = requests.post(setURL, setData, timeout=genieTimeout)
                    if rawData.status_code != 200 :
                        resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
                    parmValueList.update({ items : rawData.status_code })
                except BaseException as e :
                    parmValueList.update({ items : str(e) })
                    resultinfo = commonVariables.DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE
                else :
                    pass
                finally:
                    pass

#    print('changedElements =', changedElements)                
    return resultinfo, parmValueList, changedElements
