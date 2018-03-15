import wiringpi
import time

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

io.pinMode(4,io.OUTPUT)

while True:
    io.digitalWrite(4,io.HIGH)
    io.digitalWrite(4,io.LOW)
