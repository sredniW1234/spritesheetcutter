import tkinter as tk
import math
from tkinter import filedialog as fd
from PIL import Image, ImageTk


width = 1600
height = 900
# Required so that no error is thrown when setting displayed_image

# Create main window
root = tk.Tk()
root.geometry(f"{width}x{height}")
root.title("Sprite Sheet Cutter")


# Open_Image Function
def Open_Image():
  # Delete previous image
  image_display.delete(displayed_image)
  displayed_image = None
  # Open new image
  file_path = fd.askopenfilename()
  image = Image.open(file_path)
  # Resize image
  image = set_image_size(height/2, image)
  # Put the image on the canvas
  displayed_image = image_display.create_image(image.width(), image.height(), anchor=tk.SE, image=image)
  # Update the canvas
  root.reload()
  print("loaded Image")


# set image width and height to a specific height size while still keeping the aspect ratio
def set_image_size(height_, image):
    if height_ <= height:
        height_ = height_
    elif height >= height:
        height_ = height
    multiplier = math.ceil((height_)/image.height)
    print(multiplier, image.width, image.width*multiplier)
    print(multiplier, image.height, image.height*multiplier, height_/image.height)
    image = image.resize((image.width*multiplier, image.height*multiplier), Image.Resampling.NEAREST)
    image = ImageTk.PhotoImage(image)
    print(image.width(), image.height())
    return image


# Show Cuts
def show_cuts():
    cuts = tk.Canvas(root, width=width/2, height=height/2)
    cuts.grid(row=4, column=3)
    x_t = int(X_tile_size.get())
    y_t = int(Y_tile_size.get())
    # cuts.config(bg='') # Makes Canvas Background transparent so that you can see through it when overlayed on image
    y=0
    for i in range(int(height/2)):
        x = 0
        for j in range(int(width/2)):
            cuts.create_rectangle(x, y, x+x_t, y+y_t)
            x+=x_t
        y+=y_t



# Place widgets
# Open Image
tk.Button(root, text="Load Image", font=('Arial', 20),
          command=Open_Image).grid(row=0, column=0)


# X Tile and Y Tile entries
tk.Label(root, text="X tile size: ", font=('Arial', 18)).grid(row=1, column=0)
tk.Label(root, text="Y tile size: ", font=('Arial', 18)).grid(row=2, column=0)
X_tile_size = tk.Entry(root, font=('Arial', 18), width=4)
X_tile_size.grid(row=1, column=1)
Y_tile_size = tk.Entry(root, font=('Arial', 18), width=4)
Y_tile_size.grid(row=2, column=1)


#add button to show cuts
tk.Button(root, text="Show Cuts", font=("Arial", 15), command=show_cuts).grid(row=3, column=0)


# Canvas to show the image
image_display = tk.Canvas(root, width=width/2, height=height/2)
image_display.grid(row=4, column=3) # USED FOR DISPLAYING IMAGE


# Add a default image to the Label and size it up 
image = Image.open("empty pattern.png")
image = set_image_size(height/2, image)
displayed_image = image_display.create_image(image.width(), image.height(), anchor=tk.SE, image=image)


# Run the window mainloop
root.mainloop()
