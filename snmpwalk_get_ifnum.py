#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
このプログラムはhostnameで指定されているホストから、
IF-MIB::ifDescrのTreeを表示します
"""

# 変数
comm = "public"
hostname = "192.168.101.112"

# cmdgen を importする
# pip install pysnmpが必要
# pip install pysnmp-mibs

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.smi import builder, view, error
import sys

def mac2dec(x):
    # "01:2:3:4:5:ff"
    # [1, 2, 3, 4, 5, 255]
    return [int(x, 16) for x in x.split(":")]

mac = "00:0c:29:79:2f:88"

# IF-MIB::ifDescr
mib_ifDescr = ".1.3.6.1.2.1.2.2.1.2"
# BRIDGE-MIB::dot1dTpFdbAddress.
mibid_bridge=".1.3.6.1.2.1.17.4.3.1.1"
# Q-BRIDGE-MIB::dot1qTpFdbPort
mibid_qbridge=".1.3.6.1.2.1.17.7.1.2.2.1.2.7"


# ターゲットのMIB Treeをtupleにする。
# ".1.3.6.1.2.1.2.2.1.2" -> [1, 3, 6, 1, 2, 1, 2, 2, 1, 2]
mibstr2tuple = lambda x: [int(x) for x in mib_ifDescr.split(".")[1:]]
mibtuple = mibstr2tuple(mib_ifDescr)

t = mibid_bridge + "." + ".".join(map(lambda x: str(x), mac2dec(mac)))
mibstr2tuple = lambda x: [int(x) for x in t.split(".")[1:]]
mibtuple = mibstr2tuple(mib_ifDescr)

t = mibid_qbridge + "." + ".".join(map(lambda x: str(x), mac2dec(mac)))
mibstr2tuple = lambda x: [int(x) for x in t.split(".")[1:]]
mibtuple = mibstr2tuple(mib_ifDescr)


print(t)
# 操作用クラスの生成
cmdGen = cmdgen.CommandGenerator()
comm_data = cmdgen.CommunityData(comm, comm)
# 接続先ホスト名とポートの指定
transport = cmdgen.UdpTransportTarget((hostname, int(161)))

errorIndication, errorStatus, errorIndex, result = cmdgen.CommandGenerator().nextCmd(comm_data, transport, mibtuple)
# resultには結果が入っている
# 例: print result[0]
# [(ObjectName(1.3.6.1.2.1.2.2.1.2.1), OctetString('10GigabitEthernet1/1'))]


# errorIndication: None = 異常なし
if errorIndication:
    print(errorIndication)
    sys.exit(1)

# errorStatus: 0 = 正常
if errorStatus:
    print('%s at %s\n' % (
        errorStatus.prettyPrint(),
        errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
        ))
    sys.exit(1)


# 出力を表示
for varBindTableRow in result:
    for name, val in varBindTableRow:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

###











"""

path_to_mib_dir = "/usr/share/mibs/ietf/SNMPv2-SMI"
mibBuilder = builder.MibBuilder()
mibPath = mibBuilder.getMibPath() + ( path_to_mib_dir, )
mibBuilder.setMibPath( *mibPath )
mibBuilder.loadModules( 
    builder.ZipMibSource('SNMPv2-SMI'),
    )
"""
"""
mibBuilder = builder.MibBuilder() 
mibPath = mibBuilder.getMibSources() + (builder.DirMibSource('/usr/share/mibs/'),)
mibBuilder.setMibSources(*mibPath)
mibBuilder.loadModules('SNMPv2-MIB')
mibView = view.MibViewController(mibBuilder)
"""