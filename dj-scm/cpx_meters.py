import time
from adafruit_circuitplayground.express import cpx
import simpleio

cpx.pixels.brightness = 0.2
cpx.pixels.auto_write = False
min_temp = 24
max_temp = 30
while True:
    # Temp meter
    if cpx.switch:
        temp = cpx.temperature
        # Map the temperature to a value between 0 and 10...
        # the number of LEDs.
        peak = simpleio.map_range(temp, min_temp, max_temp, 0, 10)
        for i in range(0,10):
            if i <= peak:
                cpx.pixels[i] = (50,0,0)
            else:
                cpx.pixels[i] = (0,0,20)
        cpx.pixels.show()
        continue
    # Motion meter
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
        cpx.pixels.show()
    time.sleep(0.1)