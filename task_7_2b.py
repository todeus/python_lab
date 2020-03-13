#!/usr/bin/env python3
#from sys import argv:
argv1 = "config_sw1.txt"
argv2 = "config_sw1_cleared.txt"
ignore = ['duplex', 'alias', 'Current configuration']
#ignore.append("!")
with open(argv1,"r") as f, open(argv2,"w") as dest:
    for line in f:
        skip = 0
        for i in ignore:
            if line.find(i) != -1:
                skip = 1
        if skip == 0:
            dest.write(line)
