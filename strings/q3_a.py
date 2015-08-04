#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 結果として想定される文字列をstrに代入
str1="""
Router>show int
FastEthernet0 is up, line protocol is up 
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
FastEthernet1 is up, line protocol is up 
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  5 minute input rate 1000 bits/sec, 1 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec

"""

str2="""
Router>show int status 
Port    Name               Status       Vlan       Duplex Speed Type
Fa2     uplink             notconnect   1            auto    auto 10/100BaseTX
Fa3     user1              notconnect   2            auto    auto 10/100BaseTX
Fa4     server             notconnect   3            full     100 10/100BaseTX
Fa5     none               notconnect   1            auto    auto 10/100BaseTX
"""

