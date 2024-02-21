import PySimpleGUI
from Modules.module_zip_creator import zip_it

label_1 = PySimpleGUI.Text("Select file to compress")
label_1_box = PySimpleGUI.Input(tooltip="Enter directory")
select_button_1 = PySimpleGUI.FilesBrowse("select file", key="file")

label_2 = PySimpleGUI.Text("Select destination folder")
label_2_box = PySimpleGUI.Input(tooltip="Enter directory")
select_button_2 = PySimpleGUI.FolderBrowse("select folder", key="folder")

output_message = PySimpleGUI.Text(key="output", text_color="pink")

button_1 = PySimpleGUI.Button("Compress")
button_2 = PySimpleGUI.Button("Exit")

layout = [[label_1, label_1_box, select_button_1],
          [label_2, label_2_box, select_button_2],
          [button_2, button_1, output_message]]

main_window = PySimpleGUI.Window("The Magnificent File Compresser", layout=layout)

while True:
    event, values = main_window.read()
    filepath = values["file"].split(";")
    folder = values["folder"]

    match event:

        case "Compress":
            zip_it(filepath_input=filepath, destination_directory_input=folder)
            main_window["output"].update(value="Compression completed")

        case "Exit":
            break

main_window.close()
