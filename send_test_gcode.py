#!/usr/bin/env python3
from gpiozero import Button, LED
import subprocess

print("Start sending Gcode")

led1 = LED(27)
led2 = LED(17)

fileHandler = open('test_output.txt', "r")

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
#proc = subprocess.Popen(strz, shell=True, stdout=subprocess.PIPE)
#print(proc.communicate())
led1.off()
led2.on()
