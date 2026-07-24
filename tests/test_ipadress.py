import ipaddress

network = ipaddress.ip_network("192.168.100.4/24", strict=False)

#print(network)
#print(type(network))
#print(network.network_address)
#print(network.broadcast_address)
#print(network.netmask)
#print(network.prefixlen)
#print(network.num_addresses)
#print(network.hosts())
for i, host in enumerate(network.hosts()):
    print(host)

    if i == 9:
        break