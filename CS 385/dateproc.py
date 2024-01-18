import os

def main():
	child1 = os.fork()
	if child1 == 0:
		os.execl("/bin/date", "date")
	else:
		os.wait()
		print("child process complete")

main()
