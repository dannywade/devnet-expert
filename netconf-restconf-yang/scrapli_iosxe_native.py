from pprint import pprint
from scrapli_netconf.driver import NetconfDriver
import os
import xmltodict
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
bgp_xpath = '/bgp-state-data/neighbors/neighbor[afi-safi="ipv4-unicast" and vrf-name="default" and neighbor-id="10.250.1.2"]/up-time'

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

print(f"BGP Uptime: {dict_response['rpc-reply']['data']['bgp-state-data']['neighbors']['neighbor']['up-time']}")

# Converts dict back to XML
# print(xmltodict.unparse(dict_response))
