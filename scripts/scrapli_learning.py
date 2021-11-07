from scrapli.driver.core import IOSXEDriver
from pprint import pprint
from config import inv

dev = inv.get("192.168.7.151")


MY_DEVICE = {
    "host": dev.get("host"),
    "auth_username": dev.get("user"),
    "auth_password": dev.get("pass"),
    "auth_secondary": dev.get("enable_pass"), # Enable password (if used)
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
