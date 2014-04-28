#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
このプログラムはhostnameで指定されているホストから、
IF-MIB::ifDescrのTreeを表示します
"""

# 変数
comm = "public"
hostname = "192.168.10.253"

# cmdgen を importする
# pip install pysnmpが必要
# pip install pysnmp-mibs

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.smi import builder, view, error
import sys

# IF-MIB::ifDescr
targetmib = ".1.3.6.1.2.1.2.2.1.2"

# ターゲットのMIB Treeをtupleにする。
# ".1.3.6.1.2.1.2.2.1.2" -> [1, 3, 6, 1, 2, 1, 2, 2, 1, 2]
# [1:]は最初の".1.3.6"の最初のフィールド(".")を消す
# 結果は文字列で返ってくるのでintにする
mibtuple = targetmib.split(".")[1:]
mibtuple = [int(x) for x in mibtuple]


# 操作用クラスの生成
cmdGen = cmdgen.CommandGenerator()

comm_data = cmdgen.CommunityData(comm, comm)
transport = cmdgen.UdpTransportTarget((hostname, int(161)))
errorIndication, errorStatus, errorIndex, \
                 result = cmdgen.CommandGenerator().nextCmd(comm_data, transport, mibtuple)

# errorIndication: None = 異常なし
if errorIndication:
    print errorIndication
    sys.exit(1)

# errorStatus: 0 = 正常
if errorStatus:
    print '%s at %s\n' % (
        errorStatus.prettyPrint(),
        errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
        )
    sys.exit(1)

# resultには結果が入っている
# 例: print result[0]
# [(ObjectName(1.3.6.1.2.1.2.2.1.2.1), OctetString('10GigabitEthernet1/1'))]

# 出力を表示
for varBindTableRow in result:
    for name, val in varBindTableRow:
        print '%s = %s' % (name.prettyPrint(), val.prettyPrint())



"""

path_to_mib_dir = "/usr/share/mibs/ietf/SNMPv2-SMI"
mibBuilder = builder.MibBuilder()
mibPath = mibBuilder.getMibPath() + ( path_to_mib_dir, )
mibBuilder.setMibPath( *mibPath )
mibBuilder.loadModules( 
    builder.ZipMibSource('SNMPv2-SMI'),
    )
"""

mibBuilder = builder.MibBuilder() 
mibPath = mibBuilder.getMibSources() + (builder.DirMibSource('/usr/share/mibs/'),)
mibBuilder.setMibSources(*mibPath)
mibBuilder.loadModules('SNMPv2-MIB')
mibView = view.MibViewController(mibBuilder)
