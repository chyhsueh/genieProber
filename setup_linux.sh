#!/bin/bash

echo -e "\n[INFO]\tChecking the version of python3:\n"

python3 -V

echo -e "\n[INFO]\tInstalling of python3-pip:\n"

if [ ! -f /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-*.list ]
then
	sudo add-apt-repository ppa:deadsnakes/ppa
fi

sudo apt-get update
sudo apt-get install -y python3.7 python3-pip
sudo python3.7 -m pip install --upgrade pip requests dpath

sudo cp -v ./conf/data_element.txt /home
sudo cp -v ./conf/setting.conf.txt /home

echo -e "\n\033[45m[INFO]\tInstallation Completed. I have a brief demo of how I can do:\033[m\n"

echo -e "\n\033[44m[INFO]\t========== genieApplication.genieMetadataGenerator Example ==========\033[m\n"

echo -e "\n[INFO]\t\033[33mpython3.7 -m genieApplication.genieMetadataGenerator /tmp/easycwmp_source/function /home/data_element.txt\033[m"

echo -e "\n\033[44m[INFO]\t========== genieApplication.genieSet Example ==========\033[m\n"

echo -e "\n[INFO]\t\033[33mpython3.7 -m genieApplication.genieSet 0078cd-myPortal-0078CD025CE8,0078cd-myPortal-0078CD025CE9 Device.ManagementServer.PeriodicInformInterval=170 Device.ManagementServer.CWMPRetryIntervalMultiplier=2800\033[m"

echo -e "\n\033[44m[INFO]\t========== genieApplication.genieBatchSet Example ==========\033[m\n"

echo -e "\n[INFO]\t\033[33mpython3.7 -m genieApplication.genieBatchSet 0078cd-myPortal-0078CD025CE8,0078cd-myPortal-0078CD025CE9 /homeDir/set_test.txt\033[m"

#python3.7 -m genieApplication.genieGet --help

echo -e "\n\033[44m[INFO]\t========== genieApplication.genieGet Example ==========\033[m\n"

echo -e "\n[INFO]\t\033[33mpython3.7 -m genieApplication.genieGet 0078cd-myPortal-0078CD025CE8,0078cd-myPortal-0078CD025CE9\033[m"
echo -e "\n[INFO]\tThe default data element config for genieGet can be found at \033[32m/home/data_element.txt\033[m\n"

#python3.7 -m genieApplication.genieSet

exit 0

