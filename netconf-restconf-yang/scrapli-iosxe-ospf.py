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
        <router>
          <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <ospf>
              <process-id>
                <id>100</id>
                <network>
                  <ip>10.0.0.0</ip>
                  <wildcard>0.255.255.255</wildcard>
                  <area>0</area>
                </network>
              </process-id>
            </ospf>
          </router-ospf>
        </router>
      </native>
    </config>
"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.edit_config(config=ospf_config,target="running")
print(response.result)