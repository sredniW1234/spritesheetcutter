import PySimpleGUI as sg
import Usefull_Operations as uo
import os


woh = 1
# Set Layout
layout = [
    [
        # Left Column
        sg.Column(
            [
                [sg.Checkbox("Match Width?", enable_events=True, key="_WIDTH_")], # Either scales the width || height
                [
                    sg.In(use_readonly_for_disable=True, enable_events=True, key="_LOAD_", disabled=True), # Displays File Path
                    sg.FileBrowse(button_text="Open Image To Cut", file_types=(("Png Files", "*.png"),))   # Button To Get File Path
                ],
                [sg.HSeparator()],
                [
                    sg.Push(), sg.Text("Tiling in X"),
                    sg.In(size=(4, 1), enable_events=True, key="_X_TILE_"),
                    sg.Push(), sg.VSeparator(), sg.Push(),
                    sg.Text("Tiling In Y "),
                    sg.In(size=(4,1), enable_events=True, key="_Y_TILE_"), sg.Push()
                ],
                [
                    sg.Push(), sg.Text("Offset in X"),
                    sg.In(size=(4,1), enable_events=True, key="_X_OFF_"),
                    sg.Push(), sg.VSeparator(), sg.Push(),
                    sg.Text("Offset in Y"),
                    sg.In(size=(4,1), enable_events=True, key="_Y_OFF_"), sg.Push()
                ],
                [sg.HSeparator()],
                [
                    sg.Button("Show Selections", key="_SHOW_")
                ]
            ]),
        sg.VSeparator(),
        # Right Column
        sg.Column(
            [
                [
                    sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(800, 800), key="_GRAPH_"), # Graph to display image
                    sg.Slider(range=(0, 400), enable_events=True, key="_CUT_OFFSET_", )
                ],
                [
                    sg.Button("Reload_Image", enable_events=True, key="_RELOAD_"),
                    sg.Button("Clear", enable_events=True, key="_CLEAR_")
                ]
            ])
    ]
]

# Setup Window
window = sg.Window("Sprite Sheet Cutter", layout, resizable=True)
window.finalize()
# Create graph element
graph = window.Element("_GRAPH_")

# Draw's initial image
uo.Draw_Image("empty pattern.png", 2, graph)


h = []
cuts_offset = 0
selections = []
x_tile = 0
y_tile = 0
x_off = 0
y_off = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "_WIDTH_" or event == "_LOAD_":
        if values["_WIDTH_"]:
            woh = 1

        elif not values["_WIDTH_"]:
            woh = 2

    if event == "_LOAD_":
        try:
            h = uo.Draw_Image(values["_LOAD_"], woh, graph)
            print(h)
        except FileNotFoundError:
            uo.Draw_Image("empty pattern.png", 2, graph)

    if event == "_X_TILE_" or event == "_Y_TILE_" or event == "_X_OFF_" or event == "_Y_OFF_":
       try:
           x_tile = int(values["_X_TILE_"])
           y_tile = int(values["_Y_TILE_"])
           x_off = int(values["_X_OFF_"])
           y_off = int(values["_Y_OFF_"])
       except:
           pass

    if event == "_CUT_OFFSET_":
        cuts_offset = values["_CUT_OFFSET_"]

    if event == "_SHOW_":
        if x_tile == 0 or y_tile == 0:
            sg.popup_ok("Tile X or Tile Y must be a non-zero positive integer")
            continue
        selections = uo.Draw_Grid(h[2], h[3], h[1], h[0], x_tile, y_tile, graph, X_Off=x_off, Y_Off=y_off, Cuts_Off=cuts_offset)

    if event == "_RELOAD_":
        if values["_LOAD_"] != "":
            window.write_event_value("_LOAD_", values["_LOAD_"])
            window.write_event_value("_SHOW_", 1)

    if event == "_CLEAR_":
        graph.erase()

window.close()
