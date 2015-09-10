#!/usr/local/bin/python

from pprint import pprint
from jnpr.junos import Device

dev = Device(host='172.16.174.201', user='test', password='test123' )

dev.open()

pprint( dev.facts )

dev.close()
