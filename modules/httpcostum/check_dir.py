#!/bin/python3

import requests

def check_dirs():
	interest = []
	for dir in open("modules/httpcostum/directorys.txt").read().split("\n"):
		if url[len(url)-1] == "/":
			res = requests.post(url + dir).status_code
		else:
			res = requests.post(url +"/"+ dir).status_code
		if int(res) != 404:
			interest.append("/"+dir +" "+ str(res))
	for x in interest:
		print("[*] Interesting directory: "+ interest.split(" ")[0] +" Status: "+ interest.split(" ")[1])
