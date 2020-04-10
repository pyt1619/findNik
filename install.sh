#!/bin/bash
cd
apt install python3 python3-pip sherlock -y
git clone https://github.com/snooppr/snoop.git
cd snoop
pip3 install -r requirements.txt 

