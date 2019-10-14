'''
Created on 2019年10月14日

@author: root
'''

from genieLibrary import genieStubs

if __name__ == '__main__':
    
    resultinfo, deviceDict = genieStubs.getAllDeviceList()
    
#    print(resultinfo)
    print('MAC Address\t\tDevice ID')
    print('=================================================================')
    for items in deviceDict :
        print(items, '\t', deviceDict[items], sep='')

    print('=================================================================')
    print('Totally', len(deviceDict), 'possible MAC Addresses are available for query.')
    pass