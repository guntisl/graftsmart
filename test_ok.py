#!/usr/bin/env pythoni
#from gpiozero import Button, LED
#import subprocess
import time
import serial


def waitok():
    ser = serial.Serial('/dev/ttyUSB0', 115200)

    endcount = 0
    bytecount = 0
    ok = False
    byte = ''
    o_byte = ('o')
    k_byte = ('k')

    while True:
        try:
#            print("Start listening for ok")
            byte = ser.read()
#            ser.close()
        except:
            print("no serial device")
        if byte[0] == 111:
            endcount = 1
        elif byte[0] == 107 and endcount == 1:
#            print("----------============got ok=============--------------")
            break
        else:
            endcount = 0

waitok()
