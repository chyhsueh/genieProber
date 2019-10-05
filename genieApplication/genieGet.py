# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''
import sys
import os
import time

from genieLibrary import genieStubs, commonVariables, fileStubs, parserStubs

if __name__ == '__main__':
    
#    print('Length of sys.argv =', len(sys.argv))
    
    deviceList = []
    
    if len(sys.argv) == 1 :
        results_01, deviceList = genieStubs.getAllDeviceList()
        print(results_01)
        print(deviceList)
    else :        
        if sys.argv[1] == '--help' :
            print('Usage:\tpython3.7 -m genieApplication.genieGet [--help|deviceIDList(using \",\" for separate)]', file=sys.stderr)
            print('**** Prerequest: Please install the requests and dpath package from pip:', file=sys.stderr)
            print('\t# pip3 install --upgrade pip requests dpath', file=sys.stderr)
            if sys.platform != 'win32' :
                print('**** ConfigFile: by default, the data elements for value get will be defined in', commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX, file=sys.stderr)
            else :
                print('**** ConfigFile: by default, the data elements for value get will be defined in', commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_WINDOWS, file=sys.stderr)
            print('**** TODO: Supporting for remote genieACS. Currently only the localhost is supported.', file=sys.stderr)
            sys.exit(1)
        else :
            deviceList = sys.argv[1].split(',')
            if '' in deviceList :
                deviceList.remove('')
#    print(deviceList)
    
    if sys.platform != 'win32' :
        results_02, elementList, elementDetailed = genieStubs.getAllElementsListFromFile()
    else :
        results_02, elementList, elementDetailed = genieStubs.getAllElementsListFromFile(genieFrom=commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_WINDOWS)
#    print(results_02)
    print(elementList)
    print(elementDetailed)

#    elementList_str = repr(elementList).replace('\'', '\"')

#    print('elementList_str =', elementList_str)

    results_03, valueResult = genieStubs.getParameterValues(deviceList=deviceList, valueList=elementList)
#    print(results_03)
#    print(valueResult)
    
    results_04, valueReturned = genieStubs.queryParameterValues(deviceList=deviceList, valueList=elementList)
    print('The returning of genieStubs.queryParameterValues =', results_04)
#    print('The query results from database (for verification) =', valueReturned)

    for items in valueReturned :
        if items[1] == 200 :
#
            blankDict = {}        
            for curr_items in items[2] :
                r, p, t = parserStubs.queryMetadataList(curr_items, elementDetailed)
                if r != commonVariables.DEFAULT_MESSAGE_OK :
                    continue

                if p == commonVariables.PERMISSION_READWRITE :
                    if 'int' in t or 'Int' in t or 'boolean' in t : 
                        blankDict.update({ curr_items : items[2][curr_items]})
                    else :
                        blankDict.update({ curr_items : ''})
#
            if sys.platform != 'win32' :
                rootDir = commonVariables.DEFAULT_DATA_ELEMENT_REPORT_PATH_POSIX
            else :
                rootDir = commonVariables.DEFAULT_DATA_ELEMENT_REPORT_PATH_WINDOWS
            
            if rootDir[-1] != os.sep :
                rootDir += os.sep
            
            currfileName = rootDir + items[0] + '_' + str(int(time.time())) + '.csv'
            blankfileName = rootDir + items[0] + '_' + str(int(time.time())) + '.blankList.txt'
            fileStubs.exportCSVFromDictionary(items[2], currfileName)
            print('The device model of', items[0], 'had been exported to', currfileName)
            fileStubs.exportCSVFromDictionary(blankDict, blankfileName, delim='=')
            print('The device model (blank) of', items[0], 'had been exported to', blankfileName)
        else :
            print('The device model of', items[0], 'cannot be exported. Returned code =', items[1])
            pass

    sys.exit(0)
