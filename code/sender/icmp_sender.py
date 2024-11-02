import scapy.all
RECIEVER_IP = "172.19.0.3"

pkt = scapy.all.IP(dst = RECIEVER_IP, ttl = 1)/scapy.all.ICMP()

scapy.all.send(pkt)

# Implement your ICMP sender here
