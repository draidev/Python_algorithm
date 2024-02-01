from scapy.all import rdpcap, wrpcap, IP
  
# PCAP 파일 읽기
packets = rdpcap('pkt_2024_01_29_01_00_00_00.cap')

# 수정된 패킷을 저장할 리스트
modified_packets = []

# 패킷 순회
for packet in packets:
    # IP 레이어가 있는 패킷만 수정
    if IP in packet:
        if packet[IP].src == "192.168.6.1":
            packet[IP].src = "192.168.165.1"
        if packet[IP].dst == "192.168.6.1":
            packet[IP].dst = "192.168.165.1"

        # 필요한 경우, 목적지 IP도 수정할 수 있습니다:
        # packet[IP].dst = "새로운_목적지_IP"

    modified_packets.append(packet)

# 수정된 패킷을 새로운 PCAP 파일로 저장
wrpcap('pkt_2024_01_29_02_01_00_00.cap', modified_packets)