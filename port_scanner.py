#!/bin/python3

import sys
import socket
from datetime import datetime 

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid input")
	print("Syntax --> python3 port_scanner.py <IP>")
# Adding Banner
print("-" * 50)

print("Scanning target: "+ target)
print("Time Started: "+ str(datetime.now()))

print("-" * 50)

try:
	for port in range(1,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # connect_ex Error indicator
		if result == 0:
			print("Port {} is open".format(port))
	s.close()
	
except KeyboardInterrupt: # for ctrl + c
	print("\nExiting...")
	
# This exception for if anyone type like this python3 port_scaaner.py ldvnwe
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not be Connect to the server.")
	sys.exit()
	

