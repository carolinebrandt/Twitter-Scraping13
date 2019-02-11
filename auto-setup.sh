#!/bin/sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python
sudo apt-get install python-setuptools python-dev build-essential
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo pip install pip-requirements.txt
python get-pip.py
nohup python uppsala_aws.py &
