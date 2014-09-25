#!/usr/local/bin/python
# -*- coding: utf-8 -*-

bwlist = []
bwlist.append ( ("10M",  10 *1000 * 1000) )
bwlist.append ( ("100M", 100*1000 * 1000) )
bwlist.append ( ("1G",   1 * 1000 * 1000 * 1000) )
bwlist.append ( ("10G",  10* 1000 * 1000 * 1000) )
bwlist.append ( ("1G",   40* 1000 * 1000 * 1000) )
bwlist.append ( ("100G", 100*1000 * 1000 * 1000) )
bwlist.append ( ("400G", 400*1000 * 1000 * 1000) )
calc_bw = lambda stBW: filter(lambda x: x[0] == stBW, bwlist)[0][1]
calc_bwname_by_num = lambda stBW: filter(lambda x: x[1] == stBW, bwlist)[0][0]

print calc_bw("100M")

print calc_bwname_by_num(100000000)
