from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "192.168.7.160",
    "auth_username": "netconf2",
    "auth_password": "netconf2",
    "auth_strict_key": False,
    "port": 830
}

bgp_config = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
            <id xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="merge">65001</id>
            <bgp>
              <log-neighbor-changes>true</log-neighbor-changes>
            </bgp>
            <neighbor>
              <id>10.250.1.2</id>
              <remote-as>65002</remote-as>
              <log-neighbor-changes>
                <disable/>
              </log-neighbor-changes>
            </neighbor>
            <neighbor>
              <id>10.250.1.3</id>
              <remote-as>65003</remote-as>
              <log-neighbor-changes>
              </log-neighbor-changes>
            </neighbor>
          </bgp>
        </router>
      </native>
    </config>
"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.edit_config(config=bgp_config,target="running")
print(response.result)