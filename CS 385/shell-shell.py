#!/usr/bin/env python3
# file: shell-shell.py

import os, sys


# Modify this function to implement your shell
#   This version just prints out the command line arguments.
def execute(args):
        child = os.fork()
        try:
                if child == 0:
                        if args[-1] == "&":
                                args.pop()
                                os.execvp(args[0], args)
                        else:
                                os.execvp(args[0], args)
                else:
                        if args[-1] != "&":
                                os.wait()
                        else:
                                print(child)
        except:
                print("command not found")

def main():
    while True: # An infinite loop
        try:
            commandLine = input("Andrews shell% ")
        except:
            break  # Quit shell on interrupt or end-of-file
        if commandLine in ["exit", "quit", "logout"]:
            break  # Quit shell on exit
        if commandLine == "" :
            continue # Reprint prompt on blank line.
        if commandLine.strip() != "":
            # split at spaces to create list of strings.
            args = commandLine.split() 
            # pass the list of strings to the execute command.
            execute(args)

main()

