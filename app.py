import PySimpleGUI as sg
import Functions as F

graph_width, graph_height = 480, 480

layout = [
    [

        # Left Column
        sg.Column([
            [
                sg.Checkbox("Match Width?",
                            tooltip="Resizes so that either the width(checked) matches the screen or "
                                    "the height(unchecked) matches the screen", enable_events=True, key="_WIDTH_")
            ],
            [
                # Path Selection
                sg.In(disabled=True, enable_events=True,key="_LOAD_", default_text="Image Path Will Show Here"),
                sg.FileBrowse("Open Image", file_types=(("png Files", ".png"),))
            ],
            [
                sg.In(disabled=True, enable_events=True, key="_SAVE_", default_text="Locations Of Saved Images Will Appear Here"),
                sg.FolderBrowse("Location Of Final Sprites")
            ],
            [sg.HSeparator()],

            # Parameters for cutting
            [sg.Frame("Cutting Parameters", [
                    [
                        sg.Text("X Tile Size"), sg.InputText(size=(4, 1), enable_events=True, key="_X_TILE_"),
                        sg.Text("Y Tile Size"), sg.InputText(size=(4, 1), enable_events=True,key="_Y_TILE_"),
                    ],
                    [sg.HSeparator()],
                    [
                        sg.Text("Offset in X"), sg.InputText(size=(4, 1), enable_events=True, key="_X_OFF_", tooltip="Works but still WIP"),
                        sg.Text(" Offset in Y"), sg.InputText(size=(4, 1), enable_events=True, key="_Y_OFF_", tooltip="Works but still WIP"),
                    ]
                ], element_justification='Center'),
             sg.Push()
            ],
            # Show Cuts & Cut Button
            [
                sg.Button("Show Cuts", key="_SHOW_"),
                sg.Button("Cut Image", key="_CUT_")
            ]
        ]),
        sg.VSeparator(),

        # Right Column
        sg.Column([
            [
                # Displays Image & Cuts
                sg.Graph(canvas_size=(graph_width, graph_height), graph_bottom_left=(0, 0), graph_top_right=(480,480), key="_GRAPH_"),
                sg.Slider(range=(0,480), size=(25, 25), enable_events=True,tooltip="Repositions The Cuts Vertically", key="_SLIDER_Y_")
            ],
            [
                sg.Slider(range=(0,400), size=(53, 25), enable_events=True, tooltip="Repositions The Cuts Horizontally", key="_SLIDER_X_", orientation="horizontal")
            ],
            [
                sg.Push(), sg.Button("Clear all Above", key = "_CLEAR_"),
                sg.Push(), sg.Button("Reload image Above", tooltip="Will Remove Cuts If They Exist", key="_RELOAD_"), sg.Push()
            ]
        ])
    ]
]

window = sg.Window("Title", layout)
window.finalize()

graph = window.Element("_GRAPH_")


F.Display_Image(F.Resize("empty pattern.png", graph_height, False)[0], graph_height, graph)


w = False
x_tile = 0
y_tile = 0
x_off = 0
y_off = 0
p = []
cut_y = 0
cut_x = 0
save_location = 0
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "_WIDTH_":
        if values["_WIDTH_"]:
            w = True
        else:
            w = False

    if event == "_Y_OFF_" or event == "_X_OFF_" or event == "_Y_TILE_" or event == "_X_TILE_":
        if type(values["_Y_OFF_"]) == str and values["_Y_OFF_"].isnumeric():
            y_off = int(values["_Y_OFF_"])
        if type(values["_X_OFF_"]) == str and values["_X_OFF_"].isnumeric():
            x_off = int(values["_X_OFF_"])
        if type(values["_Y_TILE_"]) == str and values["_Y_TILE_"].isnumeric():
            y_tile = int(values["_Y_TILE_"])
        if type(values["_X_TILE_"]) == str and values["_X_TILE_"].isnumeric():
            x_tile = int(values["_X_TILE_"])

    if event == "_SLIDER_X_":
        cut_x = int(values["_SLIDER_X_"])

    if event == "_SLIDER_Y_":
        cut_y = int(values["_SLIDER_Y_"])

    if event == "_CLEAR_":
        graph.erase()
        F.Display_Image(F.Resize("empty pattern.png", graph_height, False)[0], graph_height, graph)

    if event == "_RELOAD_":
        if values["_LOAD_"] != "Image Path Will Show Here":
            window.write_event_value("_LOAD_", values["_LOAD_"])
        else:
            pass

    if event == "_LOAD_":
        try:
            p = F.Resize(values["_LOAD_"], graph_height, w) # p for outPut
            F.Display_Image(p[0], graph_height, graph)
        except FileNotFoundError:
            sg.popup_ok(f"No File Found At {values['_LOAD_']}")

    if event == "_SHOW_":
        try:
            boxie = F.Show_Cuts(x_tile, y_tile, p[1], p[2], p[3], graph, x_off, y_off, cut_x, cut_y)
        except IndexError:
            sg.PopupOK("Must Select a valid Image")
        except ZeroDivisionError:
            sg.PopupOK("X Tile or Y Tile must be greater than 0")

    if event == "_SAVE_":
        save_location = values["_SAVE_"]

    if event == "_CUT_":
        try:
            F.Cut_Image(p[0], boxie, save_location, graph)
        except FileNotFoundError:
            sg.popup_ok("Please Select A Valid File Location")
window.close()