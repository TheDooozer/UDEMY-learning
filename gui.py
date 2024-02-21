# start with importing desired elements
from Modules import module_utdl_functions
import PySimpleGUI

# creating various widgets
label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter text", key="user_input")
add_button = PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
delete_button = PySimpleGUI.Button("Delete")
exit_button = PySimpleGUI.Button("Exit")
exit_message = PySimpleGUI.Text("Save and exit?")
yes_button = PySimpleGUI.Button("Yes")
no_button = PySimpleGUI.Button("No")

# main workspace
list_box = PySimpleGUI.Listbox(values=module_utdl_functions.function_open_list(),
                               key="list_of_to_dos",
                               enable_events=True,
                               size=(44, 15))

# window's layout
layout = [[label, add_button, edit_button, delete_button, exit_button],
          [input_box],
          [list_box]]

# exit window pop up
exit_layout = [[exit_message],
               [yes_button, no_button]]

# creating a program's window
main_window = PySimpleGUI.Window("My First App", layout=layout, font=("", 12))
exit_window = PySimpleGUI.Window("My First App", layout=exit_layout, font=("", 14))

while True:
    # displaying the window
    event, values = main_window.read()
    print("1 event:", event)
    print("2 all values:", values)
    print("3 user input values:", values["user_input"])
    print("4 values of selected dict:", values["list_of_to_dos"])

    match event:
        # add
        case "Add":
            user_to_do_list = module_utdl_functions.function_open_list()
            new_to_do = values["user_input"]
            if new_to_do:
                user_to_do_list.append(new_to_do + "\n")
                module_utdl_functions.function_save_list(user_to_do_list)
                main_window["list_of_to_dos"].update(values=user_to_do_list)
                main_window["user_input"].update(value="")

        # edit
        case "Edit":
            if values["list_of_to_dos"]:
                to_do_to_edit = values["list_of_to_dos"][0]
                updated_to_do = values["user_input"]
                updated_to_do = updated_to_do.strip()
                if updated_to_do:
                    user_to_do_list = module_utdl_functions.function_open_list()
                    index = user_to_do_list.index(to_do_to_edit)
                    user_to_do_list[index] = updated_to_do + "\n"
                    module_utdl_functions.function_save_list(user_to_do_list)
                    main_window["list_of_to_dos"].update(values=user_to_do_list)
                    main_window["user_input"].update(value="")

        # display selected position in input box
        case "list_of_to_dos":
            user_to_do_list = module_utdl_functions.function_open_list()
            if user_to_do_list:
                main_window["user_input"].update(value=values["list_of_to_dos"][0])

        # delete
        case "Delete":
            if values["list_of_to_dos"]:
                to_do_to_delete = values["list_of_to_dos"][0]
                user_to_do_list = module_utdl_functions.function_open_list()
                index = user_to_do_list.index(to_do_to_delete)
                user_to_do_list.pop(index)
                module_utdl_functions.function_save_list(user_to_do_list)
                main_window["list_of_to_dos"].update(values=user_to_do_list)
                main_window["user_input"].update(value="")

        # exit
        case "Exit":
            event, values = exit_window.read()
            match event:
                case "Yes":
                    exit()
                case "No":
                    exit_window.close()

        # closing program window with windows X button
        case PySimpleGUI.WIN_CLOSED:
            break

main_window.close()
