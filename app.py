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
                    sg.In(enable_events=True, key="_LOAD_"),                                              # Displays File Path
                    sg.FileBrowse(button_text="Open Image To Cut", file_types=(("Png Files", "*.png"),))  # Button To Get File Path
                ],
                [sg.HSeparator()],
                [
                    sg.Push(), sg.Text("Tile in X"),
                    sg.In(size=(4, 1), enable_events=True, key="_X_TILE_"),
                    sg.VSeparator(),
                    sg.Text("Tile In Y"),
                    sg.In(size=(4,1), enable_events=True, key="_Y_TILE_"),
                ],
                [
                    sg.Text("Offset in X:"),
                    sg.In(size=(4,1), enable_events=True, key="_X_OFF_"),
                    sg.VSeparator(),
                    sg.Text("Offset in Y"),
                    sg.In(size=(4,1), enable_events=True, key="_Y_OFF_")
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

    if event == "_CUT_OFFSET_":
        cuts_offset = values["_CUT_OFFSET_"]

    if event == "_SHOW_":
        selections = uo.Draw_Grid(h[2], h[3], h[1], h[0], 16, 16, graph, Cuts_Off=cuts_offset)

    if event == "_RELOAD_":
        if values["_LOAD_"] != "":
            window.write_event_value("_LOAD_", values["_LOAD_"])
            window.write_event_value("_SHOW_", 1)

    if event == "_CLEAR_":
        graph.erase()

window.close()
