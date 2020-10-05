import whois
import sys
import time
import os
from colorama import *

try:
	if os.name in ['nt','win32','dos']:
		os.system('cls')
	else:
		os.system('clear')
	msg00 = "\n\t\t\033[92m##### XHAMMER WHOIS LOOKUP #####\n\t\t\033[0;96m########## Let's start #########\033[92m\n"
	for i in msg00:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)
	input_file = input('\n\033[92m[+] Enter the Doamin Name to check: >> \033[92m')
	msg01 = "\n\t\t\033[92m##### Looking up whois database for record... #####\n\t\t\033[92m\n"
	for i in msg01:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)

	w = whois.whois(input_file)
	for data,value in w.items():
		print('{} => {}'.format(data,value))
except Exception as Err:
	print('\n\t\t\033[92m[+] Exception occured >> ',Err)
	sys.exit()
else:
	print('\n\nExpected Result Returned =>> ',bool(w.domain_name))
