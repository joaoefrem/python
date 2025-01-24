import os
import csv
import time
import datetime
import logging
 
def check_ping(hostname):
    response = os.system("fping -r 5 -q " + hostname + " >/dev/null")
    if response == 0:
        check_ping = "[OK]"
    else:
        check_ping = "[Error]"
  
    return check_ping
 
with open('ip-source.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
      
    for ip in dump:
         
        #os.system('cls')
        print('Pinging now:', ip)
        #print('-'*10)
        os.system('ping -n 2 {}'.format(ip))
        #print('-'*10)
        #time.sleep(2)