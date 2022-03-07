import requests
import os
import yaml

requests.packages.urllib3.disable_warnings()

try:
    DEVICE_USER = os.environ.get("IOSXE_USER")
    DEVICE_PASS = os.environ.get("IOSXE_PASS")
except KeyError:
    print("Required environment variables are not set.")

DEVICE_IP = "192.168.7.160"
BASE_URL = f"https://{DEVICE_IP}/restconf/data"

def add_static_routes():
    headers = {
        "Accept": "application/yang-data+json, application/yang-data.errors+json",
        "Content-Type": "application/yang-data+json"
    }

    with open("config.yml", "r") as conf:
        config = yaml.safe_load(conf)

    add_static_route_url = f"{BASE_URL}/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1/static-routes/ipv4"
    
    response = requests.post(url=add_static_route_url, headers=headers, auth=(DEVICE_USER, DEVICE_PASS), json=config, verify=False)

    if response.status_code == 201:
        print("Static routes have been added successfully!")
    elif response.status_code == 409:
        print("There was a conflict. Most likely the route already exists.")
    else:
        print("There was an error and the route was not added.")

if __name__ == "__main__":
    add_static_routes()