# SimpleNetworkScanner
Simple python based Network Scanner, that trys ARPing the ip address range supplied by the user and returns a list of connected devices with their ip and mac address. 
The arping() method in scapy creates a packet with an ARP message and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff. 
If a valid ip address range was supplied the program will return the list of all results.

__Usage:__
1.  Copy the script with: 
2.  `git clone https://github.com/jokrass99/SimpleNetworkScanner.git`
3.  
4.  Change to the scripts directory: 
5.  `cd SimpleNetworkScanner/`
6.  
7.  Run the script: 
8.  `python3 ./SimpleNetworkScanner.py`


![NetworkScanner](https://user-images.githubusercontent.com/72883058/111014548-0eb7de80-839c-11eb-840b-ef228a8a6ba9.png)
