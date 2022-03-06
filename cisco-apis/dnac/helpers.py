"""
Module used to define helper function for other scripts
"""
import requests

def get_token(dnac_ip, user, pw):
    """
    Returns DNAC API token
    """
    token_url = f"{dnac_ip}/dna/system/api/v1/auth/token"
    headers = {
        "Accept": "application/json"
    }
    response = requests.post(url=token_url, auth=(user, pw), headers=headers)

    if response.status_code == 200:
        token = response.json()["Token"]
        print("Token successfully obtained!")
        return token
    else:
        print("Oops, something went wrong!")

# Example - Always-on DNAC sandbox
# get_token("sandboxdnac.cisco.com", "devnetuser", "Cisco123!")
