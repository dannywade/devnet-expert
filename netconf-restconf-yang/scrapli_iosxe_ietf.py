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
bgp_xpath = '/interfaces-state/interface[name="GigabitEthernet1"]'

conn = NetconfDriver(**iosxe_device)
conn.open()
# response = conn.get_config(source="running")
response = conn.get(filter_=bgp_xpath, filter_type="xpath")
conn.close()

print(response.result)

# Parsing XML XPath results to Python dict and parsing out uptime
dict_response = xmltodict.parse(response.result)

# Print dict as JSON string (for readability)
print(json.dumps(dict_response, indent=4))

print(f'Interface Name: {dict_response["rpc-reply"]["data"]["interfaces-state"]["interface"]["name"]}')

# Converts dict back to XML
# print(xmltodict.unparse(dict_response))
