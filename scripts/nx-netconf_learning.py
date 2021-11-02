#! /usr/bin/env python

from ncclient import manager

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

conn = manager.connect(
    host="172.16.1.90",
    port=22,
    username="cisco",
    password="cisco",
    hostkey_verify=False,  # Bypasses the known_hosts requirement
    device_params={"name": "nexus"},  # Specifies the type of device
    look_for_keys=False  # Disables the private-public key auth
)

# Print all the Nexus capabilities
for val in conn.server_capabilities:
    print(val)

# Close the NETCONF connection
conn.close_session()