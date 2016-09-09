#####
# Author:  Martin McBride
# Created: 2016-09-09
# Copyright (C) 2016, Martin McBride
#
# License: MIT
#####

import tkinter

LED_SIZE = 50

'''
Class represents a virtual LED hat which is displayed in a window and can be
animated using the draw() callback.
'''
class LEDHat:
    '''
    draw - a function which sets the color of each LED in the array. The function is called repeatedly to animate the
    LEDs
    rows - the number of rows of LEDs
    cols - the number of cols of LEDs
    delay - the delay between updates, in ms. A value of 100ms (0.1s) means that updates will occur 10 times a second
    '''
    def __init__(self, draw, rows=5, cols=5, delay=100):
        self.draw = draw
        self.rows = rows
        self.cols = cols
        self.delay = delay

        self.width = self.cols*LED_SIZE
        self.height = self.rows*LED_SIZE

        self.LEDs = [[(0, 0, 0) for i in range(self.rows)] for j in range(self.cols)]
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.redraw()
        self.root.mainloop()

    def set_pixel(self, row, col, color):
        '''
        Set a pixel (an LED) color
        :param row: Row number of LED
        :param col: Column number of LED
        :param color: A triplet of values between 0 and 255 representing the R, G amd B values
        :return:
        '''
        self.LEDs[col][row] = color

    def clear_pixels(self, color=(0, 0, 0)):
        '''
        Clear all the LEDs (default to black)
        :param color: Optional color to set all LEDs to
        :return:
        '''
        self.LEDs = [[color for i in range(self.rows)] for j in range(self.cols)]

    def redraw(self):
        '''
        Private method implements redraw tick
        :return:
        '''
        self.draw(self)
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="#222")
        for row in range(self.rows):
            for col in range(self.cols):
                color = '#{:02x}{:02x}{:02x}'.format(*self.LEDs[col][row])
                self.canvas.create_oval(col*LED_SIZE, row*LED_SIZE, (col+1)*LED_SIZE, (row+1)*LED_SIZE, fill=color)
        self.canvas.after(self.delay, self.redraw)
