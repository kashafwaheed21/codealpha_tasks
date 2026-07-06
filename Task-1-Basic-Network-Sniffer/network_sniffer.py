from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0


def packet_callback(packet):
    global packet_count

    if packet.haslayer(IP):
        packet_count += 1
        current_time = datetime.now().strftime("%H:%M:%S")

        print("=" * 60)
        print(f"📦 Packet #{packet_count}")
        print(f"Time             : {current_time}")
        print(f"Source IP        : {packet[IP].src}")
        print(f"Destination IP   : {packet[IP].dst}")

        if packet.haslayer(TCP):
            print("Protocol         : TCP")
            print(f"Source Port      : {packet[TCP].sport}")
            print(f"Destination Port : {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol         : UDP")
            print(f"Source Port      : {packet[UDP].sport}")
            print(f"Destination Port : {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol         : ICMP")

        else:
            print("Protocol         : Other")

        print("=" * 60)


print("Starting Network Sniffer...")
print("Capturing 5 packets...\n")

sniff(prn=packet_callback, count=5)

print("\nSniffing completed successfully!")