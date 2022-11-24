#!/bin/python3

import requests
from bs4 import BeautifulSoup

def discover_scripts(url:str):
	soup = BeautifulSoup(requests.get(url, allow_redirects=False).text, features="lxml")
	print("\n[*] Dumping scripts on target webserver...")
	detected = []
	plugins = []
	for x in soup.find_all("script"):
		if x.get("src") == None or x.get("src") == "" or x.get("src") == " ":
			continue
		print("[+] Dumped: " + x.get("src"))
		if "jquery" in x.get("src").lower() and "JQuery" not in detected:
			detected.append("JQuery")
		if "angular" in x.get("src").lower() and "Angular" not in detected:
			detected.append("Angular")
		if "plugin" in x.get("src").lower():
			plugins.append(x.get("src"))
	if detected != []:
		print()
		for i in detected:
			print("[*] Target webserver using: "+i)
	print("\n[*] Dumped plugins ----------------------------------")
	for plugin in plugins:
		print("[*] Plugin: " +plugin)
	print("[*] Dumped plugins ----------------------------------")
