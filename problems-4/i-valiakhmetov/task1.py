#!/bin/python

import urllib2
import bs4
import sys
import re
import time 


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Usage: %s filename' % sys.argv[0])

	phil = "/wiki/Philosophy"
	next_link = sys.argv[1]
	link_list = []

	while True:
		req = urllib2.Request(next_link)
		response = urllib2.urlopen(req)
		html = response.read()
		soup = bs4.BeautifulSoup(html, "html.parser")

		content = soup.find("div", {"id": "mw-content-text"})
		main_p = content.find("p")
		for link in main_p.find_all("a", href=True):
			if link['href'][0] == "#":
				pass
			else:		
				if link['href'] == phil:
					print("https://wikipedia.org"+link['href'])
					sys.exit("Found!");

				if link['href'] in link_list:
					sys.exit("cycle!");
				else:
					link_list.append(link['href'])
					print("https://wikipedia.org"+link['href'])
					break
				next_link = "https://wikipedia.org"+link['href']
		time.sleep(1)
