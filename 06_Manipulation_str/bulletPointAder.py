#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import sys

import pyperclip

string = pyperclip.paste()
if string == None:
    print("you must copy first and then run the code.")
    sys.exit()

string = string.split("\n")

for i in range(len(string)):
    string[i] = "* " + string[i]


pyperclip.copy("\n".join(string))
