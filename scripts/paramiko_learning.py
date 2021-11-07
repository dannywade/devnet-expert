#! /usr/bin/env python

import paramiko
from config import inv

"""
Paramiko is a low-level SSHv2 library. Hard dependency on
the cryptography library because it uses C-based
encryption algorithms for the SSH protocol. Used as the
underlying connection protocol for Ansible network modules

Example from "Mastering Python Networking" by Eric Chou
"""

dev = inv.get("iosv-1")

connection = paramiko.SSHClient()

# Automatically adds SSH keys
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Connect to the device
connection.connect(dev.get("host"), username=dev.get("user"), password=dev.get("pass"), look_for_keys=False, allow_agent=False)

# Create connections
new_connection = connection.invoke_shell()

# Number of bytes to receive from open channel
output = new_connection.recv(5000)

# Print output
print(output)

# Run show version
new_connection.send("show version")

# Print show version output (first 5000 bytes)
print(new_connection.recv(5000))

# exec_command() only allows one command at a time
