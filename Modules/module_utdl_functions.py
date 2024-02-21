FILEPATH = "Files/user_to_do_list.txt"


def function_open_list(filepath=FILEPATH):
    """ Read the main .txt file, if one exists. """
    with open(filepath, "r") as file:
        user_to_do_list_local = file.readlines()
    return user_to_do_list_local


def function_save_list(user_to_do_list_arg, filepath=FILEPATH):
    """ Save the exiting user_to_do_list to a .txt file. """
    with open(filepath, "w") as file:
        file.writelines(user_to_do_list_arg)


def function_show_positions(show):
    """ Show the contents of main .txt file. """
    print("Current positions: ")
    for number, item in enumerate(show):
        item = item.strip("\n")
        row = f"{number + 1}. {item.capitalize()}"
        print(row)
