""" This is the framework part of our interactive slide project. It will take a
    string input from the speech-to-text, process it and make a slide object.
"""

import view
from controller import strings, keystrokes  # names subject to change
import time
import sys

# loop continues checking for new strings until user keystrokes
while True:
    for text in strings.get()
#       the following section is for creating a new slide
        if 'title slide' in text:
            slide = view.Slide_Title()  # make new title slide
        elif 'list slide' in text:
            slide = view.Slide_List()  # make new list slide

#   TODO: think about the optimal way to do this. Like maybe a dictionary
#   instead of a bunch of if statements because eventually there will be a lot
#   of things here and it won't be very readable

        if 'the title of this slide is' in text:
            title = text.split('the title of this slide is', 1)[1]
            slide.title = title
        elif 'bullet' in text:
            bullet = text.split('bullet', 1)[1]
            slide.add_item(bullet)

    for key in keystrokes.get():
        if keystrokes.pop() == 'esc':
            sys.quit

    time.sleep(.01)  # allow the other threads to work
