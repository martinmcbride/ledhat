#####
# Author:  Martin McBride
# Created: 2016-09-29
# Copyright (C) 2016, Martin McBride
#
# License: MIT
#####

#
# Animated game of life using Virtual LEDHat
#

import ledhat

SIZE = 10

a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def process_grid(a, b):
    'Copy a to b according to the rules'
    for row in range(1, SIZE-1):
        for col in range(1, SIZE-1):
            count = (a[row-1][col-1] +
                     a[row-1][col] +
                     a[row-1][col+1] +
                     a[row][col-1] +
                     a[row][col+1] +
                     a[row+1][col-1] +
                     a[row+1][col] +
                     a[row+1][col+1])
            if a[row][col]:
                if count < 2 or count > 3:
                    b[row][col] = 0
                else:
                    b[row][col] = 1
            else:
                if count == 3:
                    b[row][col] = 1
                else:
                    b[row][col] = 0


def draw(hat, frame):
    global a
    hat.clear_pixels()
    b = [[0]*SIZE for i in range(SIZE)]
    process_grid(a, b)
    a = b
    for x in range(SIZE):
        for y in range(SIZE):
            n = (x + y + frame) // 2 % 8
            hat.set_pixel(x, y, (255, 255, 255) if a[y][x] else (0, 0, 0))

ledhat.LEDHat(draw, SIZE, SIZE, led_size=30, delay=1000)
