from pprint import pprint
from scrapli_netconf.driver import NetconfDriver
import os
import xmltodict
from pprint import pprint
import json


nx_device = {
    "host": "192.168.7.163",
    "auth_username": os.environ.get("CML_USER"),
    "auth_password": os.environ.get("CML_PASS"),
    "auth_strict_key": False,
    "port": 830
}

iosxe_device = {
    "host": "192.168.7.160",
    "auth_username": os.environ.get("CML_USER"),
    "auth_password": os.environ.get("CML_PASS"),
    "auth_strict_key": False,
    "port": 830
}

# Specific Xpath for BGP uptime
interface_xpath = '/interfaces/interface[name="GigabitEthernet1"]'

conn = NetconfDriver(**iosxe_device)
conn.open()
# response = conn.get_config(source="running")
response = conn.get(filter_=interface_xpath, filter_type="xpath")
conn.close()

print(response.result)

# Parsing XML XPath results to Python dict and parsing out uptime
dict_response = xmltodict.parse(response.result)

# Print dict as JSON string (for readability)
print(json.dumps(dict_response, indent=4))

# Interfaces container was provided as Python list with each model type being an item
# Index 0: Native model
# Index 1: IETF model
# Index 2: OpenConfig
oc_model = dict_response["rpc-reply"]["data"]["interfaces"][2]["interface"]
print(f'Interface Name: {oc_model["name"]}')
print(f'Interface Oper Status: {oc_model["state"]["oper-status"]}')

