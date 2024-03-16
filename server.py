import socket
from scapy.all import *

HOST = "127.0.0.1"
PORT = 3000


def convert_to_characters(urgent_pointer):
    # Split the binary string into two 8-bit chunks
    chunk1 = urgent_pointer[:8]
    chunk2 = urgent_pointer[8:]
    
    # Convert each chunk to character
    character1 = chr(int(chunk1, 2))
    character2 = chr(int(chunk2, 2))
    
    return character1 + character2


# Function to handle packet processing
def process_packet(packets):
    hidden_message = ""

    for packet in packets:

        try:
            packet = Ether(packet)        
            if packet.haslayer(TCP):
                urgent_pointer = format(packet[TCP].urgptr, '016b')  # Get binary string
                characters = convert_to_characters(urgent_pointer)
                hidden_message += characters
                print("Urgent Pointer Characters:", characters)
        except Exception as e:
            print("Error parsing packet:", e)  # Handle parsing errors
    
    print(hidden_message)


# Socket setup
with socket.socket(socket.AF_INET) as s:
    print("Listening...")
    s.bind((HOST, PORT))
    s.listen(1)

    received_data = []
    while True:
        conn, addr = s.accept()
        print("Connected by:", addr)

        # Receive data loop for handling multiple packets
        while True:
            data = conn.recv(1024)  # Adjust buffer size as needed
            if not data:
                break  # No more data, exit loop
            received_data.append(data)

        # Process received data
        process_packet(received_data)
        conn.close()
        received_data = []
