from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("850x1000")

def resize_image(img, target_width, target_height):
    width, height = img.size
    aspect_ratio = width / height
    
    if width > target_width or height > target_height:
        if width / target_width > height / target_height:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            new_height = target_height
            new_width = int(target_height * aspect_ratio)
        return img.resize((new_width, new_height), Image.ANTIALIAS)
    else:
        return img

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("Untitled design (2).gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("transformer-hi-tech-audio-logo-digital-reveal-intro-122757.mp3")
    mixer.music.play()
    
    for img_frame in ImageSequence.Iterator(img):
        # Resize the frame to maintain aspect ratio and fit the window
        img_frame = resize_image(img_frame, 1000, 1000)
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        lbl.image = img_frame  # Keep a reference to prevent garbage collection
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()
