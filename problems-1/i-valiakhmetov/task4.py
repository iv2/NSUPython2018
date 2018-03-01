#!/bin/python

import os, sys, stat

def mylistdir(lpath):
	files = {}
	for f in os.listdir(lpath):
		pathname = os.path.join(lpath, f)
		fstat = os.stat(pathname)
		if os.path.isfile(pathname):
			files[f] = fstat.st_size;

	return sorted([(value, key) for (key, value) in files.items()])

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		raise ValueError("specify path")

	if os.path.isdir(sys.argv[1]):
		flist = mylistdir(sys.argv[1])
		for k, v in flist:
			print(k, v)
	else:
		print("not a directory")
