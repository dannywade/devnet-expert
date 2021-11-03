from scrapli.driver.core import IOSXEDriver
from pprint import pprint

MY_DEVICE = {
    "host": "192.168.7.151",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_secondary": "cisco", # Enable password (if used)
    "auth_strict_key": False,
    "ssh_config_file": "config" # Need to include for older cipher suites (vIOS 15.x)
}

def main():
    """Simple example demonstrating getting structured data via textfsm/ntc-templates"""
    with IOSXEDriver(**MY_DEVICE) as conn:
        # Platform drivers will auto-magically handle disabling paging for you
        result = conn.send_command("show vlan")

    print(result.result)
    pprint(result.genie_parse_output())

    # 'show vlan' example
    # vlans = result.genie_parse_output()
    # pprint(vlans["vlans"]["10"]["interfaces"][0])

    # 'show version' example
    # device_version = result.genie_parse_output()
    # print(device_version["version"]["os"])

if __name__ == "__main__":
    main()
