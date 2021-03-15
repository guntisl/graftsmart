#!/usr/bin/env python3
from gpiozero import Button, LED
import os
from subprocess import check_call

red_led = LED(27)
green_led = LED(17)
blue_led = LED(23)
detect_frame = Button(2)
start_button = Button(21)
poweroff_button = Button(26)


while True:
    if detect_frame.is_pressed and start_button.is_pressed:
        blue_led.on()
        red_led.on()
        green_led.off()
        os.system("fswebcam -r 1280x720 --no-banner test/image11.jpg -d /dev/video1")
        #lcd veic bildēšanu
        os.system("./run")
        #lcd veic atpazīšanu
        os.system("./darknet detect cfg/custom-yolov4-detector.cfg backup/custom-yolov4-detector_last.weights test/image11.jpg -ext_output > first_output.txt")
        #lcd veic atpazīšanu
    elif button2.is_pressed:
        led1.off()
        led2.off()
        check_call(['sudo', 'poweroff']) 
    elif button3.is_pressed:
        led1.off()
        led2.off()
        check_call(['sudo', 'poweroff']) 
    else:
        led1.off()
        led2.on()
        #print("Button is not pressed")





#Button(21).wait_for_press()

