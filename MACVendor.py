import os
print(r""" 
_____ _____ _____ _____           _         
|     |  _  |     |  |  |___ ___ _| |___ ___ 
| | | |     |   --|  |  | -_|   | . | . |  _|
|_|_|_|__|__|_____|\___/|___|_|_|___|___|_|  

   >>> MAC Address lookup                  """)
      
      
while True:
    
    print('\n')
    
    macInput = input('Please enter the mac address: ')

    print('\nMac Address Vendor: ')

    print('\n')
    
    print('\033[1m')
    
    os.system('curl http://api.macvendors.com/' + macInput)

    print('\n')
    
    print('\033[0m')
    
    inp = input('\nWould you like to check another mac address? (y/n): ')
    
    if(inp == "y" or inp == "Y"):
      
      continue
    
    else:
      
      print('\n Ciao!')
      
      print('\n')
      
      break
