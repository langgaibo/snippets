from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

def fireworks():
    x = [255, 128, 0]
    y = [randint(128,255) for i in range(3)]
    e = [0, 0, 0]
    
    xplod1 = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,x,e,e,e
            ]
    
    xplod2 = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,x,e,e,e,
            e,e,e,e,e,e,e,e
            ]
    
    xplod3 = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,x,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
    
    xplod4 = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,x,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
    
    xplod5 = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
    
    xplod6 = [
            e,e,e,e,y,e,e,e,
            y,y,e,e,y,e,y,e,
            e,y,y,e,y,y,e,e,
            e,y,y,y,y,y,y,e,
            e,y,e,y,y,y,y,y,
            e,e,y,e,y,y,e,e,
            e,y,e,e,e,e,e,e,
            e,e,e,y,e,e,e,e
            ]

    sense.set_pixels(xplod1)
    time.sleep(0.15)
    sense.set_pixels(xplod2)
    time.sleep(0.15)
    sense.set_pixels(xplod3)
    time.sleep(0.15)
    sense.set_pixels(xplod4)
    time.sleep(0.15)
    sense.set_pixels(xplod5)
    time.sleep(0.4)
    sense.clear(255,255,255)
    time.sleep(0.05)
    sense.set_pixels(xplod6)
    time.sleep(0.75)

# Warning flash
for i in range(50):
    sense.clear(255,255,255)
    time.sleep(0.05)
    sense.clear()
    time.sleep(0.05)

# Message
sense.show_message("10..9..8..7..6..5..4..3..2..1..", scroll_speed=0.08, text_colour=[204,0,0])
sense.show_message("HAPPY NEW YEAR!", scroll_speed=0.04, text_colour=[204,0,204])
sense.show_letter("2")
time.sleep(0.25)
sense.show_letter("0")
time.sleep(0.25)
sense.show_letter("1")
time.sleep(0.25)
sense.show_letter("6")
time.sleep(0.25)

# Bombs Away
for i in range(7):
    fireworks()
    sense.clear()

