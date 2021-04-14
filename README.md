# SimpleNetworkScanner
Simple python based Network Scanner, that trys ARPing the IP address range supplied by the user and returns a list of connected devices with their IP and MAC address. 
The arping() method in scapy creates a packet with an ARP message and sends it to the broadcast MAC address. 
If a valid ip address range was supplied, the program will return the list of all results.

The repository also includes another basic python script for finding the vendor of a MAC address.

__Requirements:__

1. Python 3 installed
2. scapy installed (installation: `pip install scapy`)
3. Any Linux distro (also works under Windows)


__Usage:__
  
1.  Clone the repository with: `git clone https://github.com/jokrass99/SimpleNetworkScanner.git`
  
2.  Go to the scripts directory: `cd SimpleNetworkScanner/`
  
3.  Run _NetworkScanner_ script: `python3 ./SimpleNetworkScanner.py`

    Run _MACVendor_ script : `python3 ./MACVendor.py`


![NetworkScanner](https://user-images.githubusercontent.com/72883058/111014548-0eb7de80-839c-11eb-840b-ef228a8a6ba9.png)
![MACVendor](https://user-images.githubusercontent.com/72883058/111016106-e9c76980-83a3-11eb-8678-98d0b85c5de4.png)
