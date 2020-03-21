from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

## hardware
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)



## Gui
win = Tk()
win.title("Led toggler")
myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold")


## Function
def ledToggle(ledPin):
    print(ledPin)
    if GPIO.input(ledPin) == 1:
        GPIO.output(ledPin,GPIO.LOW)
    else:
        GPIO.output(ledPin,GPIO.HIGH)


## WIDGETS
ledButton1 = Button(win, text = 'Red On', bg='red', font = myFont, command = lambda: ledToggle(14), height = 1, width = 25)
ledButton1.grid(row=0, column=1)
ledButton2 = Button(win, text = 'Yellow On', font = myFont, command = lambda: ledToggle(15), height = 1, width = 25)
ledButton2.grid(row=1, column=1)
ledButton3 = Button(win, text = 'Green On', font = myFont, command = lambda: ledToggle(18), height = 1, width = 25)
ledButton3.grid(row=2, column=1)

win.mainloop()
GPIO.cleanup()
