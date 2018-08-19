import time
import board
import simpleio
import neopixel
from adafruit_circuitplayground.express import cpx

BLK = (0,0,0)
rgb_array = [(50,0,0),(50,20,0),(50,50,0),
            (0,50,0),(0,50,20),(0,50,50),
            (0,0,50),(20,0,50),(50,0,50)]

acc_x_history = []
acc_y_history = []
acc_z_history = []

numpix = 30
pix_strip = neopixel.NeoPixel(board.D6,30,brightness=0.3,auto_write=False)

def init_color_array(npix):
    colors = [BLK for i in range(npix)]
    color_idx = 0
    for i in range(0,npix,2):
        if i % len(rgb_array) == 0:
            color_idx = 0
        else:
            color_idx = color_idx + 1
        curr_color = rgb_array[color_idx]
        colors[i] = curr_color
        colors[i+1] = curr_color
    return colors
    
def write_colors_to_strip(colors,pixels):
    for i, c in enumerate(colors):
        pixels[i] = c
    pixels.show()

colors = init_color_array(numpix)
write_colors_to_strip(colors,pix_strip)

while True:
    (acc_x,acc_y,acc_z) = cpx.acceleration
    print((acc_x,acc_y,acc_z))
    time.sleep(0.5)
    #for i, pixel in enumerate(pix_strip):
    #    colors[i+1]=pixel
        