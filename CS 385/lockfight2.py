#lockfight2.py
#Andrew Poock

import os, time, random

pid = os.getpid()

def main():
    print("PID:", pid)
    for i in range(5):
        try:
            fd = os.open("/home/cs385/Desktop/projects/IPC/andrew.lock", 192)
            locktime = random.randint(1,10)
            print("Process", pid, "aquired the lock for", locktime, "seconds")
            time.sleep(locktime)
            print("Process", pid, "is releasing the lock")
            os.unlink("andrew.lock")
            os.close(fd)
            time.sleep(random.randint(1,10))
        except:
            print("Process", pid, "could not aquire the lock")
            time.sleep(5)
main()
