import scapy.all

pkt = scapy.all.sniff(count=1, filter="icmp")[0]
pkt.show()
