#!/usr/bin/env python3
f = open("ospf.txt", "r")

template = """
Protocol:           {protocol}
Prefix:             {prefix}
AD/Metric:          {metric}
Next-Hop:           {nexthop}
Last update:        {lastupdate}
Outbound Interface: {interface}
"""

for line in f:
    protocol = line.split()[0].replace("O","OSPF").replace("B","BGP").replace("D","EIGRP")
    prefix = line.split()[1]
    metric = line.split()[2].strip("[]")
    nexthop = line.split()[4].rstrip(",")
    lastupdate = line.split()[5].rstrip(",")
    interface = line.split()[6]
    print(template.format(protocol = protocol,
                          prefix = prefix,
                          metric = metric,
                          nexthop = nexthop,
                          lastupdate = lastupdate,
                          interface = interface))

f.close()