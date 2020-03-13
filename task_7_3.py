#!/usr/bin/env python3
f = open("CAM_table.txt","r")
for line in f:
    if line.find("DYNAMIC") == -1:
        continue
    vlan = line.split()[0]
    mac = line.split()[1]
    port = line.split()[3]
    array = [vlan, mac, port]
    string = "  \t  ".join(array)
    print(string)
f.close()