#!/usr/bin/env python3
from gpiozero import Button, LED
import subprocess
import time
import serial



def waitok():
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    endcount = 0
    byte = 'ok\n'

    while True:
        try:
#            print("Start listening for ok")
            byte = ser.read()
 #           print(byte[0])
        except:
            print("no serial device")
        if (byte[0] == 111):
            endcount = 1
        elif byte[0] == 107 and endcount == 1:
            ser.close()
            break
        else:
            x = 1
led1 = LED(27)
led2 = LED(17)

fileHandler = open('main_cutput.txt', "r")

listOfLines = fileHandler.readlines()

fileHandler.close()
str2 = '"'
strl_echo = "echo " 
strl_port = " >> /dev/ttyUSB0"
strz = ("echo " + str2 + " >> /dev/ttyUSB0")
#print(strz)
for line in listOfLines:
    print(strl_echo + str2 + line.strip() + str2 + strl_port)
    subprocess.Popen(strl_echo + str2 + line.strip() + str2 + strl_port ,shell=True,stdout=subprocess.PIPE)
#    time.sleep(1)
    waitok()
#proc = subprocess.Popen(strz, shell=True, stdout=subprocess.PIPE)
#print(proc.communicate())
led1.off()
led2.on()
