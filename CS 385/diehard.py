#!/usr/bin/env python3
# diehard.py - Andrew Poock
# use: kill -# pid

from signal import *
import sys, os, time

def handler(signal, traceback):
    print("Got Signal:", signal)

def main():
    print("My PID is:", os.getpid())
    print("I'm an immortal process, you can't kill me!")
    hits = 0
    for i in range(1, NSIG):
        if i not in [9, 19, 32, 33]:
            signal(i, handler)
    while hits < 5:
        pause()
        hits += 1
        print("Hit number:", hits)
    print("Noooo! I have been defeated.")

main()
