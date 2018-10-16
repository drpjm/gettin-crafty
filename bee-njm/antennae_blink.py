import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Initializing LEDs to have three of decreasing brightness.
numpix = 7
pix_strip1 = neopixel.NeoPixel(board.D1,numpix,brightness=0.2, auto_write=False)
pix_strip1[0] = (0,0,0)
pix_strip1[1] = (100,60,0)
pix_strip1[2] = (40,20,0)
pix_strip1[3] = (20,10,0)
pix_strip1.show()

pix_strip2 = neopixel.NeoPixel(board.D0,numpix,brightness=0.2, auto_write=False)
pix_strip2[0] = (0,0,0)
pix_strip2[1] = (100,60,0)
pix_strip2[2] = (40,20,0)
pix_strip2[3] = (20,10,0)
pix_strip2.show()

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################

i = 0
idxs = range(1,numpix)
prior_pix1 = pix_strip1[-1]
prior_pix2 = pix_strip2[-1]
# On indicator
dot[0] = (0,25,0)
dot.show()
while True:
    # Center neopixel displays rainbow
    wheel_val = wheel(i)
    pix_strip1[0] = tuple(wheel_val)
    pix_strip2[0] = tuple(wheel_val)
  
    # Chasing animation for the yellow lights on the antennae
    for idx in idxs:
        curr_pix1 = pix_strip1[idx]
        pix_strip1[idx] = prior_pix1
        prior_pix1 = curr_pix1
      
        curr_pix2 = pix_strip2[idx]
        pix_strip2[idx] = prior_pix2
        prior_pix2 = curr_pix2

    pix_strip1.show()
    pix_strip2.show()
    time.sleep(0.05)

    i = (i+1) % 256  # run from 0 to 255
  
  