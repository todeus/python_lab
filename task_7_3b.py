#!/usr/bin/env python3
f = open("CAM_table.txt","r")
i = 0
get_vlan = input("Введите номер VLAN: ")
dictionary = {}
for line in f:
    if line.find("DYNAMIC") == -1:
        continue
    vlan = line.split()[0]
    if vlan != get_vlan:
        continue
    mac = line.split()[1]
    port = line.split()[3]
    array = [vlan, mac, port]
    string = "  \t  ".join(array)
    i += 1
    vlan_i = int(vlan) + i
    dictionary.setdefault(vlan_i,string)
index = sorted(dictionary)
for i in index:
    print(dictionary[i])

f.close()