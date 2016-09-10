#####
# Author:  Martin McBride
# Created: 2016-09-09
# Copyright (C) 2016, Martin McBride
#
# License: MIT
#####

#
# Move the red dot along the row, and down each column.
#

WIDTH = 8
HEIGHT = 4

import ledhat


def draw(hat, frame):
    hat.clear_pixels()
    y = (frame // WIDTH) % HEIGHT
    x = frame % WIDTH
    hat.set_pixel(x, y, (255, 0, 0))


hat = ledhat.LEDHat(draw, WIDTH, HEIGHT)
