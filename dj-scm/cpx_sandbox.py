import time
from adafruit_circuitplayground.express import cpx
import simpleio

cpx.pixels.brightness = 0.2
while True:
    if cpx.switch:
        print("Slide switch off.")
        cpx.pixels.fill((10,10,10))
        if cpx.button_a:
            cpx.play_tone(262,1)
        if cpx.button_b:
            cpx.play_tone(294,1)
        print("light level = ", cpx.light)
        continue
        
    else:
        R = 0
        G = 0
        B = 0
        x,y,z = cpx.acceleration
        print((int(x),int(y),int(z)))
        if x:
            R = R + abs(int(x))
        if y:
            G = G + abs(int(y))
        if z:
            B = B + abs(int(z))
        cpx.pixels.fill((R,G,B))
    time.sleep(0.1)