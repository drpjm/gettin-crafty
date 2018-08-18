import time
import board
import simpleio
import neopixel
from adafruit_circuitplayground.express import cpx

rgb_array = [(50,0,0),(50,20,0),(50,50,0),
            (0,50,0),(0,50,20),(0,50,50),
            (0,0,50),(20,0,50),(50,0,50)]

acc_x_history = []
acc_y_history = []
acc_z_history = []

numpix = 30
pix_strip = neopixel.NeoPixel(board.D6,30,brightness=0.3,auto_write=False)

def init_pixels():
    init_colors = []
    color_idx = 0
    for i in range(0,30,2):
        if i % len(rgb_array) == 0:
            color_idx = 0
        else:
            color_idx = color_idx + 1
        curr_color = rgb_array[color_idx]
        pix_strip[i] = curr_color
        init_colors.append(curr_color)
        pix_strip[i+1] = curr_color
        init_colors.append(curr_color)
    pix_strip.show()
    return init_colors

init_color_arr = init_pixels()
#print(init_color_arr)

while True:
    (acc_x,acc_y,acc_z) = cpx.acceleration
    print((acc_x,acc_y,acc_z))
    time.sleep(0.5)