from scapy import all as scapy
from collections import defaultdict

packets = []
_iface = "enx04bf1b9ed863"
sent = defaultdict(lambda : 1)


class TCPAnalyzer:
    def __init__(self, packet):
        self.packet = packet
        self.analyze()

    def analyze(self):
        if self.packet.haslayer(scapy.TCP):
            tcp_layer = self.packet[scapy.TCP]
            seq_number = tcp_layer.seq
            print(f"TCP Sequence Number: {seq_number}")

            # Optionally modify TCP flags and send
            tcp_layer.flags = "FA"  # Set FIN flag
            scapy.sendp(self.packet, iface=_iface)
            print(f"Sent modified packet with FIN flag.")


    def __repr__(self):
        return self.packet.__str__()

    def __str__(self):
        return self.packet.__str__()


# Sniff TCP packets on the specified interface
scapy.sniff(iface="enx04bf1b9ed863", filter="tcp", prn=TCPAnalyzer)
