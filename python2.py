import wiringpi2

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(23,io.OUTPUT)

while True:
    io.digitalWrite(23,io.HIGH)
    io.digitalWrite(23,io.LOW)