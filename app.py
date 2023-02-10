import tkinter as tk
import math
from tkinter import filedialog as fd
from PIL import Image, ImageTk
width = 1600
height = 900

# Create main window
root = tk.Tk()
root.geometry(f"{width}x{height}")
root.title("Sprite Sheet Cutter")


# Open_Image Function
def Open_Image():
  file_path = fd.askopenfilename()
  image = Image.open(file_path)
  image=set_image_size(height/2, image)
  image_display.config(image=image)
  root.reload()

def set_image_size(height_, image):
    multiplier = math.ceil((height_)/image.height)
    image=image.resize((image.width*multiplier, image.height*multiplier), Image.NEAREST)
    image=ImageTk.PhotoImage(image)
    return image

# Place widgets
# Open Image
tk.Button(root, text="Load Image", font=('Arial', 20),
          command=Open_Image).grid(row=0, column=0)

# X Tile and Y Tile entries
tk.Label(root, text="X tile size: ", font=('Arial', 20)).grid(row=1, column=0)
tk.Label(root, text="Y tile size: ", font=('Arial', 20)).grid(row=2, column=0)
tk.Entry(root, font=('Arial', 20), width=4).grid(row=1, column=1)
tk.Entry(root, font=('Arial', 20), width=4).grid(row=2, column=1)

# Canvas to show the image
image_display = tk.Label(root)
image_display.grid(row=3, column=3)
# Add a default image to the Label and size it up 
image = Image.open("empty pattern.png")
image = set_image_size(height/2, image)
image_display.config(image=image)

# Run the window mainloop
root.mainloop()
