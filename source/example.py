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

import ledhat

WIDTH = 8
HEIGHT = 4

def draw(hat, frame):
    hat.clear_pixels()
    x = frame % WIDTH
    y = (frame // WIDTH) % HEIGHT
    hat.set_pixel(x, y, (255, 0, 0))


ledhat.LEDHat(draw, WIDTH, HEIGHT)
