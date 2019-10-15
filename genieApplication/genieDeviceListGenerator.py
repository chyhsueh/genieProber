'''
Created on 2019年10月14日

@author: root
'''

import sys

from genieLibrary import genieStubs, commonVariables, fileStubs
from genieTypes.genieServer import genieACSServer

if __name__ == '__main__':

    if sys.platform != 'win32' :
        results_00, serverInstance = fileStubs.configReader(commonVariables.DEFAULT_CONFIG_FILE_PATH_POSIX)
    else :
        results_00, serverInstance = fileStubs.configReader(commonVariables.DEFAULT_CONFIG_FILE_PATH_WINDOWS)

    resultinfo, deviceDict = genieStubs.getAllDeviceList(genieSERVERIP=serverInstance.serverIP, geniePort=str(serverInstance.serverPort), genieTimeout=serverInstance.serverTimeout)
    
#    print(resultinfo)
    print('MAC Address\t\tDevice ID')
    print('=================================================================')
    for items in deviceDict :
        print(items, '\t', deviceDict[items], sep='')

    print('=================================================================')
    print('Totally', len(deviceDict), 'possible MAC Addresses are available for query.')
    pass