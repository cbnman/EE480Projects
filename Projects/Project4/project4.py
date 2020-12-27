#!/usr/bin/python3
import wiringpi as wpi
from time import sleep

wpi.wiringPiSetupGpio()

#Sets all Pins
wpi.pinMode(22,1)

wpi.pinMode(27,1)

wpi.pinMode(17,1)

wpi.pinMode(24,1)

wpi.pinMode(23,1)

#Asks for User Input
print("Select an Option Below \n")
print("1. Sequential count in Binary \n")
print("2. Sweeping light movement from right to left \n")
print("3. Sweeping light movement from left to right \n")
print("4. Continuous sweeping light movemen \n")
print("5. User input Decimal to Binary translation \n")
uinput =  input("Enter your choice (1-5): ")

#Option 1
if uinput == "1":
    #This loop will count from 0 to 31 in binary with the LEDs
    for x in range(0, 32):
        #Each GPIO pin is mapped to a certain bit using the & (bitwise and) symbol and 0x00 (byte) notation
        wpi.digitalWrite(23,x & 0x01)
        wpi.digitalWrite(24,x & 0x02)
        wpi.digitalWrite(17,x & 0x04)
        wpi.digitalWrite(27,x & 0x08)
        wpi.digitalWrite(22,x & 0x10)
        sleep(1)
    wpi.digitalWrite(23,0)
    wpi.digitalWrite(24,0)
    wpi.digitalWrite(17,0)
    wpi.digitalWrite(27,0)
    wpi.digitalWrite(22,0)

elif uinput == "2":

    wpi.digitalWrite(23,1)
    sleep(2)
    wpi.digitalWrite(23,0)
    sleep(2)
    wpi.digitalWrite(24,1)
    sleep(2)
    wpi.digitalWrite(24,0)
    sleep(2)
    wpi.digitalWrite(17,1)
    sleep(2)
    wpi.digitalWrite(17,0)
    sleep(2)
    wpi.digitalWrite(27,1)
    sleep(2)
    wpi.digitalWrite(27,0)
    sleep(2)
    wpi.digitalWrite(22,1)
    sleep(2)
    wpi.digitalWrite(22,0)
    sleep(2)

elif uinput == "3":

    wpi.digitalWrite(22,1)
    sleep(2)
    wpi.digitalWrite(22,0)
    sleep(2)
    wpi.digitalWrite(27,1)
    sleep(2)
    wpi.digitalWrite(27,0)
    sleep(2)
    wpi.digitalWrite(17,1)
    sleep(2)
    wpi.digitalWrite(17,0)
    sleep(2)
    wpi.digitalWrite(24,1)
    sleep(2)
    wpi.digitalWrite(24,0)
    sleep(2)
    wpi.digitalWrite(23,1)
    sleep(2)
    wpi.digitalWrite(23,0)
    sleep(2)

elif uinput == "4":
    for x in range(1,10000000):
        #Sweep to the left
        wpi.digitalWrite(23,1)
        sleep(2)
        wpi.digitalWrite(23,0)
        sleep(2)
        wpi.digitalWrite(24,1)
        sleep(2)
        wpi.digitalWrite(24,0)
        sleep(2)
        wpi.digitalWrite(17,1)
        sleep(2)
        wpi.digitalWrite(17,0)
        sleep(2)
        wpi.digitalWrite(27,1)
        sleep(2)
        wpi.digitalWrite(27,0)
        sleep(2)
        wpi.digitalWrite(22,1)
        sleep(2)
        wpi.digitalWrite(22,0)
        sleep(2)
        #Sweep to the right
        wpi.digitalWrite(22,1)
        sleep(2)
        wpi.digitalWrite(22,0)
        sleep(2)
        wpi.digitalWrite(27,1)
        sleep(2)
        wpi.digitalWrite(27,0)
        sleep(2)
        wpi.digitalWrite(17,1)
        sleep(2)
        wpi.digitalWrite(17,0)
        sleep(2)
        wpi.digitalWrite(24,1)
        sleep(2)
        wpi.digitalWrite(24,0)
        sleep(2)
        wpi.digitalWrite(23,1)
        sleep(2)
        wpi.digitalWrite(23,0)
        sleep(2)

elif uinput == "5":
    #Asks the user for input
    number = int(input("Enter a decimal value between 0 and 31: "))
    #Checks to see if input is in the correct range
    if number >= 0 and number <= 31:
        #Each GPIO pin is mapped to a certain bit using the & symbol and 0x00 notation
        #The LEDs will then display the binary representation of the decimal number
        wpi.digitalWrite(23,number & 0x01)
        wpi.digitalWrite(24,number & 0x02)
        wpi.digitalWrite(17,number & 0x04)
        wpi.digitalWrite(27,number & 0x08)
        wpi.digitalWrite(22,number & 0x10)
        sleep(3)
        wpi.digitalWrite(23,0)
        wpi.digitalWrite(24,0)
        wpi.digitalWrite(17,0)
        wpi.digitalWrite(27,0)
        wpi.digitalWrite(22,0)
    else:
        #If the number is outside of the range, then the LEDs will blink 5 times
        for x in range(0,5):
            wpi.digitalWrite(23,1)
            wpi.digitalWrite(24,1)
            wpi.digitalWrite(17,1)
            wpi.digitalWrite(27,1)
            wpi.digitalWrite(22,1)
            sleep(2)
            wpi.digitalWrite(23,0)
            wpi.digitalWrite(24,0)
            wpi.digitalWrite(17,0)
            wpi.digitalWrite(27,0)
            wpi.digitalWrite(22,0)
            sleep(2)
else:
    print("Invalid Option")