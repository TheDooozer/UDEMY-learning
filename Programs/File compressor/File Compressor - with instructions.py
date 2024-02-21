# importing important imports
import PySimpleGUI
from Modules.module_zip_creator import zip_it

# first row of main window, label, input box and select button
label_1 = PySimpleGUI.Text("Select file to compress")
label_1_box = PySimpleGUI.InputText(tooltip="Enter directory")
select_button_1 = PySimpleGUI.FilesBrowse("select file", key="file")

# second row of main window, label, input box and select button
label_2 = PySimpleGUI.Text("Select destination folder")
label_2_box = PySimpleGUI.InputText(tooltip="Enter directory")
select_button_2 = PySimpleGUI.FolderBrowse("select folder", key="folder")

# after-conversion message
output_message = PySimpleGUI.Text(key="output", text_color="pink")

# third row of main window, buttons
button_1 = PySimpleGUI.Button("Compress")
button_2 = PySimpleGUI.Button("Exit")

# layout of the whole window
layout = [[label_1, label_1_box, select_button_1],
          [label_2, label_2_box, select_button_2],
          [button_2, button_1, output_message]]

# main program window configuration
main_window = PySimpleGUI.Window("The Magnificent File Compresser", layout=layout)

# main program
while True:
    # running main window
    # assigning event and value to data provided by main_window.read()
    event, values = main_window.read()
    # extracting file path from .FileBrowse() function
    # splitting it with .split() to obtain operable list instead of plain string
    filepath = values["file"].split(";")
    # extracting destination folder path from .FolderBrowse() function
    folder = values["folder"]

    match event:

        # compresser
        case "Compress":
            # calling main program's function, the compresser
            # filepath(s) and destination folder are provided by extracting
            # information from even/values from main_window.read()
            zip_it(filepath_input=filepath, destination_directory_input=folder)
            # updating main window with 'operation successful' message
            # changing the previously-empty "output" message using .update(value=)
            main_window["output"].update(value="Compression completed")

        # exit program
        case "Exit":
            break

main_window.close()
