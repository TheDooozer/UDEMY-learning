import module_utdl_functions
import PySimpleGUI

# creating various widgets
label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter text", key="user_input")
add_button = PySimpleGUI.Button("Add")

# creating a window widget
# layout of the window is defined my rows within 'layout'
# managing various options how window will be displayed
main_window = PySimpleGUI.Window("My First App",
                                 layout=[[label],   # 1st row
                                         [input_box, add_button]],  # 2nd row
                                 font=("", 13))    # setting the font

# while-loop operating the whole program
while True:
    # displaying the window
    event, values = main_window.read()
    print(event)
    print(values)
    # further actions, based on user input or action
    match event:
        # adding new positions
        case "Add":
            user_to_do_list = module_utdl_functions.function_open_list()
            new_to_do = values["user_input"] + "\n"
            user_to_do_list.append(new_to_do)
            module_utdl_functions.function_save_list(user_to_do_list)
        # closing the program
        case PySimpleGUI.WIN_CLOSED:
            break


# closing the window
main_window.close()
