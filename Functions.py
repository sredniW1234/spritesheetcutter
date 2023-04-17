import math
import os
import glob
from io import BytesIO
from PIL import Image


# Resizes Image
def Resize(file_path, target, w, zoom):
    # Open Image
    image = Image.open(file_path)
    # Get Width and Height
    width, height = image.width, image.height
    if w:
        # Multiplier to multiply Width to get to Target
        multiplier = math.ceil((zoom / 100) * (target / width))
    else:
        # Multiplier to multiply Height to get to Target
        multiplier = math.ceil((zoom / 100) * (target / height))
    # Resize Image
    image = image.resize((width * multiplier, height * multiplier), Image.NEAREST)
    # Convert it to Bytes
    print(multiplier, width, height)
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


def Cut_Image(data, boxes_data, location, graph, naming):
    image = Image.open(BytesIO(data))
    for i, box in enumerate(boxes_data[0]):
        ((left, top), (right, bottom)) = graph.get_bounding_box(box)
        im = image.crop((left + 1 - boxes_data[1][0], bottom + 1 - boxes_data[1][1], right - 1 - boxes_data[1][0],
                         top - 1 - boxes_data[1][1]))
        im.save(f"{location}/{naming}{i}.png")

def Clear_Boxies(graph, boxies):
    if boxies != []:
        for i, id in enumerate(boxies[0]):
            graph.DeleteFigure(id)


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

def img_to_bytes(img_loc):
    image = Image.open(img_loc)
    with BytesIO() as output:
        image.save(output, format="PNG")
        data = output.getvalue()
    return data

def Dupe_remove(image):
    image_folder = image
    image_loc = image.split("/")
    image_folder = image_folder.replace(image_loc[-1], "")
    images = [x for x in os.listdir(image_folder) if x.endswith(".png")]
    c = 0
    for i, current_image in enumerate(images):
        if img_to_bytes(image_folder + current_image) == img_to_bytes(image):
            if image_folder + current_image == image:
                continue
            else:
                Delete_File(image_folder + current_image)

def Auto_Dupe_remove(image_folder, sg):
    image_folder = image_folder+"/"
    images = [x for x in os.listdir(image_folder) if x.endswith(".png")]
    del_images = []
    for i, current_image in enumerate(images):
        for i, dupe in enumerate(images):
            if image_folder + dupe in del_images or image_folder + current_image in del_images:
                continue
            if img_to_bytes(image_folder + dupe) == img_to_bytes(image_folder + current_image):
                if image_folder + dupe == image_folder + current_image:
                    continue
                else:
                    del_images.append(image_folder + dupe)
                    Delete_File(image_folder + dupe)
    sg.PopupOK("Done")


# TODO: 2 Functions to find fully transparent images and delete them. - 1/2 DONE
# TODO: FAST FUNCTION: get top left, bottom right - DONE
#   and go through DIAGONALLY to see if pixels are all transparent and deletes the image, else it stops the check and
#   keeps the image.

# TODO: SLOW FUNCTION: get top left, bottom right
#   and go through SNAKE LIKE to see if pixels are all transparent and deletes the image, else it stops the check and
#   keeps the image.
