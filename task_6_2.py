#!/usr/bin/env python3
ip_addr = input("Введите IP адрес: ")
probe = int(ip_addr.split(".")[0])
if probe > 0:
    if probe < 224:
        print('unicast')
    if probe > 223:
        if probe < 240:
            print('multicast')
        else:
            if ip_addr == '255.255.255.255':
                print('local broadcast')
            else:
                print('unused')
else:
    if ip_addr == '0.0.0.0':
        print('unassigned')
