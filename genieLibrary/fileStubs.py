# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

import os
from genieLibrary import commonVariables

def findAllFilesFromDir(rootPath):
    '''
    findAllFilesFromDir: Given a rootPath, getting all the \"files\" within the rootPath recursively.
    '''

    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    fileList = []
    
    if not os.path.isdir(rootPath) :
        resultinfo = commonVariables.DEFAULT_MESSAGE_TYPE_MISMATCH
    else :
        for root, dirs, files in os.walk(rootPath):
            for f in files :
                fullpath = os.path.join(root, f)
                fileList.append(fullpath)
    
    return resultinfo, fileList

def exportCSVFromMultiDimensionalList(sourceList, exportPath, expectedColumSize=None):
    '''
    exportCSVFromMultiDimensionalList: Export the multidimensional List to exportPath. 
    '''
    totalString = ''

    if type(sourceList) is not list :
        return None

    for listitem in sourceList :
        if type(listitem) is not list :
            continue
        else :
            if type(expectedColumSize) is int and expectedColumSize > len(listitem) :
                continue
            else :
                curr_str = ''
                add_count = 0
                for items in listitem :
                    if type(expectedColumSize) is int and expectedColumSize < add_count :
                        break
                    else :
                        curr_str += items
                        curr_str += commonVariables.DEFAULT_DELIMINATOR
                        add_count += 1
                curr_str = curr_str[:-1] + '\n'
                totalString += curr_str

#    print('FinalString = ', totalString)
    with open(exportPath, 'w') as f :
        f.write(totalString)

    return None

def exportCSVFromDictionary(sourceDict, exportPath, delim=commonVariables.DEFAULT_DELIMINATOR):
    '''
    exportCSVFromDictionary: Export the dict structure to exportPath. 
    '''
    totalString = ''
    
    if type(sourceDict) is not dict :
        return None
    
    all_element = sourceDict.keys()
#    
    for listitem in all_element :
        curr_string = listitem + delim + str(sourceDict[listitem]) + '\n'
        totalString += curr_string

#    print('FinalString = ', totalString)
    with open(exportPath, 'w') as f :
        f.write(totalString)

    return None
    
def importCSVToMultiDimensionalList(importPath, delim=commonVariables.DEFAULT_DELIMINATOR):
    '''
    importCSVToMultiDimensionalList: Import the multidimensional List from CSV. 
    '''
    resultinfo = commonVariables.DEFAULT_MESSAGE_OK
    multiList = []
    
    if not os.path.isfile(importPath) :
        resultinfo = commonVariables.DEFAULT_MESSAGE_FILE_NOT_FOUND
        multiList = None
    else :
#
        with open(importPath, 'r') as f:
            curr_str = f.readline()
            elementList = []
            while curr_str :
                elementList = curr_str[:-1].split(delim)
                multiList.append(elementList)
                curr_str = f.readline()
#
    return resultinfo, multiList
