#!/bin/sh

echo "23" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction

while true
do
	echo 1 > /sys/class/gpio/gpio23/value

	echo 0 > /sys/class/gpio/gpio23/value
done