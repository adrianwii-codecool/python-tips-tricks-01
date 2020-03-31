import time
import tkinter as tk
from tkinter import *

def tick(time1=''):
    time2 = time.strftime("%H:%M:%S")
    if time1 != time2:
        time1 = time2   
        clock.config(text=time2)
    clock.after(200, tick)

# create basic GUI window
window=Tk()
clock = Label(window, bg='green')
clock.pack()
tick()
mainloop()