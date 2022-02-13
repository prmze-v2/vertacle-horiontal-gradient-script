import os
from os import path, sys, system
from time import sleep

if sys.argv[1] == "verticle":

    def horizontal_gradient(rgb_code, text):
        print(rgb_code + text, end='', flush=True)

    with open(sys.argv[2], 'r') as f:
        startrgb = 0,255,255
        endrgb = 255,255,0
        r = int(startrgb[0]) #initial red value
        g = int(startrgb[1]) #initial green value
        b = int(startrgb[2]) #initial blue value
        for x in f.readlines():
            changer = int((int(endrgb[0]) - int(startrgb[0]))/len(x))
            changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(x))
            changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(x))
            rgb_code = f"\x1b[40;38;2;{r};{g};{b}m"
            r+=changer  
            g+=changeg 
            b+=changeb
            horizontal_gradient(rgb_code, x)


elif sys.argv[1] == "horizontal":
    def gradient(startrgb,endrgb,text):
        #calculates the amount to change red, green, and blue values each character
        changer = int((int(endrgb[0]) - int(startrgb[0]))/len(text))
        changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(text))
        changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(text))

        r = int(startrgb[0]) #initial red value
        g = int(startrgb[1]) #initial green value
        b = int(startrgb[2]) #initial blue value

        for letter in text:
            if letter == '\n':pass
            print(f"\x1b[40;38;2;{r};{g};{b}m{letter}",end="")
            r+=changer 
            g+=changeg 
            b+=changeb
    with open(sys.argv[2], 'r') as f:
        for x in f.readlines():
            startrgb = 0,255,255
            endrgb = 255,255,0
            gradient(startrgb, endrgb, x)