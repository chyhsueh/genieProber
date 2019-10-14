# -*- coding: utf-8 -*-
'''
@author: root@localhost
'''

DEFAULT_SERVERIP = '127.0.0.1'
DEFAULT_PORT = '7557'

DEFAULT_CONNECTION_TIMEOUT = 5000

DEFAULT_CONFIG_FILE_PATH_POSIX = '/home/genie_setting.conf'
DEFAULT_CONFIG_FILE_PATH_WINDOWS = 'D:\\genie_setting.conf'

DEFAULT_CPE_LIST_FILE_PATH_POSIX = '/home/cpe_element.txt'
DEFAULT_CPE_LIST_FILE_PATH_WINDOWS = 'D:\\cpe_element.txt'

DEFAULT_DATA_ELEMENT_FILE_PATH_POSIX = '/home/data_element.txt'
DEFAULT_DATA_ELEMENT_FILE_PATH_WINDOWS = 'D:\\data_element.txt'

DEFAULT_DATA_ELEMENT_REPORT_PATH_POSIX = '/home/'
DEFAULT_DATA_ELEMENT_REPORT_PATH_WINDOWS = 'D:\\'

#DEFAULT_DEVICELIST_FILE_PATH_POSIX = '/home/deviceslist.txt'
#DEFAULT_DEVICELIST_FILE_PATH_WINDOWS = 'D:\\deviceslist.txt'

DEFAULT_DELIMINATOR = '\t'

DEFAULT_MESSAGE_OK = 'OK'

DEFAULT_MESSAGE_EMPTY_CONTAINER = 'The input container is empty.'
DEFAULT_MESSAGE_FILE_NOT_FOUND = 'File not found.'
DEFAULT_MESSAGE_TYPE_MISMATCH = 'The data type is NOT matched to the original design.'

DEFAULT_MESSAGE_INFO_EXTRACTION_FAILED = 'Failed to extract any info from source.'

DEFAULT_MESSAGE_PLEASE_SEE_STATUS_CODE = 'Please verify the status code and identify what\'s happened.'

PERMISSION_READONLY = 'R'
PERMISSION_READWRITE = 'RW'

TAG_OUI = 'Device.DeviceInfo.ManufacturerOUI'
TAG_MODEL = 'Device.DeviceInfo.ModelName'
TAG_SN = 'Device.DeviceInfo.SerialNumber'
