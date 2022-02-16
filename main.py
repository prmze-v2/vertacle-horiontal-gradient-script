import os
from os import path, sys, system
from time import sleep

with open('output.tfx', 'w') as f:
    f.write("")

if sys.argv[1] == "verticle":
    Banner = open(sys.argv[2], "r", encoding="utf8").read()
    output_lines = Banner.split("\n")
    startrgb = 0,255,255
    endrgb = 255,255,0
    r = int(startrgb[0]) #initial red value
    g = int(startrgb[1]) #initial green value
    b = int(startrgb[2]) #initial blue value
    for x in output_lines:
        changer = int((int(endrgb[0]) - int(startrgb[0]))/len(output_lines))
        changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(output_lines))
        changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(output_lines))
        rgb_code = f"\x1b[40;38;2;{r};{g};{b}m"
        r+=changer  
        g+=changeg 
        b+=changeb
        with open('output.tfx', 'a', encoding='utf8') as f:
            f.write(f"{rgb_code}{x}\n")


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
            with open('output.tfx', 'a', encoding='utf8') as f:
                f.write(f"\x1b[40;38;2;{r};{g};{b}m{letter}")
            r+=changer 
            g+=changeg 
            b+=changeb
    with open(sys.argv[2], 'r', encoding='utf8') as f:
        for x in f.readlines():
            startrgb = 0,255,255
            endrgb = 255,255,0
            gradient(startrgb, endrgb, x)
