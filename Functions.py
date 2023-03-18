import math
import os
import glob
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
        multiplier = math.ceil(target / width)
    else:
        # Multiplier to multiply Height to get to Target
        multiplier = math.ceil(target / height)
    # Resize Image
    image = image.resize((width * multiplier, height * multiplier), Image.NEAREST)
    # Convert it to Bytes
    with BytesIO() as output:
        image.save(output, format="PNG")
        data = output.getvalue()
    # Return it

    return [data, multiplier, image.width, image.height]


def Display_Image(image_data, height, graph):
    graph.erase()
    graph.DrawImage(data=image_data, location=(0, 480))


def Show_Cuts(xtile, ytile, multiplier, targetx, targety, graph, xoff=0, yoff=0, cutx=0, cuty=0):
    boxes = []
    for i in range(math.floor(targety / ((ytile + yoff) * multiplier))):
        y = (i + 1) * (ytile + yoff) * multiplier
        for j in range(math.floor(targetx / ((xtile + xoff) * multiplier))):
            x = (j + 1) * (xtile + xoff) * multiplier
            id = graph.DrawRectangle((x - (xtile * multiplier), y - (ytile * multiplier)), (x, y), line_color="Red")
            graph.move_figure(id, xoff, yoff)
            graph.move_figure(id, cutx, cuty)
            boxes.append(id)
    return [boxes, [cutx, cuty]]


def Cut_Image(data, boxes_data, location, graph):
    image = Image.open(BytesIO(data))
    for i, box in enumerate(boxes_data[0]):
        ((left, top), (right, bottom)) = graph.get_bounding_box(box)
        im = image.crop((left + 1 - boxes_data[1][0], bottom + 1 - boxes_data[1][1], right - 1 - boxes_data[1][0],
                         top - 1 - boxes_data[1][1]))
        im.save(f"{location}/box__{i}.png")


def Delete_File(file_loc):
    os.remove(file_loc)


def Fast_scan(image_folder):
    # Get the images
    images = [x for x in os.listdir(image_folder) if x.endswith(".png")]
    x_c, y_c = 0, 0

    # loop through every image
    for i, image_ in enumerate(images):

       # Open the image
        image_loc = f"{image_folder}\\{image_}"
        image = Image.open(image_loc)

        print(image.width, image.height)
        # Set the x change and y change depending on image height & withs
        if image.width > image.height:
            x_c = math.floor(image.width/image.height)
            y_c = 1
            # print(image_, x_c, y_c)
        elif image.width < image.height:
            x_c = 1
            y_c = math.floor(image.height/image.width)
            # print(image_, x_c, y_c)
        elif image.width == image.height:
            x_c = 1
            y_c = 1

        # Check every pixel
        x, y = 0, 0
        while image.getpixel((x, y))[3] == 0:
            if x+x_c != image.width and y+y_c != image.height:
                # print(x, y)
                x += x_c
                y += y_c
            else:
                break
        else:
            continue
        Delete_File(image_loc)


# TODO: 2 Functions to find fully transparent images and delete them. - DONE
# TODO: FAST FUNCTION: get top left, bottom right - DONE
#   and go through DIAGONALLY to see if pixels are all transparent and deletes the image, else it stops the check and
#   keeps the image.

# TODO: SLOW FUNCTION: get top left, bottom right
#   and go through SNAKE LIKE to see if pixels are all transparent and deletes the image, else it stops the check and
#   keeps the image.
