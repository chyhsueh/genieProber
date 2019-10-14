# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import sys
import os
from genieLibrary import genieStubs

if __name__ == '__main__':
    
#    print(len(sys.argv))
#    print(sys.argv)
    
    if len(sys.argv) < 3 or not os.path.isfile(sys.argv[2]) :
        print('Usage:\tpython3.7 -m genieApplication.genieBatchSet [MACAddressList(using \",\" for separate)] [IMPORT_FILE]', file=sys.stderr)
        print('**** Prerequest: Please PREPARE the IMPORT_FILE for batch setting the data elements into specific CPEs.', file=sys.stderr)
        print('**** The format would be: \"DATA_ELEMENT=VALUE\" in each line of the file.', file=sys.stderr)
        sys.exit(1)
    else :

        deviceDict = {}
        deviceList = []

        results_00, deviceDict = genieStubs.getAllDeviceList()
        print(results_00)
        print(deviceDict)

        
        whole_value_list = []
        
#        deviceList = sys.argv[1].split(',')
#        if '' in deviceList :
#            deviceList.remove('')
#
        mac_List = sys.argv[1].split(',')
        if '' in mac_List :
            mac_List.remove('')
                
        for mac_items in mac_List :
            if mac_items in deviceDict :
                deviceList.append(deviceDict[mac_items])

        print('OK. I will do genieGet on the following devices:')
    
        for its in deviceList :
            print('\t', its)
#
        with open(sys.argv[2], 'r') as f :
            curr_str = f.readline()
            elementList = []

            while curr_str :
                elementList = curr_str[:-1].split('=')
                whole_value_list.append(elementList)
                curr_str = f.readline()
            
#        print(deviceList)
#        print(whole_value_list)
        
        ret_info, status_dict, elementList = genieStubs.setParameterValues(deviceList, whole_value_list)
        
#        print('The returning of genieStubs.setParameterValues = ', ret_info)
#        print('The status code of webAPI execution (genieStubs.setParameterValues) =', status_dict)
        
        print('The status code of webAPI execution (genieStubs.setParameterValues) =')
        
        for its in status_dict :
            res = 'SUCCESS'
            if status_dict[its] != 200 :
                res = 'FAILED'
            print('\t', its, ':', res)
        
#        print('The updated data model elements =', elementList)

        results_04, valueReturned = genieStubs.queryParameterValues(deviceList=deviceList, valueList=elementList)
#        print('The returning of genieStubs.queryParameterValues =', results_04)
#        print('The query results from database (for verification) =', valueReturned)
        print('The query results from database (for verification) =')
        
        for jts in valueReturned :
            print('\t', jts[0], ':')
            
            for kts in jts[2] :
                print('\t\t', kts, '\t', jts[2][kts])

        sys.exit(0)

