import os
import socket
import csv


iplist = []

#loop from 1 to 255
# Appends the concatenated ip to the ip_list

for ip in range(1,5):
    iplist.append("192.168.101." + str(ip))

#show me the list of ip address in the list

print("*********ADBY IT AND MEDIA SOLUTIONS NETWORK SCAN*********")
# Loop to ping ip_list and check if device up or down
# Outputs to results.txt file
print("Starting ping test")
for ip in iplist:
   
    response = os.popen(f"ping  {ip} -n 1").read()
    if "Received = 4"  and "Approximate" in response:
        try:
            hostname = socket.gethostbyaddr(ip)
            print(" {}ONLINE".format( hostname))
        except socket.error:
            hostname = "No HOST NAME "
            print(" {}{} ONLINE".format( hostname,ip))
            print({hostname} +  "The System is online")
    else:
        print(f"{ip} OFFLINE")