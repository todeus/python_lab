#!/usr/bin/env python3
#from sys import argv:
argv = "config_sw1.txt"
ignore = ['duplex', 'alias', 'Current configuration']
ignore.append("!")
f = open(argv,"r")
for line in f:
    skip = 0
    for i in ignore:
        if line.find(i) != -1:
            skip = 1
    if skip == 0:
        print(line)
f.close()