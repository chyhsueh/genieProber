# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import re
from genieLibrary import commonVariables

def queryMetadataList(elementName, data_element_single_list):
    '''
    queryMetadataList: querying the definition from the metadata list. Returning datatype and RW-Permission
    '''
    resultinfo = commonVariables.DEFAULT_MESSAGE_INFO_EXTRACTION_FAILED
    
    for items in data_element_single_list :
        if elementName == items[0] :
            resultinfo = commonVariables.DEFAULT_MESSAGE_OK
            return resultinfo, items[1], items[2]

    return resultinfo, None, None

def extractingMetadata(srcString, patternString):
    '''
    extractingMetadata: Given single str and then try to extract the elements from the str.  
    '''
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    mytuple = ()
    p = re.compile(patternString)
    m = re.search(p, srcString)
    
    if m == None :
        resultinfo = commonVariables.DEFAULT_MESSAGE_INFO_EXTRACTION_FAILED
#        print('Failed', ':: ' + srcString.replace('\n', '') + ' :: ' + patternString.replace('\n', ''))
    else :
        mytuple = m.groups()
#        print('Successful', ':: ' + srcString.replace('\n', '') + ' :: ' + patternString.replace('\n', ''))
    
    return resultinfo, mytuple

def extractingDataElementMetadata(srcString):
    '''
    extractingDataElementMetadata: Applying the extractingMetadata and extracting data element metadata. Syntax = [ELEMENT, R/W/RW, DATATYPE]
    '''
    data_element_single_list = []

    myPattern = 'common_execute_method_param(.+)\"\$DMROOT.([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\"(.*)'
    mzPattern = 'common_execute_method_param(.+)\"\$DMROOT.([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\"(.*)'
    mwPattern = 'common_execute_method_param(.+)\"\$DMROOT.([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\"(.*)'
#    mxPattern = 'common_execute_method_param(.+)\"\$DMROOT.([^\"]*)\" \"([^\"]*)\"(.*)'
#    mvPattern = 'common_execute_method_param(.+)\"\$DMROOT.([^\"]*)\"(.*)'
    resultinfo, resultTuple = extractingMetadata(srcString, myPattern)
    
    if resultTuple == None or len(resultTuple) == 0:
        resultinfo, resultTuple = extractingMetadata(srcString, mzPattern)

    if resultTuple == None or len(resultTuple) == 0:
        resultinfo, resultTuple = extractingMetadata(srcString, mwPattern)
   
    if resultTuple != None and len(resultTuple) >= 4:
        elementStr = resultTuple[1].replace('$j', '1')
        elementStr = elementStr.replace('$k', '1')
        data_element_single_list.append('Device.' + elementStr)
        
        if len(resultTuple) == 4 :
            data_element_single_list.append(commonVariables.PERMISSION_READONLY)
        elif resultTuple[4] != '' :
            data_element_single_list.append(commonVariables.PERMISSION_READWRITE)
        else :
            data_element_single_list.append(commonVariables.PERMISSION_READONLY)
        
        if len(resultTuple) <= 5 :
            data_element_single_list.append('str')
        elif resultTuple[5] != '' and 'xsd:' in resultTuple[5]:
            data_element_single_list.append(resultTuple[5].replace('xsd:', ''))
        else :
            data_element_single_list.append('str')
    else :
        resultinfo = commonVariables.DEFAULT_MESSAGE_INFO_EXTRACTION_FAILED
        data_element_single_list.append(srcString)
        data_element_single_list.append(resultinfo)
    
    return resultinfo, data_element_single_list


