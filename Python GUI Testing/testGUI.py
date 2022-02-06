from cProfile import label
from multiprocessing.connection import wait
import tkinter as tk

from matplotlib.pyplot import text

window = tk.Tk() #similar to the GUI constructor in Java (with exitonclose etc.)

#canvas = tk.Canvas(window, width=700, height=500, )
#canvas.pack()

def setUpGUI():
    canvas = tk.Canvas(window, width=100, height=100, bg="aqua",
    highlightcolor="yellow") # similar to conentPane in Java
    canvas.pack() # similar to contentPane.add(component)

    label1 = tk.Label(window, text="I'm in Frame A")
    label1.pack()


setUpGUI()

window.mainloop() #the event loop (listens for keypresses etc.)