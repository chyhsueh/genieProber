'''
Created on 2019年9月23日

@author: root
'''

import sys
#import os
#from genieLibrary import commonVariables, fileStubs, parserStubs, genieStubs

if __name__ == '__main__':
    print('Currently no functions.', file=sys.stderr)
    '''
    print(len(sys.argv))
    print(sys.argv)

    if len(sys.argv) != 3 :
        print('Usage:\tpython3.7 -m genieApplication.genieSpoofGenerator [current_data_element_kayvaluepair_CSV] [FINAL_data_element_kayvaluepair_CSV (after spoofing)]', file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]) :
        print('Usage:\tpython3.7 -m genieApplication.genieSpoofGenerator [current_data_element_kayvaluepair_CSV] [FINAL_data_element_kayvaluepair_CSV (after spoofing)]', file=sys.stderr)
        sys.exit(2)

    dataElementOriginal = sys.argv[1]
    dataElementSpoofed = sys.argv[2]
    
    resultinfo, dataElement_index_list = fileStubs.importCSVToMultiDimensionalList(commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX, delim=',')
    
    if resultinfo != commonVariables.DEFAULT_MESSAGE_OK :
        print('Cannot find the element definition file ( default value =', commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX, '. Please have a check.', file=sys.stderr)
        sys.exit(3)
    
    print(dataElement_index_list)

    resultinfo, currentStatus = fileStubs.importCSVToMultiDimensionalList(dataElementOriginal)

#    print(currentStatus)

    deviceID = ''

    if resultinfo == commonVariables.DEFAULT_MESSAGE_OK :
        oui = ''
        model = ''
        sn = ''
        for items in currentStatus :
            if items[0] == commonVariables.TAG_OUI :
                oui = items[1]
            elif items[0] == commonVariables.TAG_MODEL :
                model = items[1]
            elif items[0] == commonVariables.TAG_SN :
                sn = items[1]
            else :
                pass
            
            if oui != '' and model != '' and sn != '' :
                break
        
        deviceID += oui
        deviceID += '-'
        deviceID += model
        deviceID += '-'
        deviceID += sn
        
        print('deviceID =', deviceID)
        
        for items in currentStatus :

            if items[0] == 'Device.ManagementServer.EnableCWMP' or 'ConnectionRequest' in items[0] :
                continue

            spoofedStatus = [] 
        
            result, permission, datatype = parserStubs.queryMetadataList(items[0], dataElement_index_list)
            if permission == commonVariables.PERMISSION_READWRITE :
                if items[1] == None or items[1] == 'None':
                    print('Skipped:', items)
                    pass
                else :
                    print('Doing:', items)
                    if datatype == 'str' :
#                        pass
                        newValue = items[1]
                    elif datatype == 'boolean' :
#                        pass
                        newValue = items[1]
                    elif datatype == 'dateTime' :
                        import time
                        newValue = time.asctime(time.localtime(time.time()))
                        del time
                    else :
                        if items[1] == 'Enabled' :
                            newValue = 0
                        elif items[1] == 'Disabled' :
                            newValue = 1
                        else :
                            newValue = int(items[1]) + 1
 
                    spoofme = [items[0], newValue]
                    spoofedStatus.append(spoofme)
                    
                    setresult, devstatus, changedElements = genieStubs.setParameterValues([deviceID], spoofedStatus)
        
                    print('setresult =', setresult)
                    print('devstatus =', devstatus)
                    print('changedElements', changedElements)
                    
                    if devstatus[deviceID] != 200 :
                        break
            else :
                pass
        
        print('spoofedStatus =', spoofedStatus)
    else :
        pass
    '''
    pass
