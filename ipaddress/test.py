#!/usr/bin/python
# -*- coding: utf-8 -*-

import ipaddress
from ipaddress import *

print(str(ipaddress.IPv4Address('192.168.0.1')))
# >>> 192.168.0.1

print(IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1'))

print(IPv4Network("192.168.0.2/255.255.255.255"))
a=IPv4Network("192.168.0.2/255.255.255.255")
print(str(a))
