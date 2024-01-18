#!/usr/bin/env python3
# Dining Philosophers shell
# Code shamefully borrowed from Dr. John Zelle. Thanks, Dr. Zelle!
# Andrew Poock

# system modules
from random import randint
import _thread, time, signal

# local modules
from DPGui import DPDisplay
from semaphores import Semaphore

NUM_PHILOSOPHERS = 5   # changeable from command-line
THINKMAX = 6
EATMAX = 2

def philosopher(i, display, forks):
    # behavior of the ith philosopher - code goes here
    while True:
        time.sleep(randint(0,6))
        forks[i].wait()
        display.setFork(i, "inuse")
        display.setPhil(i, "hungry")
        time.sleep(1)
        if forks[(i+1) % NUM_PHILOSOPHERS].getStatus() == 1:
            forks[(i+1) % NUM_PHILOSOPHERS].wait()
            display.setFork((i+1) % NUM_PHILOSOPHERS, "inuse")
            display.setPhil(i, "eating")
            time.sleep(randint(1,2))
            forks[(i+1) % NUM_PHILOSOPHERS].post()
            display.setFork((i+1) % NUM_PHILOSOPHERS, "free")
            display.setPhil(i, "hungry")
            forks[i].post()
            display.setFork(i, "free")
            display.setPhil(i, "thinking")
        else:
            forks[i].post()
            display.setFork(i, "free")
            display.setPhil(i, "thinking")
        
def main():
    d = DPDisplay(NUM_PHILOSOPHERS)
    forks = []
    for i in range(NUM_PHILOSOPHERS):
        forks.append(Semaphore(1))
        d.setFork(i,"free")
    for i in range(NUM_PHILOSOPHERS):
        _thread.start_new_thread(philosopher, (i,d,forks))
    d.pause()  # wait for mouse click to keep main thread alive


# Use command-line argument to change number of philosophers
from sys import argv
if len(argv) > 1:
    NUM_PHILOSOPHERS = int(argv[1])

main()         # Run main program to launch philosophers
