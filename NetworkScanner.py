import scapy.all as scapy
import re

ip_add_range_pattern = re.compile('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$')

while True:
    
      ip_add_range_entered = input('\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ')
    
      if ip_add_range_pattern.search(ip_add_range_entered):
            print('\n')
            print(f'{ip_add_range_entered} is a valid ip address range')
            print('\n')
            break

arp_result = scapy.arping(ip_add_range_entered)

print('\n')


