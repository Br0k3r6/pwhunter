#!/bin/python3

global url

import requests
from bs4 import BeautifulSoup
import threading

# CUSTOM IMPORTS

from modules.httpcostum.http_file_check import *
from modules.httpcostum.http_header_check import *
from modules.httpcostum.check_wordpress import *
from modules.httpcostum.script_discover import *

def start_scan(url:str):
	try:
		requests.get(url, allow_redirects=False)
	except requests.ConnectionError:
		print("[-] There was an ConnectionError to target webserver!")
		exit()
	except:
		print("[-] There was an ConnectionError to target webserver!")
		exit()
	if check_robots(url) == 0:
		check_robots_info(url)
	print()
	check_headers(url)
	print()
	check_wordpress(url)
	discover_scripts(url)
