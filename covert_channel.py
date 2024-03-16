import socket
import sys
from scapy.all import *

HOST = "127.0.0.1"
PORT = 3000


def char_to_binary(char):
    ascii_code = ord(char)
    padded_binary = bin(ascii_code)[2:].zfill(8)     # Remove the '0b' prefix and zero-pad the binary representation to ensure it's 8 bits long

    return padded_binary
    

def split_into_16bit_chunks(binary_data):
    chunks = []
    
    # Iterate over the binary data in chunks of 16 bits
    for i in range(0, len(binary_data), 16):
        chunk = binary_data[i:i+16]  # Extract a 16-bit chunk and append it to the list
        chunks.append(chunk)
    
    return chunks


def convert_to_16bit_chunks(data):
    binary_chars = []
    for char in data:
        binary_chars.append(char_to_binary(char))
            
    binary_data = ''.join(binary_chars)     # Join the binary representations into a single binary string
    chunks = split_into_16bit_chunks(binary_data)
    
    return chunks


def sendData(data):
    with socket.socket(socket.AF_INET) as s:
        s.connect((HOST, PORT))

        for chunk in data:
            packet = Ether() / IP(dst=HOST) / TCP(dport=PORT, flags="U", urgptr=int(chunk, 2))
            s.send(bytes(packet)) 


if len(sys.argv) > 1:
    secret_data = sys.argv[1]
    chunks = convert_to_16bit_chunks(secret_data)
    
    sendData(chunks)
else:
    print("Invalid input")


