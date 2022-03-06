"""
Script used to get all network devices in DNAC inventory
"""
import requests
import os
import sys
from helpers import get_token
from pprint import pprint

# Disable InsecureRequestWarning warning messages
requests.packages.urllib3.disable_warnings()

BASE_URL = "https://sandboxdnac.cisco.com"
try:
    DNAC_USER = os.environ.get("DNAC_USER")
    DNAC_PASS = os.environ.get("DNAC_PASS")
except KeyError:
    print("Missing required environment variables!")

# Acquire token for DNAC API use
TOKEN = get_token(BASE_URL, DNAC_USER, DNAC_PASS)

# Get list of network devices from DNAC
def get_dnac_network_devices(dnac_token: str) -> None:

    headers = {
        "X-Auth-Token": dnac_token,
        "Accept": "application/json"
    }

    net_device_resource = f"{BASE_URL}/dna/intent/api/v1/network-device"
    net_device_list = requests.get(url=net_device_resource, headers=headers, verify=False)

    if net_device_list.ok:
        pprint(net_device_list.json())
    else:
        print(f"Error code: {net_device_list.status_code}")
        print(f"Error response: {net_device_list.text}")

# Get list of network devices with the same IOS software version
def get_device_by_software(dnac_token: str, ios_version: str = None):

    headers = {
        "X-Auth-Token": dnac_token,
        "Accept": "application/json"
    }

    # Only send API request if IOS version is specified
    if ios_version:
        net_device_resource = f"{BASE_URL}/dna/intent/api/v1/network-device?softwareVersion={ios_version}"
        net_device_list = requests.get(url=net_device_resource, headers=headers, verify=False)
    else:
        sys.exit("Error: Please specify a software version.")

    # Print out response if response is ok (status code 200)
    if net_device_list.ok:
        pprint(net_device_list.json())
    else:
        print(f"Error code: {net_device_list.status_code}")
        print(f"Error response: {net_device_list.text}")

# Get uptime of network devices from DNAC using device's IP address
def get_uptime_by_ip(dnac_token: str, ip_address: str = None):

    headers = {
        "X-Auth-Token": dnac_token,
        "Accept": "application/json"
    }

    # Only send API request if IOS version is specified
    if ip_address:
        net_device_resource = f"{BASE_URL}/dna/intent/api/v1/network-device/ip-address/{ip_address}"
        net_device_list = requests.get(url=net_device_resource, headers=headers, verify=False)
    else:
        sys.exit("Error: Please specify a device IP address.")

    # Print out response if response is ok (status code 200)
    if net_device_list.ok:
        print(f"Current device uptime: {net_device_list.json()['response']['upTime']}")
    else:
        print(f"Error code: {net_device_list.status_code}")
        print(f"Error response: {net_device_list.text}")

if __name__ == "__main__":
    # get_dnac_network_devices(dnac_token=TOKEN)
    # get_device_by_software(dnac_token=TOKEN, ios_version="16.11.1c")
    get_uptime_by_ip(dnac_token=TOKEN, ip_address="10.10.20.80")