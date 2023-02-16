import tkinter as tk, math
from tkinter import filedialog as fd
from PIL import Image, ImageTk

# Define Functions

# Change image_display image
def open_image():
    global image_item
    file_path = fd.askopenfilename()
    img = Image.open(file_path)
    img = resize(height/2, img)
    print(image_item)
    image_item = image_display.itemconfig(image_item, image=img)
    print(image_item)
    root.reload()

    
# Resize image
def resize(tall, image):
    if tall <= height:
        tall = tall
    else:
        tall = height
    if (tall % 2) == 0:
        multiplier = round((tall/image.height) * 2) / 2
    else:
        multiplier = int(math.ceil(tall/image.height))
    image = image.resize((int(image.width*multiplier), int(image.height * multiplier)), Image.Resampling.NEAREST)
    image = ImageTk.PhotoImage(image)
    return image


# Define width & height
width = 1600
height = 900

# Define Variables if needed
image_item = None

# Setup root window
root = tk.Tk()
root.geometry(f'{width}x{height}')


# Setup widget frame
widgets = tk.Frame(root).grid(row=0, column=0)

# Setup main widgets (load image button, cutting options, etc)
tk.Button(widgets, text = "Load Image", font=("Arial", 20), command=open_image).grid(row=0, column=0) # Load Image Widget

tk.Label(widgets, text = "X Tile Size: ", font=("Arial", 18)).grid(row=1, column=0) # X Tile Size Label 
tk.Label(widgets, text = "Y Tile Size: ", font=("Arial", 18)).grid(row=2, column=0) # Y Tile Size Label
x_tile = tk.Entry(widgets, width=4, font=("Arial", 18)).grid(row=1, column=1) # X Tile Size Entry
y_tile = tk.Entry(widgets, width=4, font=("Arial", 18)).grid(row=2, column=1) # Y Tile Size Entry

tk.Button(widgets, text = "Display Cuts", font=("Arial", 15)).grid(row=3) # Show Cuts Based On Previous Entries


# Setup image display and display temp image
image_display = tk.Canvas(root, width=width, height=height)
image_display.grid(row=4, column=2)
image = Image.open("empty pattern.png")
image = resize(height/2, image)
image_item = image_display.create_image(2, 2, anchor= tk.NW, image=image)
print(image_item)




# Run root mainloop
root.mainloop()