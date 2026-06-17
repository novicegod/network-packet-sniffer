from scapy.all import sniff, IP, TCP, UDP
import csv
import os

csv_file = "network_stats.csv"
with open(csv_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Protocol", "Source_IP", "Destination_IP"])

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
        else:
            proto = "OTHER"
            
        with open(csv_file, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([proto, src_ip, dst_ip])

print("🚀 Backend Sniffer running... Writing data to network_stats.csv")
sniff(store=0, prn=packet_callback)