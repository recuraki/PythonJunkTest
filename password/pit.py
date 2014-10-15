#!/usr/local/bin/python

from pit import Pit
import os

if not "EDITOR" in os.environ:
  print("OS-EDITOR = NONE")
  sys.exit(1)

print(Pit.get('hoge',{'require': {'email':'your email','password':'your password'}}))

