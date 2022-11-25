#!/bin/python3

import requests

def check_headers(url:str):
	response = requests.post(url, allow_redirects=False)
	headers = response.headers
	for x in headers:
		print("[*] " + x + " = " + headers[x])

	try:
		found = 0
		print()
		try:
			headers['X-XSS-Protection']
			print("[!] X-XSS-Protection header is defined!")
		except:
			print("[*] X-XSS-Protection header is not defined!")
		print("[*] Checking for exploits...")
		if headers['X-Powered-By'] == "PHP/8.1.0-dev":
			found = 1
			print("[*] [EXPLOIT] Directory exploits/PHP-8.1.0-dev/exploit.cpp")
		if found == 0:
			print("[!] No exploits found for http headers (not injectable)")
	except:
		if found == 0:
			print("[!] No exploits found for http headers (not injectable)")
		return -1
