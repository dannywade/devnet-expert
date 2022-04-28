import os
from aiohttp import BasicAuth
import requests
from requests.auth import HTTPBasicAuth
# from requests.packages.urllib3
from pprint import pprint


CML_USER = os.environ.get("CML_USER")
CML_PASS = os.environ.get("CML_PASS")

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

response = requests.get(url="https://192.168.7.160/restconf/data/Cisco-IOS-XE-bgp-oper:bgp-state-data/address-families/address-family=ipv4-unicast,default", auth=HTTPBasicAuth(CML_USER, CML_PASS), headers=headers, verify=False)

print(response.text)