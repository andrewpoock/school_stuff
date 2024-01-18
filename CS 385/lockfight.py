# lockfight.py
# Andrew Poock

from _thread import *
from time import sleep
from random import randint

done = False

def getlock(threadname, lock):
    global done
    for i in range(5):
        lock.acquire()
        locktime = randint(1, 5)
        print(threadname, "aquired the lock for", locktime, "seconds")
        sleep(locktime)
        print(threadname, "has released the lock")
        lock.release()
        sleep(1)
    done = True

def main():
    lock = allocate_lock()
    thread0 = start_new_thread(getlock, ("Thread 0", lock))
    thread1 = start_new_thread(getlock, ("Thread 1", lock))
    while done != True and lock.locked != False:
        pass
    sleep(1)
    print("Main thread exiting")
    exit()

main()
