import PySimpleGUI as sg
import Usefull_Operations as F

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
                sg.Graph(canvas_size=(graph_width, graph_height), graph_bottom_left=(0, 0), graph_top_right=(480,480), key="_GRAPH_")
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
xtile = 0
ytile = 0
xoff = 0
yoff = 0
p = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "_WIDTH_":
        if values["_WIDTH_"]:
            w = True
        else:
            w = False

    if event == "_X_TILE_" or event == "_Y_TILE_" or event == "_X_OFF_" or event == "_Y_OFF_":
        try:
            xtile = int(values["_X_TILE_"])
            ytile = int(values["_Y_TILE_"])
            xoff = int(values["_X_OFF_"])
            yoff = int(values["_Y_OFF_"])
        except ValueError:
            pass

    if event == "_CLEAR_":
        graph.erase()
        F.Display_Image(F.Resize("empty pattern.png", graph_height, False)[0], graph_height, graph)

    if event == "_RELOAD_":
        if values["_LOAD_"] != "Image Path Will Show Here":
            window.write_event_value("_LOAD_", values["_LOAD_"])
        else:
            pass

    if event == "_LOAD_":
        p = F.Resize(values["_LOAD_"], graph_height, w) # p for outPut
        F.Display_Image(p[0], graph_height, graph)

    if event == "_SHOW_":
        F.Show_Cuts(xtile, ytile, p[1], p[2], p[3], graph, xoff=xoff, yoff=yoff)
window.close()