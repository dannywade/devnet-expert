## Dynamic subscriptions
- Created by the subscribers and only last as long as the connection
- Not configured into the running-config

### NETCONF Dial-in
- `<establish-subscription>` RPC
- `IETF-event-notification` YANG module
- XPath filter format: `/prefix:xpath` (check node properties in YANG Suite)
- Periodic update is in 1/100 of a second (A period of 1000 results = 10 seconds)
- Following fields are required in the RPC: `stream`, `xpath-filter`, and `period`
- Check IOS-XE example here: [NETCONF dial-in example](netconf-dial-in/example_memory_oper.xml)

### gRPC Dial-out
- Can be configured via CLI or NETCONF RPC message
- Only Key-value Google Protocol Buffers (kvGPB) encoding supported with gRPC transport
- `Cisco-IOS-XE-mdt-cfg` YANG module to configure via NETCONF
- No need to specify keys in XPath for telemetry.
    - Example: `/bgp-ios-xe-oper:bgp-state-data/neighbors/neighbor/up-time` (did not specify neighbor)
- Check IOS-XE examples here: 
    - [gRPC BGP dial-out example](grpc-dial-out/example_bgp_oper.xml)
    - [gRPC CPU dial-out example](grpc-dial-out/example_cpu_oper.xml)