import whois
import sys
import time
import os
from colorama import *


def whois_lookup(domain):
	w = whois.whois(domain)
	return w 

def registrar(domain):
	whois_info = whois.whois(domain)
	data = whois_info.registrar
	return data

def emails(domain):
	data = []
	whois_info = whois.whois(domain) 
	for da in whois_info.emails:
		if da is None:
			return
		data.append(da)
		data.sort()
	return data

def name_server(domain):
	data = []
	whois_info = whois.whois(domain)
	for da in whois_info.name_servers:
		data.append(da)
		data.sort()
	return data

def status(domain):
	data = []
	whois_info = whois.whois(domain)
	for da in whois_info.status:
		 data.append(da)
		 data.sort()
	return data

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
	list_data = []
	input_file = input('\n\033[92m[+] Enter the Doamin Name to check: >> \033[92m')
	msg01 = "\n\t\t\033[92m##### Looking up whois database for record... #####\n\t\t\033[92m\n"
	for i in msg01:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)

	w = whois_lookup(input_file)
	print(w)


	print('\n\t\t [+] EMAILS >> ')
	list_data = emails(input_file) 
	for data in list_data:
		if data is None:
			pass
		print(data)

	print('\n\t\t [+] REGISTRAR >>')
	list_data = registrar(input_file)
	print(list_data)

	print('\n\t\t [+] STATUS >> \n')
	list_data = status(input_file)
	for data in list_data:
		print(data)
	print('\n\t\t [+] NAME SERVERS >> \n')
	list_data = name_server(input_file)
	for data in list_data:
		print(data)
except Exception as Err:
	print('\n\t\t\033[92m[+] Exception occured >> ',Err)
	sys.exit()
else:
	print('\n\nExpected Result Returned =>> ',bool(w.domain_name))
