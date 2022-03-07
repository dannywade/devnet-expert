import requests
import os
import yaml
import urllib.parse

requests.packages.urllib3.disable_warnings()

try:
    DEVICE_USER = os.environ.get("IOSXE_USER")
    DEVICE_PASS = os.environ.get("IOSXE_PASS")
except KeyError:
    print("Required environment variables are not set.")

DEVICE_IP = "192.168.7.160"
BASE_URL = f"https://{DEVICE_IP}/restconf/data"

def delete_static_routes():
    headers = {
        "Accept": "application/yang-data+json, application/yang-data.errors+json"
    }

    with open("config.yml", "r") as conf:
        config = yaml.safe_load(conf)

    static_route_url = f"{BASE_URL}/ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1/static-routes/ipv4"

    for route in config["route"]:
        prefix = route["destination-prefix"]
        enc_prefix = urllib.parse.quote(prefix, safe="")

        response = requests.delete(url=f"{static_route_url}/route={enc_prefix}", headers=headers, auth=(DEVICE_USER, DEVICE_PASS), verify=False)

        if response.status_code == 204:
            print(f"Prefix {prefix} has been removed.")
        elif response.status_code == 404:
            print(f"Prefix {prefix} was not found.")
        else:
            print(response.status_code)
            print(f"There was an error and prefix {prefix} was not removed.")

if __name__ == "__main__":
    delete_static_routes()