# TCP Covert Channel

## Overview

The TCP Covert Channel is a Python program designed to hide data within TCP packets' Urgent Pointer field, allowing for stealthy communication over a network. This covert communication technique leverages the TCP protocol's Urgent Pointer mechanism, enabling users to exchange data in a clandestine manner.

## Features

- **Data Hiding**: Conceal data within the Urgent Pointer field of TCP packets.
- **Covert Communication**: Facilitate covert communication channels over TCP connections.
- **Secure Communication**: Transmit data discreetly over a network without raising suspicion.
- **Customizable**: Adapt the program for various use cases by modifying the code as needed.
- **Scapy Integration**: Utilize Scapy, a powerful Python library for packet manipulation, to construct and send TCP packets with hidden data.

## Prerequisites

Before using the TCP Covert Channel program, ensure you have the following prerequisites installed:

- Python 3.x
- Scapy library

You can install Scapy using pip:

```
pip install scapy
```
## Usage

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/tcp-covert-channel.git
    ```

2. Navigate to the project directory:

    ```
    cd tcp-covert-channel
    ```

4. Run the local host server

    ```
    python3 server.py
    ```

3. Run the program, specifying the data you want to hide:

    ```
    python3 covert_channel.py "your secret message"
    ```

    Replace `"your secret message"` with the data you wish to conceal within TCP packets. Ensure that you have appropriate permissions and network access to send TCP packets.

