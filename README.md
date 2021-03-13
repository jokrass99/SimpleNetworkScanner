# SimpleNetworkScanner
Simple python based Network Scanner, that trys ARPing the ip address range supplied by the user and returns a list of connected devices with their ip and mac address. 
The arping() method in scapy creates a packet with an ARP message and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff. 
If a valid ip address range was supplied the program will return the list of all results.

The repository also includes another basic python script for finding the vendor of a MAC address.



__Usage:__
  
1.  Copy the script with: `git clone https://github.com/jokrass99/SimpleNetworkScanner.git`
  
2.  Change to the scripts directory: `cd SimpleNetworkScanner/`
  
3.  Run _NetworkScanner_ script: `python3 ./SimpleNetworkScanner.py`

    Run _MACVendor_ script : `python3 ./MACVendor.py`


![NetworkScanner](https://user-images.githubusercontent.com/72883058/111014548-0eb7de80-839c-11eb-840b-ef228a8a6ba9.png)
