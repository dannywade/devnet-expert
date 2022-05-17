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
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
          <GigabitEthernet>
            <name>3</name>
            <logging>
              <event>
                <link-status/>
              </event>
            </logging>
            <mop>
              <enabled>false</enabled>
              <sysid>false</sysid>
            </mop>
            <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
              <auto>true</auto>
            </negotiation>
          </GigabitEthernet>
          <Loopback>
            <name>0</name>
            <ip>
              <address>
                <primary>
                  <address>11.11.11.11</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
            <logging>
              <event>
                <link-status/>
              </event>
            </logging>
          </Loopback>
        </interface>
      </native>
    </config>
"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.edit_config(config=ospf_config,target="running")
print(response.result)