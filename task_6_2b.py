#!/usr/bin/env python3
while True:
    ip_addr = input("Введите IP адрес: ")
    oct = ip_addr.split(".")
    bool = True
    for oc in oct:
        try:
           bool &= (int(oc) >= 0) & (int(oc) <= 255)
        except ValueError:
            print("IP адрес должен быть в виде 192.168.1.100")
    if ((len(oct) == 4) & bool):
        probe = int(oct[0])
        if probe > 0:
            if probe < 224:
                print('unicast')
                break
            if probe > 223:
                if probe < 240:
                    print('multicast')
                    break
                else:
                    if ip_addr == '255.255.255.255':
                        print('local broadcast')
                        break
                    else:
                        print('unused')
                        break
        else:
            if ip_addr == '0.0.0.0':
                print('unassigned')
                break
    else:
        print('Неправильный IP адрес')
