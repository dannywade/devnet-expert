import logging
import hvac
import os
from pprint import pprint
"""
Using boilerplate code to interact with a Vault (dev) server
"""
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.info("Setting up client...")
client = hvac.Client(url='http://localhost:8200', token=os.environ['VAULT_TOKEN'])

if client.is_authenticated():
    log.info("Client successfully authenticated with Vault")

### READING SECRETS ###
read_creds = client.secrets.kv.read_secret_version(path="iosxe", mount_point="netauto")
log.info("Successfully extracted secrets from Vault...")
SSH_USER = read_creds["data"]["data"]["ssh_user"]
SSH_PASS = read_creds["data"]["data"]["ssh_pass"]

### CREATING POLICIES ###
policies = client.sys.list_policies()["data"]["policies"]
log.info(f"Available policies: {*policies,}")
log.info("Adding new policy")

policy_name = "neteng_policy"
neteng_policy = """
path "netauto/*" {
    capabilities = ["create", "read", "update", "delete", "list", "patch"]
}
"""

client.sys.create_or_update_policy(name=policy_name, policy=neteng_policy)
log.info(f"New policy written: {policy_name}")