import PySimpleGUI as sg
import Functions as F

graph_width, graph_height = 480, 480
empty_pattern_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x04\x00\x00\x00\x02@\x08\x00\x00\x00\x006\xfeK\t' \
                     b'\x00\x00\x07kIDATx\x9c\xed\xdd\xb1Q\x050\x0c\x05AL\xff=\x7f:@\x91\xc6\x86\xdbM=/\xbdq\xa6\xf3' \
                     b'\xf9\xfa\xdd\x19\xde\xed\xed\xed\xff\xee\xfe{' \
                     b'x\x07\xfe1\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800' \
                     b'\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x80' \
                     b'\xb0\xe9|\xf8\xf5\xfb\xe5\xf6\xf6\xf6{{' \
                     b'?\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b'\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00' \
                     b'\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13' \
                     b'\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b';\xaf\xdf/\xb7\xb7\xb7\xdf\xdb\xfb\x01@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\xd8t>\xfc\xfa\xfdr{{' \
                     b'\xfb\xbd\xbd\x1f\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84' \
                     b'\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t' \
                     b'\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00' \
                     b'\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\x9d\xd7\xef\x97\xdb\xdb\xdb\xef\xed\xfd\x00 L\x00 ' \
                     b'L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 ' \
                     b'L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 ' \
                     b'l:\x1f~\xfd~\xb9\xbd\xbd\xfd\xde\xde\x0f\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00' \
                     b'\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04' \
                     b'\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2' \
                     b'\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00' \
                     b'\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\xce\xeb\xf7\xcb\xed\xed\xed\xf7\xf6~\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x106\x9d\x0f\xbf' \
                     b'~\xbf\xdc\xde\xde~o\xef\x07\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02' \
                     b'\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02' \
                     b'\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02' \
                     b'\x00a\x02\x00a\x02\x00a\x02\x00a\xe7\xf5\xfb\xe5\xf6\xf6\xf6{{' \
                     b'?\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b'\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00' \
                     b'\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13' \
                     b'\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b'\x9b\xce\x87_\xbf_noo\xbf\xb7\xf7\x03\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x800\x01\x800\x01\x800\x01\x80\xb0\xf3\xfa\xfdr{{' \
                     b'\xfb\xbd\xbd\x1f\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84' \
                     b'\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t' \
                     b'\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00' \
                     b'\x84\t\x00\x84\t\x00\x84\t\x00\x84\t\x00\x84M\xe7\xc3\xaf\xdf/\xb7\xb7\xb7\xdf\xdb\xfb\x01' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00@\x98\x00' \
                     b'@\xd8y\xfd~\xb9\xbd\xbd\xfd\xde\xde\x0f\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00' \
                     b'\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04' \
                     b'\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2' \
                     b'\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00' \
                     b'\xc2\x04\x00\xc2\x04\x00\xc2\x04\x00\xc2\xa6\xf3\xe1\xd7\xef\x97\xdb\xdb\xdb\xef\xed\xfd\x00 ' \
                     b'L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 ' \
                     b'L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 L\x00 ' \
                     b'\xec\xbc~\xbf\xdc\xde\xde~o\xef\x07\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a' \
                     b'\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02' \
                     b'\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02\x00a\x02' \
                     b'\x00a\x02\x00a\x02\x00a\x02\x00a\xd3\xf9\xf0\xeb\xf7\xcb\xed\xed\xed\xf7\xf6~\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10' \
                     b'&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10&\x00\x10v^\xbf_noo' \
                     b'\xbf\xb7\xf7\x03\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800' \
                     b'\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01\x800\x01' \
                     b'\x800\x01\x80\xb0\xe9|\xf8\xf5\xfb\xe5\xf6\xf6\xf6{{' \
                     b'?\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b'\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00' \
                     b'\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13' \
                     b'\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08\x13\x00\x08' \
                     b'\xfb\x01\x1e\xc8$u\xd0\xb2 /\x00\x00\x00\x00IEND\xaeB`\x82 '

sg.theme("DarkGrey1")

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
                    ],
                ], element_justification='Center'),
             sg.Push()
            ],
            # Show Cuts & Cut Button
            [
                sg.Button("Show Cuts", key="_SHOW_"),
                sg.Button("Cut Image", key="_CUT_")
            ],
            # Optional
            [
                sg.Frame("Optional After Cutting Options", [
                    [
                        sg.Text("Remove Fully Transparent Sprite To Not Clog Folder:")
                    ],
                    [
                        sg.Push(), sg.Button("Fast Remove", tooltip="(Chance to not get everything if unlucky)", key="_FAST_"), sg.Push()
                    ],[sg.HSep()],
                    [
                        sg.Text("Remove Duplicate Sprites Of Your Choosing:")
                    ],
                    [
                        sg.In(disabled=True, enable_events=True, key="_DUPE_", default_text="Dupe Sprite Location"),
                        sg.FileBrowse("Dupe Remove", tooltip="Removes Selected Duplicates of sprite", file_types=(("png Files", ".png"),))
                    ],[sg.HSep()],
                    [
                        sg.Text("Automatically Remove Duplicate Sprites:"),
                        sg.Push(), sg.Button("Auto Dupe Remove", tooltip="Removes Duplicates Of All Sprites", key="_DUPEALL_")
                    ]
                ])
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
                sg.Push(), sg.Button("Reload Above", tooltip="Will Remove Cuts If They Exist", key="_RELOAD_"), sg.Push()
            ]
        ])
    ]
]
window = sg.Window("Title", layout)
window.finalize()

graph = window.Element("_GRAPH_")

F.Display_Image(empty_pattern_data, graph_height, graph)

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
        F.Display_Image(empty_pattern_data, graph_height, graph)

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
        except TypeError:
            sg.popup_ok("Please Show Cuts First To Verify")
        except IndexError:
            sg.popup_ok("Please Select A Valid File Location")

    if event == "_FAST_":
        try:
            F.Fast_scan(values["_SAVE_"])
        except FileNotFoundError:
            sg.PopupOK("Please Select A Output Folder")
    
    if event == "_DUPE_":
        try:
            F.Dupe_remove(values["_DUPE_"])
        except FileNotFoundError:
            sg.PopupOK("Please Select A Sprite")
    if event == "_DUPEALL_":
        try:
            F.Auto_Dupe_remove(values["_SAVE_"], sg)
        except FileNotFoundError:
            sg.PopupOK("Please Select A Output Folder")
window.close()