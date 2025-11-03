from itertools import cycle
from PIL import Image , ImageTk
import time
import tkinter as tk
root = tk.Tk()
root.title("Image Slideshow")
image_paths = [
    r"/home/husnain/Pictures/Wallpapers/2.jpg",
    r"/home/husnain/Pictures/Wallpapers/2.jpg",
    r"/home/husnain/Pictures/Wallpapers/5.jpg",
    r"/home/husnain/Pictures/Wallpapers/6.jpg"
]

image_size = (1000, 600)


images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = cycle([ImageTk.PhotoImage(image) for image in images])

label = tk.Label(root)
label.pack()

def update_image():
    label.config(image=next(photo_images))   
    root.after(3000, update_image)           

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack(pady=30)

root.mainloop()
