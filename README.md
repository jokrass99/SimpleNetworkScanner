# SimpleNetworkScanner
Simple python based Network Scanner, that trys ARPing the ip address range supplied by the user and returns a list of connected devices with their ip and mac address. 
The arping() method in scapy creates a packet with an ARP message and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff. 
If a valid ip address range was supplied the program will return the list of all results.

Usage:
1. git clone https://github.com/jokrass99/SimpleNetworkScanner.git
2. cd SimpleNetworkScanner/
3. python3 ./SimpleNetworkScanner.py

![NetworkScanner](https://user-images.githubusercontent.com/72883058/111011091-4c166f00-8390-11eb-839d-a6888c6b97a9.png)
