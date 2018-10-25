import time
import board
import neopixel
from analogio import AnalogIn
from simpleio import map_range
import gc

BLK = (0,0,0)
rainbow = [(50,0,0),(50,20,0),(50,50,0),
            (0,50,0),(0,50,20),(0,50,50),
            (0,0,50),(20,0,50),(50,0,50)]

numpix = 30

pix_strip_a1 = neopixel.NeoPixel(board.D6,numpix,brightness=0.1,auto_write=False)
pix_strip_a6 = neopixel.NeoPixel(board.D0,numpix,brightness=0.1,auto_write=False)

def init_every_other(npix):
    i = 0
    colors = [BLK for i in range(npix)]
    for c in reversed(rainbow):
        colors[i] = c
        i += 2
    return {'color_arr':colors, 'final_idx':i-2}
    
#print(init_every_other(30))
    
def write_colors_to_strip(colors,pixels):
    i = 0
    for c in colors:
        pixels[i] = c
        i = i+1
    pixels.show()

res = init_every_other(30)
head_idx = res['final_idx']
write_colors_to_strip(res['color_arr'],pix_strip_a1)
write_colors_to_strip(res['color_arr'],pix_strip_a6)

is_blinking = True

light_in = AnalogIn(board.LIGHT)
while True:
#    print(gc.mem_free())
    gc.collect()
#    light_val = light_in.value
#    print(light_val)
    time.sleep(0.08)
    if is_blinking:
        t0 = time.monotonic()
        
        idx = head_idx
        for c in rainbow:
            pix_strip_a1[idx] = c
            pix_strip_a6[idx] = c
            idx -= 2
        pix_strip_a1.show()
        pix_strip_a6.show()
        t1 = time.monotonic()
        
        head_idx +=2
        if head_idx % 30 == 0:
            head_idx = 0
        #print("Time = {0}".format(t1-t0))
    