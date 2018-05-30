# -*- Coding: utf-8 -*-
import subprocess
import wiringpi as w
import time

"""
w.pullUpDnControl(0, 2) # ポート0をプルアップ

w.pullUpDnControl(0, 1) # ポート0をプルダウン

w.pullUpDnControl(0, 0) # プルアップ／プルダウンの解除
"""

w.wiringPiSetup()
w.pinMode(4,0)
w.pullUpDnControl(4, 0) # プルアップ／プルダウンの解除
while 1:
  a = w.digitalRead(4)
  print(a)
  if ( a == 1 ):
    print("SWITCH ON")
  time.sleep(1)
