""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

# Using pathlib and OS to create directories and add files
from pathlib import Path
import os
print(Path.cwd())

os.chdir('C:/github')

print(Path.cwd())

os.makedirs('C:/github/test')

os.chdir('C:/github/test')

print(Path.cwd())

p = Path('spam.txt')

p.write_text("what's up")

p.read_text()


# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
   message= "Hello "+ entry.get()
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   entry.delete(0, 'end')
   label.pack(pady=30)

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Name...")
entry.pack()
#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()

entry1 = ttk.Entry(frame, width= 40)
entry1.insert(INSERT, "Enter Your Name...")
entry1.pack()

entry2 = ttk.Entry(frame, width= 40)
entry2.insert(INSERT, "Enter Your Name...")
entry2.pack()

