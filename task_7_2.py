#!/usr/bin/env python3
#from sys import argv:
argv = "config_sw1.txt"
f = open(argv,"r")
for line in f:
    if line.startswith("!"):
        continue
    print(line)
f.close()