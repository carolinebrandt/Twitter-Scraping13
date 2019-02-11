#!/bin/sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python
sudo apt-get install python-setuptools python-dev build-essential
sudo -H chown -R ubuntu: /home/ubuntu/.cache
sudo apt install python-pip
sudo pip install -r pip-requirements.txt
nohup python uppsala_aws.py &
