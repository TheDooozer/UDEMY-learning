# import module_utdl_functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter text")
add_button = PySimpleGUI.Button("Add")

main_window = PySimpleGUI.Window("My First App", layout=[[label], [input_box, add_button]])
main_window.read()
main_window.close()
