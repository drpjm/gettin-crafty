import board
import digitalio
import time
import busio
import adafruit_lis3dh
import neopixel
from math import fabs, sqrt, floor

i2c_iface = busio.I2C(board.SCL, board.SDA)
ax_int = digitalio.DigitalInOut(board.D1)
lis3dh_iface = adafruit_lis3dh.LIS3DH_I2C(i2c_iface, int1=ax_int)
lis3dh_iface.range = adafruit_lis3dh.RANGE_2_G
G_TO_INT8_FACTOR = 255.0/2.0

pix1_pin = board.A3
pix2_pin = board.A4
pix1 = neopixel.NeoPixel(pix1_pin, 30, brightness=0.3,auto_write=False)
pix2 = neopixel.NeoPixel(pix2_pin, 30, brightness=0.3,auto_write=False)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
colors = [RED, GREEN, BLUE]

idx = 0

# Takes x and y accelerations and returns the led brightness
def compute_brightness(x,y,max_bright):
    val = sqrt(x*x + y*y)
    if val > max_bright:
        return max_bright
    else:
        return val

while True:
    x, y, z = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh_iface.acceleration]
    #print((x,y,z))
    x_color = floor(fabs(x) * G_TO_INT8_FACTOR)
    y_color = floor(fabs(y) * G_TO_INT8_FACTOR)
    time.sleep(0.05)
    pix1.fill((y_color,0,x_color))
    pix1.brightness = compute_brightness(x,y,0.5)
    pix1.show()