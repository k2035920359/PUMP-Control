# -*- coding: utf-8 -*-
import wiringpi

PWM_PIN = 19#12,13,18,19から選べる
DUTY = 0

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(PWM_PIN, wiringpi.GPIO.PWM_OUTPUT)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(375)

try:
	while True:
		print("ON")
		wiringpi.pwmWrite(PWM_PIN, 500)
		wiringpi.delay(3000)
		print("OFF")
		wiringpi.pwmWrite(PWM_PIN, 0)
		wiringpi.delay(3000)

except KeyboardInterrupt:
    pass
wiringpi.pwmWrite(PWM_PIN, 0)
