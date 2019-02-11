#!/bin/sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python
sudo apt-get install python-setuptools python-dev build-essential
sudo apt install python-pip
#sudo -H pip install -r pip-requirements.txt
sudo -H pip install pip-requirements.txt
nohup python uppsala_aws.py &
