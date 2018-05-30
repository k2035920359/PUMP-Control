# -*- coding: utf-8 -*-
import wiringpi

PWM_PIN = 19
DUTY = 0

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(PWM_PIN, wiringpi.GPIO.PWM_OUTPUT)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(375)

try:
	while True:
		for DUTY in range(0, 1025, 1):
			wiringpi.pwmWrite(PWM_PIN, DUTY)
			wiringpi.delay(10)
			print(DUTY)
		for DUTY in range(1024, 1, -1):
			wiringpi.pwmWrite(PWM_PIN, DUTY)
			wiringpi.delay(10)
			print(DUTY)

except KeyboardInterrupt:
    pass
wiringpi.pwmWrite(PWM_PIN, 0)
