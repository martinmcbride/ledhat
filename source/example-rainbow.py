#####
# Author:  Martin McBride
# Created: 2016-09-10
# Copyright (C) 2016, Martin McBride
#
# License: MIT
#####

#
# Move the red dot along the row, and down each column.
#

WIDTH = 16
HEIGHT = 16

import ledhat

rainbow = (
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 0, 255),
    (128, 0, 255)
)

def draw(hat, frame):
    hat.clear_pixels()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            n = (x + y + frame) // 2 % 8
            hat.set_pixel(x, y, rainbow[n])

hat = ledhat.LEDHat(draw, WIDTH, HEIGHT, led_size=30)
