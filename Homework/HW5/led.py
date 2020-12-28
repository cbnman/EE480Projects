#!/usr/bin/python3
import sys
from time import sleep
LED_Path = "/sys/class/gpio/gpio17/"
sysfs_dir = "/sys/class/gpio/"
LED_number = "17"

def writeLED( filename, value, path = LED_Path ):
	fo = open( path + filename, "w")
	fo.write(value)
	fo.close()
	return
	
#This section sets up the GPIO Pin for the program
writeLED(filename = "export", value = LED_number, path = sysfs_dir)
sleep(0.1)
writeLED(filename = "direction", value = "out")

#This section blinks the LED at 0.5s intervals
for x in range(0,20):
	writeLED(filename = "value", value = "1")
	sleep(0.5)
	writeLED(filename = "value", value = "0")
	sleep(0.5)

#This section closes down the operation
writeLED(filename = "unexport", value = LED_number, path = sysfs_dir)
