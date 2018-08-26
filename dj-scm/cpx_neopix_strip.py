import time
import board
import neopixel
from adafruit_circuitplayground.express import cpx
import gc

BLK = (0,0,0)
rgb_array = [(50,0,0),(50,20,0),(50,50,0),
            (0,50,0),(0,50,20),(0,50,50),
            (0,0,50),(20,0,50),(50,0,50)]

#acc_x_history = []
#acc_y_history = []
#acc_z_history = []

numpix = 30
pix_strip = neopixel.NeoPixel(board.D6,numpix,brightness=0.3,auto_write=False)

#print("free="+str(gc.mem_free()))
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
    i = 0
    for c in colors:
        pixels[i] = c
        i = i+1
    pixels.show()

init_colors = init_color_array(numpix)

write_colors_to_strip(init_colors,pix_strip)
del init_colors
prior_pix = pix_strip[-1]
idx = 0;
idxs = range(numpix)
is_blinking = False
while True:
    #(acc_x,acc_y,acc_z) = cpx.acceleration
    #print((acc_x,acc_y,acc_z))
    #print(gc.mem_free())
    gc.collect()
    time.sleep(1)
    if is_blinking:
        for idx in idxs:
            curr_pix = pix_strip[idx]
            pix_strip[idx] = prior_pix
            prior_pix = curr_pix
            idx += 1
            if idx % numpix:
                idx = 0
        pix_strip.show()
    