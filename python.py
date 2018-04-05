import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

while True:
    GPIO.output(23, True)
    GPIO.output(23, False)