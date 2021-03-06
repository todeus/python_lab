#!/usr/bin/env python3
type = input("Введите режим работы интерфейса (access/trunk): ")
intf = input("Введите тип и номер интерфейса: ")

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = {
    'access' : access_template,
    'trunk' : trunk_template
}

message = {
    'access' : 'Введите номер VLAN: ',
    'trunk' : 'Введите разрешенные VLANы: '
}

vlan = input(message[type])

template_all = 'interface '+intf+'\n '+'\n '.join(template[type])
print(template_all.format(vlan))
