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

i = 0

def draw(hat):
    global i
    hat.clear_pixels()
    row = (i//5)%5
    col = i%5
    hat.set_pixel(row, col, (255, 0, 0))
    i += 1


hat = ledhat.LEDHat(draw)
