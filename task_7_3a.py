#!/usr/bin/env python3
f = open("CAM_table.txt","r")
i = 0
dictionary = {}
for line in f:
    i += 1
    if line.find("DYNAMIC") == -1:
        continue
    vlan = line.split()[0]
    mac = line.split()[1]
    port = line.split()[3]
    array = [vlan, mac, port]
    string = "  \t  ".join(array)
    vlan_i = int(vlan) + i
    dictionary.setdefault(vlan_i,string)
index = sorted(dictionary)
for i in index:
    print(dictionary[i])

f.close()