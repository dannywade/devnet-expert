from pprint import pprint
from scrapli_netconf.driver import NetconfDriver
import os
import xmltodict
from pprint import pprint
import json


nx_device = {
    "host": "192.168.7.163",
    "auth_username": os.environ.get("CML_USER"),
    "auth_password": os.environ.get("CML_PASS"),
    "auth_strict_key": False,
    "port": 830
}

iosxe_device = {
    "host": "192.168.7.160",
    "auth_username": os.environ.get("CML_USER"),
    "auth_password": os.environ.get("CML_PASS"),
    "auth_strict_key": False,
    "port": 830
}

dial_in_periodic = """
    <config>
      <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
        <mdt-subscription>
          <subscription-id>20</subscription-id>
          <base>
            <stream>yang-push</stream>
            <encoding>encode-kvgpb</encoding>
            <period>1000</period>
            <xpath>/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization</xpath>
          </base>
          <mdt-receivers>
            <address>192.168.7.184</address>
            <port>57344</port>
            <protocol>grpc-tcp</protocol>
          </mdt-receivers>
        </mdt-subscription>
      </mdt-config-data>
    </config>
"""

bgp_periodic = """
    <config>
      <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
        <mdt-subscription>
          <subscription-id>30</subscription-id>
          <base>
            <stream>yang-push</stream>
            <encoding>encode-kvgpb</encoding>
            <period>1000</period>
            <xpath>/bgp-ios-xe-oper:bgp-state-data/neighbors/neighbor/up-time</xpath>
          </base>
          <mdt-receivers>
            <address>192.168.7.203</address>
            <port>57000</port>
            <protocol>grpc-tcp</protocol>
          </mdt-receivers>
        </mdt-subscription>
      </mdt-config-data>
    </config>
"""

dial_in_onchange = """
    <config>
      <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
        <mdt-subscription>
          <subscription-id>25</subscription-id>
          <base>
            <stream>yang-push</stream>
            <encoding>encode-kvgpb</encoding>
            <period>1000</period>
            <xpath>/memory-ios-xe-oper:memory-statistics/memory-statistic</xpath>
          </base>
          <mdt-receivers>
            <address>192.168.7.203</address>
            <port>57000</port>
            <protocol>grpc-tcp</protocol>
          </mdt-receivers>
        </mdt-subscription>
      </mdt-config-data>
    </config>
"""

conn = NetconfDriver(**iosxe_device)
conn.open()
response = conn.edit_config(config=bgp_periodic, target="running")
conn.close()

print(response.result)

