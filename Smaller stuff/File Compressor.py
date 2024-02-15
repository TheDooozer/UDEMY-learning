import PySimpleGUI

label_1 = PySimpleGUI.Text("Select file to compress")
label_1_box = PySimpleGUI.InputText(tooltip="Enter directory")
select_button_1 = PySimpleGUI.FilesBrowse("select")

label_2 = PySimpleGUI.Text("Select destination folder")
label_2_box = PySimpleGUI.InputText(tooltip="Enter directory")
select_button_2 = PySimpleGUI.FolderBrowse("select")

button_1 = PySimpleGUI.Button("Compress")
button_2 = PySimpleGUI.Button("Exit")

main_window = PySimpleGUI.Window("The Magnificent File Compresser",
                                 layout=[[label_1, label_1_box, select_button_1],
                                         [label_2, label_2_box, select_button_2],
                                         [button_2, button_1]])
main_window.read()
main_window.close()
