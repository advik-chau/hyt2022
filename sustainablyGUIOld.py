from tkinter import *
from turtle import onclick
#from cProfile import label
#from multiprocessing.connection import wait
#from turtle import bgcolor
#from matplotlib.pyplot import text

root = Tk() #similar to the GUI constructor in Java (with exitonclose etc.)

def TakeImage():
    lblTakingImage = Label(root, text="Opening picture...")
    lblTakingImage.grid(row=2, column=1)

lblSustainably = Label(root, text="Sustainably.")
lblTakeImage = Label(root, text="Press button to take image of bill.")
btnTakeImage = Button(root, text="take image", command=TakeImage)

lblSustainably.grid(row=0, column=0)
lblTakeImage.grid(row=1, column=0)
btnTakeImage.grid(row=1, column=1)

root.mainloop() #the event loop (listens for keypresses etc.)

#window.title("Sustainably")
#window.geometry('800x700')
#window.configure(background='#403e3b')
#window.configure(highlightcolor='yellow')
#window.resizable(False, False)

#canvas = tk.Canvas(window, width=700, height=500, )
#canvas.pack()

#def setUpGUI():
#    canvas = tk.Canvas(window, width=1000, height=1000, bg="grey",
#    highlightcolor="yellow") # similar to conentPane in Java
    #canvas.pack() # similar to contentPane.add(component)

#    lblSustainably = tk.Label(window, text="Sustainably.")
#    lblSustainably.grid(row=2, column=10)

    
    
    #lblSustainably.pack()


#setUpGUI()