import os
from aiohttp import BasicAuth
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import xmltodict


CML_USER = os.environ.get("CML_USER")
CML_PASS = os.environ.get("CML_PASS")

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

serial_response = requests.get(url="https://192.168.7.163/restconf/data/Cisco-NX-OS-device:System/serial", auth=HTTPBasicAuth(CML_USER, CML_PASS), headers=headers, verify=False)

print(serial_response.text)
pprint(xmltodict.parse(serial_response.text)["serial"])

ospf_response = requests.get(url='https://192.168.7.163/restconf/data/Cisco-NX-OS-device:System/ospf-items/inst-items/Inst-list=100/dom-items/Dom-list=default/if-items/If-list=eth1%2F2', auth=HTTPBasicAuth(CML_USER, CML_PASS), headers=headers, verify=False)

print(ospf_response.text)
dict_reply = xmltodict.parse(ospf_response.text)
pprint(dict_reply)