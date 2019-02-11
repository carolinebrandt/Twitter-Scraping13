#!/bin/sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python
sudo apt-get install python-setuptools python-dev build-essential

sudo -H apt-get install python-pip
sudo pip install virtualenv 
virtualenv venv
source venv/bin/activate

pip install -r pip-requirements.txt
nohup python uppsala_aws.py &
