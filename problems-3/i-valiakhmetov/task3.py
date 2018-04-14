#!/bin/python3

import sys

class LazyRead(object):
	def __init__(self, f):
		self.__chunk = 512

	def __iter__(self):
		return self

	def __next__(self):
		self.__data = f.read(self.__chunk)
		if len(self.__data) == 0:
			raise StopIteration
		return self.__data
		
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Usage: %s filename' % sys.argv[0])

	with open(sys.argv[1], "r") as f:
		a = LazyRead(f)
		for chunk in a:
			print(chunk)