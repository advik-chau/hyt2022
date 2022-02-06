import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Polygon
import time

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'visionAPIkey.json'

# API
client = vision.ImageAnnotatorClient()



width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()
def analyseImg(img):
    client = vision.ImageAnnotatorClient()
    # construct an iamge instance

    content = io.BytesIO()
    img.save(content, format='PNG')

    image = types.Image(content=content.getvalue())
    response = client.text_detection(image=image)  # returns TextAnnotation

    texts = response.text_annotations
    #print(full_text.bounding_poly.vertices)
    plt.figure(figsize=(12, 20))
    plt.imshow(Image.open(content))
    for text in texts:    
        vertices = [[vertex.x, vertex.y] for vertex in text.bounding_poly.vertices]
        vertices.append(vertices[0]) #repeat the first point to create a 'closed loop'

        xs, ys = zip(*vertices) #create lists of x and y values
        plt.plot(xs,ys) 
    pltContent = io.BytesIO()
    plt.savefig(pltContent, format='PNG')
    print(time.time())
    return pltContent # if you need...


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgPlot = Image.open(analyseImg(img))
    imgtk = ImageTk.PhotoImage(image=imgPlot)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(50, show_frame)

show_frame()
root.mainloop()