#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

# command args
# [1] pin number (GPIOn)
# [2] 周期 [ms]
# [3] パルス幅[ms]
# >python3 pi_servo.py 18 20 2

import sys
import wiringpi

args = sys.argv
argc = len( args )

if argc != 4 :
        print("error : invalid arguments")
        print("ex.) python3 pi_servo.py 18 20 2")
        quit()

pwm_pin = int( args[1] )
interval = float( args[2] )
pulse = float( args[3] )

"""
PWMは、以下の式で成り立つ

[PWM周波数] = 19.2MHz / [Clock] / [Range]
[Duty比] = [Duty] / [Range]

wiringpiでは、[Range] = 1024で固定し、[Clock]と[Duty]
の2つのパラメータでPWMを制御する

[Range] = 1024
[PWM周波数] = 18750 / [Clock]
[Duty比] = [Duty] / 1024
"""

range = 1024
duty_ratio = pulse / interval
hz = 1 / ( interval * 0.001 )
clock = int( 18750 / hz )
duty = int( duty_ratio * range )

print("pin = ", pwm_pin, " interval[ms] = ", interval, " pulse[ms] = ", pulse )
print("clock = ", clock, " duty=", duty, " duty_ratio=", duty_ratio )

# 初期設定
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( pwm_pin, wiringpi.GPIO.PWM_OUTPUT )
wiringpi.pwmSetMode( wiringpi.GPIO.PWM_MODE_MS )

# ClockとDutyを設定してPWMを生成する
wiringpi.pwmSetClock( clock )
wiringpi.pwmWrite( pwm_pin, duty )
