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


def Show_Cuts(xtile, ytile, multiplier, targetx, targety, graph, xoff = 0, yoff = 0, cutx = 0, cuty = 0):
    boxes = []
    for i in range(math.floor(targety/((ytile + yoff) * multiplier))):
        y = (i+1) * (ytile + yoff) * multiplier
        for j in range(math.floor(targetx/((xtile + xoff) * multiplier))):
            x = (j+1) * (xtile + xoff) * multiplier
            id = graph.DrawRectangle((x-(xtile * multiplier), y-(ytile * multiplier)), (x,y), line_color="Red")
            graph.move_figure(id, xoff, yoff)
            graph.move_figure(id, cutx, cuty)
            boxes.append(id)
    return boxes

def Cut_Image(data, boxes, graph):
    image = Image.open(BytesIO(data))
    for i, box in enumerate(boxes):
        top_left, bottom_right = graph.get_bounding_box(box)
        im = image.crop()

