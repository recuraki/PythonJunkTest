#!/usr/bin/python
# -*- coding: utf-8 -*-

# 結果として想定される文字列をstrに代入
str="""
Cisco#show standby brief 
Load for five secs: 2%/0%; one minute: 2%; five minutes: 2%
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Gi0/0/3.11 1    110 P Init    unknown         unknown         10.0.81.1
Gi0/0/3.201
            1    110 P Init    unknown         unknown         10.0.1.1
Gi0/0/3.202
            1    110 P Init    unknown         unknown         10.0.2.1
Gi0/0/3.203
            1    110 P Init    unknown         unknown         10.0.3.1
Gi0/0/3.204
            1    110 P Init    unknown         unknown         10.0.4.1
Gi0/0/3.205
            1    110 P Init    unknown         unknown         10.0.5.1
Gi0/0/3.206
            1    110 P Init    unknown         unknown         10.0.6.1
Gi0/0/3.207
            1    110 P Init    unknown         unknown         10.0.7.1
Gi0/0/3.208
            1    110 P Init    unknown         unknown         10.0.8.1
Gi0/0/3.209
            1    110 P Init    unknown         unknown         10.0.9.1
Gi0/0/3.210
            1    110 P Init    unknown         unknown         10.0.10.1
Gi0/0/4     1    110 P Init    unknown         unknown         10.0.11.1
Gi0/0/5     1    110 P Init    unknown         unknown         10.0.21.1
"""

"""
output
Gi0/0/3.201 Init
Gi0/0/3.202 Init
Gi0/0/3.203 Init
Gi0/0/3.204 Init
Gi0/0/3.205 Init
Gi0/0/3.206 Init
Gi0/0/3.207 Init
Gi0/0/3.208 Init
Gi0/0/3.209 Init
Gi0/0/3.210 Init
Gi0/0/4 Init
Gi0/0/5 Init
"""

# まず、元の文字列を表示
print("Original:")
print("[" + str + "]")

import re

r = re.finditer("(Gi[^ ]+)[ \n]+ +[0-9]+ +[0-9]+ +. ([^ ]+) +[^ ]+", str)
for res in r:
    eth = res.group(1).strip()
    stat = res.group(2)
    print eth,stat
