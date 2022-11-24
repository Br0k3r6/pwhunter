#!/bin/python3

import requests

def check_robots_info(url):
	if url[len(url)-1] == "/":
		robots = requests.get(url+"robots.txt", allow_redirects=False).text
		robots = str(robots).split("\n")
		print("[*] Robots.txt file found! " + url + "robots.txt")
	else:
		robots = requests.get(url+"/robots.txt", allow_redirects=False).text
		robots = str(robots).split("\n")
		print("[*] Robots.txt file found! " + url + "/robots.txt")
	for local in robots:
		if local == "" or local == " ":
			continue
		print("     -- " + local)

def check_robots(url):
	if url[len(url)-1] == "/":
		response = requests.post(url+"robots.txt", allow_redirects=False).status_code
		if response == 200:
			del response
			return 0
		else:
			del response
			return -1
	else:
		response = requests.post(url+"/robots.txt", allow_redirects=False).status_code
		if response == 200:
			del response
			return 0
		else:
			del response
			return -1
