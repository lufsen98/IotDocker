from scapy.all import sniff, ARP

def arp_display(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1:
            return f"Request: {pkt[ARP].psrc} is asking about {pkt[ARP].pdst}"
        if pkt[ARP].op == 2:
            return f"*Response: {pkt[ARP].hwsrc} has adress {pkt[ARP].psrc}"

print("Sniffing ARP packets....")
sniff(prn=arp_display, filter = "arp", store = 0, count = 0)

