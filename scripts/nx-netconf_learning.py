#! /usr/bin/env python

from ncclient import manager
from config import inv
"""
NX-API is turned off by default on Cisco Nexus devices. Here
are steps to enable it via CLI:
feature nxapi

How to enable sandbox and HTTP in lab environment:
nxapi http port 80
nxapi sandbox

ncclient is a Python library for NETCONF clients.

Example from "Mastering Python Networking" by Eric Chou
"""

dev = inv.get("nexus")

conn = manager.connect(
    host=dev.get("host"),
    port=dev.get("port"),
    username=dev.get("user"),
    password=dev.get("pass"),
    hostkey_verify=False,  # Bypasses the known_hosts requirement
    device_params={"name": dev.get("type")},  # Specifies the type of device
    look_for_keys=False  # Disables the private-public key auth
)

# Print all the Nexus capabilities
for val in conn.server_capabilities:
    print(val)

# Close the NETCONF connection
conn.close_session()