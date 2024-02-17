# start with importing desired elements
import module_utdl_functions
import PySimpleGUI

# creating various widgets
label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter text", key="user_input")
add_button = PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
delete_button = PySimpleGUI.Button("Delete")
list_box = PySimpleGUI.Listbox(values=module_utdl_functions.function_open_list(),
                               key="list_of_to_dos",
                               enable_events=True,
                               size=(62, 15))

# creating a window widget
main_window = PySimpleGUI.Window("My First App",
                                 layout=[[label],   # 1st row
                                         [input_box, add_button, edit_button, delete_button],    # 2nd row
                                         [list_box]],    # 3rd row
                                 font=("", 14))    # setting the font

while True:
    # displaying the window
    event, values = main_window.read()
    print("event:", event)
    print("all values:", values)
    print("values of selected dict:", values["list_of_to_dos"])

    match event:
        case "Add":
            user_to_do_list = module_utdl_functions.function_open_list()
            new_to_do = values["user_input"]
            if new_to_do:
                user_to_do_list.append(new_to_do + "\n")
                module_utdl_functions.function_save_list(user_to_do_list)
                main_window["list_of_to_dos"].update(values=user_to_do_list)
                main_window["user_input"].update(value="")

        case "Edit":
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

        case "list_of_to_dos":
            user_to_do_list = module_utdl_functions.function_open_list()
            if user_to_do_list:
                main_window["user_input"].update(value=values["list_of_to_dos"][0])

        case "Delete":
            to_do_to_delete = values["list_of_to_dos"][0]
            user_to_do_list = module_utdl_functions.function_open_list()
            index = user_to_do_list.index(to_do_to_delete)
            user_to_do_list.pop(index)
            module_utdl_functions.function_save_list(user_to_do_list)
            main_window["list_of_to_dos"].update(values=user_to_do_list)
            main_window["user_input"].update(value="")

        case PySimpleGUI.WIN_CLOSED:
            break

main_window.close()
