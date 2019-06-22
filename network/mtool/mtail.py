#!/usr/bin/python3.5

import signal
import os
import time

target = ["a.log"]

def trap_alarm(signum, frame):
  print('Signal handler called with signal', signum)
  # no-need set signal again
  signal.alarm(3)
  
signal.signal(signal.SIGALRM, trap_alarm)
signal.alarm(3)
time.sleep(10)

