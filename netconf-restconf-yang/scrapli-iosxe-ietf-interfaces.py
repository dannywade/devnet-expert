from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "192.168.7.160",
    "auth_username": "netconf2",
    "auth_password": "netconf2",
    "auth_strict_key": False,
    "port": 830
}

ospf_config = """
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet3</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>true</enabled>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>10.40.1.1</ip>
              <netmask>255.255.255.0</netmask>
            </address>
          </ipv4>
          <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        </interface>
        <interface>
          <name>Loopback0</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
          <enabled>true</enabled>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>11.11.11.11</ip>
              <netmask>255.255.255.255</netmask>
            </address>
          </ipv4>
          <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        </interface>
      </interfaces>
    </config>
"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.edit_config(config=ospf_config,target="running")
print(response.result)