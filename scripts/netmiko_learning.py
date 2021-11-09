#! /usr/bin/env python

from netmiko import ConnectHandler
from config import inv
"""
Netmiko is a fork of Paramiko and simplifies the
channel management when connecting to a network device

Example from "Mastering Python Networking" by Eric Chou
"""

dev = inv.get("iosv-1")

# Define the device to connect to
ios_v1 = {
    "device_type": dev.get("type"),
    "host": dev.get("host"),
    "username": dev.get("user"),
    "password": dev.get("pass")
    }

# Connect to the device
net_connect = ConnectHandler(**ios_v1)

# Automatically knows the prompt
net_connect.find_prompt()  # "iosv-1#"

# Run show version
output = net_connect.send_command("show version")

# Send multiple commands at once
output2 = net_connect.send_config_set(["logging buffered 19999", "logging host 10.1.1.1"])