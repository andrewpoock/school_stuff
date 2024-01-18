import sys
import os
import time

def main():
	child1 = os.fork()
	if child1 == 0:
		ppid = os.getppid()
		print("PPID:", ppid)
		time.sleep(10)
		print("Child terminating")
		sys.exit(13)
	else:
		print("Child PID:", child1)
		_, status = os.wait()
		print("Child terminated with id", os.WEXITSTATUS(status))

main()
