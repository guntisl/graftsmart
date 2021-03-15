#!/usr/bin/env python3
from gpiozero import MotionSensor, LED
import numpy as np
import os
from subprocess import check_call
import cv2
from tkinter import *
import tkinter as tk
#import Image, ImageTk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import tkinter.ttk as ttk
import itertools
import shutil
import threading
import time


img_counter = 0
#tuple_1 = tuple(range(1, 25))
#brt = len(tuple_1)
#
#
#def progress_bar_func():
#    global num
#
#    num = 1
#    root.after(500, update_progress_bar)
#
#def update_progress_bar():
#    global num
#
#    if num <= brt:
#        percentage = round(num/brt*100)  # Calculate percentage.
#        print(num, percentage)
#        progressBar['value'] = num
#        style.configure('text.Horizontal.TProgressbar',
#                        text='{:g} %'.format(percentage))
#        num += 1
#        if num > brt:
#            print('Done')
#        else:
#            root.after(500, update_progress_bar)
#

cap = cv2.VideoCapture(1)
_, frame = cap.read()
frame = cv2.flip(frame, 1)



def on_click3():
    global img_counter
    img_counter = img_counter + 1
    img_name = "snaps/opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
#    print("{} written!".format(img_name))







def on_click1():
    blue_led.on()
    red_led.on()
    green_led.off()
    img_name = "snaps/image111.png"
    cv2.imwrite(img_name, frame)
    image_resized = "snaps/image111_resized.png"
    img = cv2.imread('/home/pi/darknet/snaps/image111.png', cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # rsize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(image_resized, resized)
    os.system("/home/pi/darknet/darknet detect custom-yolov4-tiny-detector.cfg custom-yolov4-tiny-detector_final.weights snaps/image111.png -dont-show -ext_output > first_output.txt ")
    print("detection is finished")
    os.system("python /home/pi/darknet/egg_lis.py")
    with open('first_output.txt', 'r') as f:
        print(f.read())
    with open('main_cutput.txt', 'r') as f:
        print(f.read())

def on_click2():
    blue_led.on()
    red_led.on()
    green_led.off()
    img_name = "snaps/image111.png"
    cv2.imwrite(img_name, frame)
    image_resized = "snaps/image111_resized.png"
    img = cv2.imread('/home/pi/darknet/snaps/image111.png', cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # rsize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(image_resized, resized)
    os.system("/home/pi/darknet/darknet detect custom-yolov4-tiny-detector.cfg custom-yolov4-tiny-detector_final.weights snaps/image111.png -dont-show -ext_output > first_output.txt ")
    print("detection is finished")
    os.system("python3 /home/pi/darknet/egg_lis.py")
    with open('first_output.txt', 'r') as f:
        print(f.read())
    with open('main_cutput.txt', 'r') as f:
        print(f.read())
    os.system("sudo python3 /home/pi/darknet/send_gcode.py")


def close_window():
        window.destroy()
#        check_call(['sudo', 'poweroff']) 

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Egg_PnP")
window.config(background="#FFFFFF")

red_led = LED(27)
green_led = LED(17)
blue_led = LED(23)
start_button = MotionSensor(21)
poweroff_button = MotionSensor(26)
detectButton = MotionSensor(22)
#Graphics window
imageFrame = tk.Frame(window, width=30, height=20)
imageFrame.grid(row=0, column=0, padx=1, pady=2)

controlFrame = tk.Frame(window, width=30, height=30)
controlFrame.grid(row=0, column=1, padx=1, pady=20)
#Capture video frames
#barFrame = tk.Frame(window, width=30, height=10)
#barFrame.grid(row=0, column=1, padx=10, pady=20)
#
#
#style = ttk.Style(barFrame)
#style.layout('text.Horizontal.TProgressbar',
#             [('Horizontal.Progressbar.trough',
#               {'children': [('Horizontal.Progressbar.pbar',
#                              {'side': 'left', 'sticky': 'ns'})],
#                'sticky': 'nswe'}),
#              ('Horizontal.Progressbar.label', {'sticky': ''})])
#              # , lightcolor=None, bordercolo=None, darkcolor=None
#style.configure('text.Horizontal.TProgressbar', text='0 %')
#
#progressBar = ttk.Progressbar(barFrame, style='text.Horizontal.TProgressbar', length=200,
#                              maximum=brt, value=0)
##progressBar.pack()
#
#progress_button = tk.Button(controlFrame, text="start", command=progress_bar_func)
##progress_button.pack()
#
#
#
#
#
#
#
#
#



def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    canvas = Canvas(controlFrame,width=100,height=100)
    #canvas.pack()
    pilImage = Image.open("predictions.jpg")
    instrImage = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(100,100,image=instrImage)






    display1.imgtk = imgtk #Shows frame for display 1
    display1.configure(image=imgtk)
    display2.imgtk = instrImage #Shows frame for display 2
    display2.configure(image=instrImage)
    window.after(10, show_frame) 


    
#instructions.grid(row=0, column=1) #Display 2
#Slider window (slider controls stage position)
#sliderFrame = tk.Frame(window, width=600, height=100)
#sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


display1 = tk.Label(imageFrame)
display1.grid(row=0, column=0, padx=2, pady=2)  #Display 1
display2 = tk.Label(controlFrame)
display2.grid(row=1, column=1, sticky=N) #Display 2

button = Button(imageFrame, text="Run Detection", command=on_click1, state='active')
button.grid(row=0, column=0, padx=2, pady=100, sticky=N+W)

pnpButton = Button(imageFrame, text="Detect & Place", command=on_click2, state='active')
pnpButton.grid(row=0, column=0, padx=2, pady=150, sticky=N+W)

closeButton = Button(imageFrame, text="Power Off", command=close_window, state='active')
closeButton.grid(row=0, column=0, padx=2, pady=200, sticky=N+W)
    
snapButton = Button(imageFrame, text="Capture Image", command=on_click3, state='active')
snapButton.grid(row=0, column=0, padx=2, pady=50, sticky=N+W)

    
#while True:
#if detectButton.when_motion and start_button.when_motion:
#    blue_led.on()
#    red_led.on()
#    green_led.off()
#    os.system("fswebcam -r 1280x720 --no-banner test/image11.jpg -d /dev/video1")
#    os.system("./darknet detect cfg/custom-yolov4-detector.cfg backup/custom-yolov4-detector_last.weights test/image11.jpg -ext_output > first_output.txt")
#        #lcd veic atpazīšanu
#elif poweroff_button.when_motion:
#    blue_led.on()
#    red_led.on()
#    green_led.off()
#    check_call(['sudo', 'poweroff']) 
#    window.destroy()
#else:
#    blue_led.off()
#    red_led.off()
#    green_led.on()





#instructions = tk.Label(instructionFrame)

show_frame() #Display
window.mainloop()  #Starts GUI

