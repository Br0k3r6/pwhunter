#!/bin/python3

import requests
from bs4 import BeautifulSoup

def check_wordpress(url:str):
	if url[len(url)-1] == "/":
		response = requests.post(url+"wp-login.php", allow_redirects=False)
	else:
		response = requests.post(url+"/wp-login.php", allow_redirects=False)
	if response.status_code != 404:
		soup = BeautifulSoup(requests.get(url).text, features="lxml")
		version = None
		for index in soup.find_all("meta"):
			if index.get("content") == None:
				continue
			if "WordPress" in index.get("content") and "." in index.get("content") and "org" not in index.get("content")  and not "http://" in index.get("content") and not "https://" in index.get("content"):
				version = index.get("content")
		if version == None:
			version = "WordPress"

		print("[*] " + version + " detected on target webserver!")
		if url[len(url)-1] == "/":
			print("    WP-Login: " + url+"wp-login.php")
		else:
			print("    WP-Login: " + url+"/wp-login.php")
		if url[len(url)-1] == "/":
			print("    WP-Dashboard: " + url+"wp-admin.php")
		else:
			print("    WP-Dashboard: " + url+"/wp-admin.php")
		if url[len(url)-1] == "/":
			request = "wp-content/uploads/wpo-plugins-tables-list.json"
			response = requests.post(url + request, allow_redirects=False).status_code
			if response != 404:
				print("    WP-Plugins: " + url + request)
		else:
			request = "/wp-content/uploads/wpo-plugins-tables-list.json"
			response = requests.post(url + request, allow_redirects=False).status_code
			if response != 404:
				print("    WP-Plugins: " + url + request)



		if url[len(url)-1] == "/":
			response = requests.post(url+"wp-json", allow_redirects=False)
			if response.status_code == 200:
				print("    WP-Json: " + url+"wp-json")
		else:
			response = requests.post(url+"/wp-json", allow_redirects=False)
			if response.status_code == 200:
				print("    WP-Json: " + url+"/wp-json")
