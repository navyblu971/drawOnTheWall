import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)


try:
	GPIO.setmode(GPIO.BCM)

	GPIO.cleanup() 

	MYPIN=14
	while True:
		GPIO.setup(MYPIN, GPIO.OUT)
		GPIO.output(MYPIN, GPIO.LOW)
		time.sleep(5)	
		GPIO.output(MYPIN, GPIO.HIGH)
		time.sleep(5)
except KeyboardInterrupt:
      GPIO.cleanup()


finally: GPIO.cleanup()

