import math
from io import BytesIO
from PIL import Image

# Resizes Image
def Resize(file_path, target, w):
    # Open Image
    image = Image.open(file_path)
    # Get Width and Height
    width, height = image.width, image.height
    if w:
        # Multiplier to multiply Width to get to Target
        multiplier = math.ceil(target/width)
    else:
        # Multiplier to multiply Height to get to Target
        multiplier = math.ceil(target/height)
    # Resize Image
    image = image.resize((width * multiplier, height * multiplier), Image.NEAREST)
    # Convert it to Bytes
    with BytesIO() as output:
        image.save(output, format="PNG")
        data = output.getvalue()
    # Return it
    print(image.width, image.height)
    return [data, multiplier, image.width, image.height]


def Display_Image(image_data, height, graph):
    graph.erase()
    graph.DrawImage(data=image_data, location=(0, height))


def Show_Cuts(xtile, ytile, multiplier, targetx, targety, graph, xoff = 0, yoff = 0):
    for i in range(int(targety/((ytile + yoff) * multiplier))):
        y = (i+1) * (ytile + yoff) * multiplier
        for j in range(int(targetx/((xtile + xoff) * multiplier))):
            x = (j+1) * (xtile + xoff) * multiplier
            graph.DrawRectangle((x-(xtile * multiplier),y-(ytile * multiplier)), (x,y), line_color="Red")