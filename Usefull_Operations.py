from PIL import Image
import math


def resize_image(Image_file, target_size, woh = 1): # woh is width or height, 1 = width, 2 = height
    if woh == 1:
        image = Image.open(Image_file)
        width, height = image.width, image.height
        multiplier = target_size / width
        image = image.resize((int(width * multiplier), int(height * multiplier)), Image.NEAREST)
        image.save("Current_Image.png")
        return [height, multiplier, width, height]
    if woh == 2:
        image = Image.open(Image_file)
        width, height = image.width, image.height
        multiplier = target_size / height
        image = image.resize((int(width * multiplier), int(height * multiplier)), Image.NEAREST)
        image.save("Current_Image.png")
        return [0, multiplier, width, height]


def Draw_Image(loc, woh, graph):
    graph.Erase()
    h = resize_image(loc, 800, woh)
    graph.DrawImage(filename="Current_Image.png", location=(0, 800))
    return h


def Draw_Grid(width, height, multiplier, h_off, X_Tile, Y_Tile, graph, X_Off = 0, Y_Off = 0, Cuts_Off = 0):
    selections = []
    for i in range(math.ceil(height/Y_Tile+Y_Off)):
        y = math.ceil((i+1) * multiplier * Y_Tile)
        print(y)
        for j in range(int(width/X_Tile+X_Off)):
            x = math.floor((j+1) * X_Tile * multiplier)
            id = graph.DrawRectangle((0, 0), (x, y), line_color="#0f0f0f")
            if h_off != 0:
                graph.move_figure(id, 0, h_off+(400-h_off)-Cuts_Off)
            graph.move_figure(id, 0+X_Off, 0+Y_Off)
            selections.append([(0, 0), x, y+h_off+(400-h_off)-Cuts_Off+Y_Off])
    return selections

# h_off+(400-h_off)-Cuts_Off+Y_Off means the height offset + (400-height offset) - cuts offset + y offset
#                                            ^----- To Get To 800 i think -----^   ^ to recenter if needed