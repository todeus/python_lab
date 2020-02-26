#!/usr/bin/env python3
arg = input("Введите адрес сети в формате 10.0.0.0/24: ")
oct1 = int(arg.split(".")[0])
oct2 = int(arg.split(".")[1])
oct3 = int(arg.split(".")[2])
oct4 = int(arg.split(".")[3].split("/")[0])
mask = int(arg.split(".")[3].split("/")[1])
nulls = 32-mask
str_mask = "1"*mask+"0"*nulls
mask1 = int(str_mask[0:8], 2)
mask2 = int(str_mask[8:16], 2)
mask3 = int(str_mask[16:24], 2)
mask4 = int(str_mask[24:32], 2)


template = """
Network:
{o1:<8} {o2:<8} {o3:<8} {o4:<8}
{o1:08b} {o2:08b} {o3:08b} {o4:08b}

Mask:
/{m}
{m1:<8} {m2:<8} {m3:<8} {m4:<8}
{m1:08b} {m2:08b} {m3:08b} {m4:08b}
"""
print(template.format(o1=oct1, o2=oct2, o3=oct3, o4=oct4, m=mask, m1=mask1, m2=mask2, m3=mask3, m4=mask4))
