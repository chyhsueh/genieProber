# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import sys
from genieLibrary import genieStubs

if __name__ == '__main__':
    
#    print(len(sys.argv))
    
    if len(sys.argv) <= 2 :
        print('Usage:\tpython3.7 -m genieApplication.genieSet [MACAddressList(using \",\" for separate)] [data_element=Value]xN ...', file=sys.stderr)
        print('**** Prerequest: Please install the requests and dpath package from pip:', file=sys.stderr)
        print('\t# pip3 install --upgrade pip requests dpath', file=sys.stderr)
        print('**** TODO: Supporting for remote genieACS. Currently only the localhost is supported.', file=sys.stderr)
        sys.exit(1)
    else :

        deviceDict = {}
        deviceList = []

        results_00, deviceDict = genieStubs.getAllDeviceList()
        print(results_00)
        print(deviceDict)
        
        whole_value_list = []
        
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
        
        for idx in range(2, len(sys.argv)) :
            curr_pair = sys.argv[idx].split('=')
            if len(curr_pair) != 2 or '' in curr_pair:
                print('Usage:\tpython3.7 -m genieApplication.genieSet [MACAddressList(using \",\" for separate)] [data_element=Value]xN ...', file=sys.stderr)
                sys.exit(2)
            else :
                whole_value_list.append(curr_pair)

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

