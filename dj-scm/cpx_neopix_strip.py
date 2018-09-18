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
pix_strip_a1 = neopixel.NeoPixel(board.D6,numpix,brightness=0.3,auto_write=False)
pix_strip_a2 = neopixel.NeoPixel(board.D9,numpix,brightness=0.3,auto_write=False)

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

write_colors_to_strip(init_colors,pix_strip_a1)
write_colors_to_strip(init_colors,pix_strip_a2)
del init_colors
prior_pix1 = pix_strip_a1[-1]
prior_pix2 = pix_strip_a2[-1]
idx = 0;
idxs = range(numpix)
is_blinking = True
while True:
    #(acc_x,acc_y,acc_z) = cpx.acceleration
    #print((acc_x,acc_y,acc_z))
#    print(gc.mem_free())
    gc.collect()
    time.sleep(0.01)
    if is_blinking:
        for idx in idxs:
            curr_pix1 = pix_strip_a1[idx]
            pix_strip_a1[idx] = prior_pix1
            prior_pix1 = curr_pix1
            curr_pix2 = pix_strip_a2[idx]
            pix_strip_a2[idx] = prior_pix2
            prior_pix2 = curr_pix2
            idx += 1
            if idx % numpix:
                idx = 0
        pix_strip_a1.show()
        pix_strip_a2.show()
    