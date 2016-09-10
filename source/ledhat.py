#####
# Author:  Martin McBride
# Created: 2016-09-09
# Copyright (C) 2016, Martin McBride
#
# License: MIT
#####

import tkinter

'''
Class represents a virtual LED hat which is displayed in a window and can be
animated using the draw() callback.
'''
class LEDHat:
    '''
    draw - a function which sets the color of each LED in the array. The function is called repeatedly to animate the
    LEDs
    width - the number of columns of LEDs
    height - the number of rows of LEDs
    delay - the delay between updates, in ms. A value of 100ms (0.1s) means that updates will occur 10 times a second
    led_size - radius of each LED in pixels. If you want a dispaly with a large number fo LEDS, you can reduce this
    value so that they all fit on the screen.
    '''
    def __init__(self, draw, width=8, height=8, delay=100, led_size=50):
        self.draw = draw
        self.width = width
        self.height = height
        self.delay = delay
        self.led_size = led_size

        self.frame = 0                # Frame counter, supplied to draw function for animation control

        # Pixel width of window
        self.px_width = self.width*self.led_size
        self.px_height = self.height*self.led_size

        # Create a 2D list of LED colors
        self.LEDs = [[(0, 0, 0) for i in range(self.width)] for j in range(self.height)]

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=self.px_width, height=self.px_height)
        self.canvas.pack()
        self.redraw()
        self.root.mainloop()

    def set_pixel(self, x, y, color):
        '''
        Set a pixel (an LED) color
        :param x: Column number of LED
        :param y: Row number of LED
        :param color: A triplet of values between 0 and 255 representing the R, G amd B values
        :return:
        '''
        self.LEDs[y][x] = color

    def clear_pixels(self, color=(0, 0, 0)):
        '''
        Clear all the LEDs (default to black)
        :param color: Optional color to set all LEDs to
        :return:
        '''
        self.LEDs = [[color for i in range(self.width)] for j in range(self.height)]

    def redraw(self):
        '''
        Private method implements redraw tick
        :return:
        '''
        self.draw(self, self.frame)
        self.frame += 1
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, self.px_width, self.px_height, fill="#222")
        for y in range(self.height):
            for x in range(self.width):
                color = '#{:02x}{:02x}{:02x}'.format(*self.LEDs[y][x])
                self.canvas.create_oval(x*self.led_size, y*self.led_size, (x+1)*self.led_size, (y+1)*self.led_size, fill=color)
        self.canvas.after(self.delay, self.redraw)
