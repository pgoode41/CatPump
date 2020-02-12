import os
import sys
import json
import requests
from pprint import pprint




projectDir = os.getenv('CATPUMPDIR')
HostConfigDir = projectDir+"HostConfig/"
inventoryFile = HostConfigDir+"/inventory"


def TestPlay():
    os.environ["ANSIBLE_HOST_KEY_CHECKING"] = "False"
    #ANSIBLE_HOST_KEY_CHECKING
    projectDir = os.getenv('CATPUMPDIR')

    playbook = projectDir+"HostConfig/Playbooks/test.yaml"

    ansible_command_string = "ansible-playbook -i "+inventoryFile+" "+playbook
    os.system(ansible_command_string)


