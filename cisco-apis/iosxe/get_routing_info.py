import requests
import os

requests.packages.urllib3.disable_warnings()

try:
    DEVICE_USER = os.environ.get("IOSXE_USER")
    DEVICE_PASS = os.environ.get("IOSXE_PASS")
except KeyError:
    print("Required environment variables are not set.")

DEVICE_IP = "192.168.7.160"
BASE_URL = f"https://{DEVICE_IP}/restconf/data"

def get_static_routes():
    headers = {
        "Accept": "application/yang-data+json"
    }

    interfaces_url = f"{BASE_URL}/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1"
    response = requests.get(url=interfaces_url, headers=headers, auth=(DEVICE_USER, DEVICE_PASS), verify=False)

    print(response.status_code)
    print(response.text)
    print("All Static Routes:")
    for route in response.json()["ietf-routing:routing-protocol"]["static-routes"]["ietf-ipv4-unicast-routing:ipv4"] ["route"]:
        print(f"Prefix: {route.get('destination-prefix', '')}  Next-Hop: {route['next-hop'].get('next-hop-address', '')}")

if __name__ == "__main__":
    get_static_routes()