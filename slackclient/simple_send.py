#!env python
# -*- coding: utf-8 -*-

from slackclient import SlackClient
# pip install pit
from pit import Pit
# pip instal oauth2
import time
import os
import sys
import pickle
import datetime
import types
import sys, codecs
import re

# for stdout
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# for pit
if not "EDITOR" in os.environ:
  print("OS-EDITOR = NONE")
  sys.exit(1)
# tokenの取得
piConf = Pit.get("slackclient", {'require': {'tkn': 'token',}})


tkn = piConf['tkn']
print tkn
sc = SlackClient(tkn)


#print sc.api_call(
#    "chat.postMessage", channel="#bottest", text="Hi",
#    username='kanaibot', icon_emoji=':robot_face:'
#)
#sc.rtm_send_message("bottest", "hogehoge")




res = sc.api_call("rtm.start")
selfid = res["self"]["id"]

res = sc.rtm_connect()


if not res:
  print "err"
  sys.exit(1)

def do_recv_msg2self(d):
  if re.search(u".*しゃべって:.*", d["text"]) is not None:
    content = d["text"].split(u"て:")[1]
    print content
    sc.api_call("chat.postMessage", channel="#bottest", text=u"しゃべるよ:" + content, username="kanaibot", )
  else:
    sc.api_call("chat.postMessage", channel="#bottest", text=u"よんだ？", username="kanaibot", )

def do_recv_msg(d):
  if re.search(u"@" + selfid,  d["text"]) is not None:
    do_recv_msg2self(d)

def do_recv(d):
  print "recv"
  if "type" in d.keys():
    if d["type"] == "message":
      do_recv_msg(d)


while True:
  # listen開始
  dats =  sc.rtm_read()
  # 何もないと[]がかえってくる
  if len(dats) > 0:
    for dat in dats:
      do_recv(dat)
  time.sleep(1)

