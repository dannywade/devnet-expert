from scrapli.driver.core import IOSXEDriver
from pprint import pprint
from config import inv

def get_ios_version(hostname: str) -> str:
    try:
        dev = inv.get(hostname)
    except:
        print("Device not found!")

    scrapli_dev = {
        "host": dev.get("host"),
        "auth_username": dev.get("user"),
        "auth_password": dev.get("pass"),
        "auth_secondary": dev.get("enable_pass"), # Enable password (if used)
        "auth_strict_key": False,
        "ssh_config_file": "config" # Need to include for older cipher suites (vIOS 15.x)
    }

    with IOSXEDriver(**scrapli_dev) as conn:
        result = conn.send_command("show version")

    parsed_output = result.genie_parse_output()

    return parsed_output["version"]["version"]

# USED FOR TESTING
if __name__ == "__main__":
    get_ios_version("R1")