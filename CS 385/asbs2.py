#!usr/bin/env python3
import sys
import os

HOWMANY = 2000

def main():
	child1 = os.fork()
	if child1 == 0:
		for i in range(HOWMANY):
			sys.stdout.write("a")
			sys.stdout.flush()
	else:
		child2 = os.fork()
		if child2 == 0:
			for i in range(HOWMANY):
				sys.stdout.write("b")
				sys.stdout.flush()
		else:
			os.wait()
			os.wait()
			sys.stdout.write("all done!")
			sys.stdout.flush()

main()
