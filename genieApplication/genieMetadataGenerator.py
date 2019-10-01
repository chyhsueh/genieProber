# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import sys
import os
from genieLibrary import fileStubs, parserStubs, commonVariables

if __name__ == '__main__':

    if len(sys.argv) < 2 or len(sys.argv) > 3 or not os.path.isdir(sys.argv[2]):
        print('Usage:\tpython3.7 -m genieApplication.genieMetadataGenerator [IMPORT_PATH (easycwmp function source code)] [EXPORTFILE (default =', commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX , ')]', file=sys.stderr)
        sys.exit(1)
    
    exportPath = commonVariables.DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX
    
    if len(sys.argv) == 3 :
        exportPath = sys.argv[2]

    testPath = sys.argv[1]
    datamodel_elements_list = []
    results, fileList = fileStubs.findAllFilesFromDir(testPath)
    
    if results == commonVariables.DEFAULT_MESSAGE_OK :
    
        for items in fileList :
            print('handling file: ', items)
            with open(items, 'r') as f :

                curr_str = f.readline()
                while curr_str :                    
                    if ' common_execute_method_param' in curr_str or '\tcommon_execute_method_param' in curr_str :
                        localresults, resultList = parserStubs.extractingDataElementMetadata(curr_str)
                        if resultList != None :
                            datamodel_elements_list.append(resultList)
                        else :
                            pass
                    else :
                        pass
                    curr_str = f.readline()
        print('total handled files: ', len(fileList))
        
        for items in datamodel_elements_list :
            print(items)
        print('total extracted elements: ', len(datamodel_elements_list))

        fileStubs.exportCSVFromMultiDimensionalList(datamodel_elements_list, exportPath, expectedColumSize=3)

        print('Exporting to CSV file DONE:', exportPath)
    else :
        pass
    pass

