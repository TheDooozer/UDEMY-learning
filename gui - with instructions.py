# start with importing desired elements
import module_utdl_functions
import PySimpleGUI

# creating various widgets
label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter text", key="user_input")
add_button = PySimpleGUI.Button("Add")
# creating list box widget, the requirements are:
# using function from another module
# assigning key value,
# allowing interaction with events
# setting size of the widget
list_box = PySimpleGUI.Listbox(values=module_utdl_functions.function_open_list(),
                               key="list_of_to_dos",
                               enable_events=True,
                               size=(62, 15))
# creating edit widget
edit_button = PySimpleGUI.Button("Edit")
# creating delete widget
delete_button = PySimpleGUI.Button("Delete")

# creating a window widget
# layout of the window is defined my rows within 'layout'
# managing various options how window will be displayed:
# layout defines displayed elements, their placement in the window
# font defines the size of the font displayed in the window
main_window = PySimpleGUI.Window("My First App",
                                 layout=[[label],   # 1st row
                                         [input_box, add_button, edit_button, delete_button],    # 2nd row
                                         [list_box]],    # 3rd row
                                 font=("", 14))    # setting the font

# while-loop operating the whole program
while True:
    # displaying the window
    # every even and value is recorded my application as interaction
    # visible in console due to "print(event/values)"
    event, values = main_window.read()
    print("event:", event)
    print("all values:", values)
    print("values of selected dict:", values["list_of_to_dos"])

    # further actions
    # based on user input or event triggered by users actions within the program window
    match event:

        # making add_button add positions to list_box
        case "Add":
            # get existing list
            user_to_do_list = module_utdl_functions.function_open_list()
            # create new position extracting it from values dict and add new line command
            new_to_do = values["user_input"]
            # add new position to existing list
            #     .strip() method to remove whitespaces
            #     if there is nothing after using .strip() method, no position will be added
            #     as "if" will return "False" and won't trigger further code
            new_to_do = new_to_do.strip()
            if new_to_do:
                user_to_do_list.append(new_to_do + "\n")
            # save new list with new position added to it
                module_utdl_functions.function_save_list(user_to_do_list)
            # update the list_box within main_window to make changes visible (after "Add")
            # to access certain part of main_window instance, use that part's corresponding key value
            # in this case:
            # bring "main_window" variable, which is associated with .Window() function
            # use list_box key ("list_of_to_dos") to access list_box within main_window
            # update selected part of main_window using .update() method
            # within .update() use method VALUES= and provide new file/list,
            #     *VALUES= as plural as we update multiple positions
            # ie "values=user_to_do_list" in this case
            # (the same file/list that has been used to save a new file using "function_save_list()")
                main_window["list_of_to_dos"].update(values=user_to_do_list)
            # clear the input_box after adding position
                main_window["user_input"].update(value="")

        # making edit_button edit positions in list_box
        case "Edit":
            # get position to edit by extracting it from values (name proper dict)
            # select its index number (index = [0])
            to_do_to_edit = values["list_of_to_dos"][0]
            # get updated position by extracting it from values (name proper dict)
            # add new line command
            updated_to_do = values["user_input"]
            #     .strip() method to remove whitespaces
            #     if there is nothing after using .strip() method, no position will be added
            #     as "if" will return "False" and won't trigger further code
            updated_to_do = updated_to_do.strip()
            if updated_to_do:
            # open existing file
                user_to_do_list = module_utdl_functions.function_open_list()
            # get index number of position that is to be replaced
            # .index() creates a digit value based on provided input value within its parenthesis
                index = user_to_do_list.index(to_do_to_edit)
            # replace old position with new position
            # old position that is to be replaced is indicated by the index number
                user_to_do_list[index] = updated_to_do + "\n"
            # save the updated list
                module_utdl_functions.function_save_list(user_to_do_list)
            # update the list_box within main_window to make changes visible (after "Edit")
            # to access certain part of main_window instance, use that part's corresponding key value
            # in this case:
            # bring "main_window" variable, which is associated with .Window() function
            # use list_box key ("list_of_to_dos") to access list_box within main_window
            # update selected part of main_window using .update() method
            # within .update() use method VALUES= and provide new file/list,
            #     *VALUES= as plural as we update multiple positions
            # ie "values=user_to_do_list" in this case
            # (the same file/list that has been used to save a new file using "function_save_list()")
                main_window["list_of_to_dos"].update(values=user_to_do_list)
            # clear the input_box after editing position
                main_window["user_input"].update(value="")

        # make input_box display position selected from list_box
        case "list_of_to_dos":
            # update the input_box within main_window to make changes visible
            # after selecting position within list_box
            # to access certain part of main_window instance, use that part's corresponding key value
            # in this case:
            # bring "main_window" variable, which is associated with .Window() function
            # use input_box key ("user_input") to access input_box within main_window
            # update selected part of main_window using .update() method
            # within .update() use method VALUE= and use "values[*dict*][*index*]" (index = [0]),
            #     *VALUE= as singular as we update single position/element
            # point out specific dictionary, and it's index which is provided by main_window(read) function
            # that will extract the string from "values" dictionary and update the input_box with it
            #     "if" used to determine if the list is empty
            #     cannot load anything into input_box if list contains nothing
            #     that would result in TypeError, causing program to crash
            user_to_do_list = module_utdl_functions.function_open_list()
            if user_to_do_list:
                main_window["user_input"].update(value=values["list_of_to_dos"][0])

        # making delete_button delete positions from list_box
        case "Delete":
            to_do_to_delete = values["list_of_to_dos"][0]
            user_to_do_list = module_utdl_functions.function_open_list()
            index = user_to_do_list.index(to_do_to_delete)
            user_to_do_list.pop(index)
            module_utdl_functions.function_save_list(user_to_do_list)
            main_window["list_of_to_dos"].update(values=user_to_do_list)
            main_window["user_input"].update(value="")

        # closing the program
        case PySimpleGUI.WIN_CLOSED:
            break

# closing the window
main_window.close()
