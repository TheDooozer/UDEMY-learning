import module_utdl_functions
import time

current_time = time.strftime("%d.%m.%Y, %H:%M")
print(f"Today is {current_time}")


while True:
    print("\n> Type create, add, show, complete, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    match user_input:

        case "create":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
            except FileNotFoundError:
                user_to_do_list = []
                module_utdl_functions.function_save_list(user_to_do_list_arg=user_to_do_list)
                print("The list has been created")

        case "add" | "new":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
                new_to_do = input(">> Enter a \"to-do\": ")
                new_to_do = new_to_do.strip()
                if new_to_do:
                    user_to_do_list.append(new_to_do + "\n")
                    module_utdl_functions.function_save_list(user_to_do_list_arg=user_to_do_list)
                    print("Position added")
                else:
                    print("* Incorrect input *")
            except FileNotFoundError:
                print("There is no list created")

        case "show" | "display":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
                if user_to_do_list:
                    module_utdl_functions.function_show_positions(user_to_do_list_arg=user_to_do_list)
                else:
                    print("The list is empty")
            except FileNotFoundError:
                print("There is no list created")

        case "flush":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
                user_input = input('''Do you want to remove current list?
Type "yes" or "no": ''').lower()
                if user_input == "yes":
                    user_to_do_list = module_utdl_functions.function_open_list()
                    user_to_do_list.clear()
                    module_utdl_functions.function_save_list(user_to_do_list_arg=user_to_do_list)
                    print("List has been cleared")
                elif user_input == "no":
                    print("List has not been cleared")
                else:
                    print("* Incorrect input *")
            except FileNotFoundError:
                print("There is no list created")

        case "remove" | "delete" | "complete":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
                if user_to_do_list:
                    module_utdl_functions.function_show_positions(user_to_do_list_arg=user_to_do_list)
                    if user_input == "complete":
                        remove_number = input("\nComplete position number: ")
                    else:
                        remove_number = input("\nRemove position number: ")
                    try:
                        remove_number = int(remove_number)
                        try:
                            del user_to_do_list[remove_number - 1]
                            module_utdl_functions.function_save_list(user_to_do_list_arg=user_to_do_list)
                            if user_input == "complete":
                                print(f"Position {remove_number} completed")
                            else:
                                print(f"Position {remove_number} removed")
                        except IndexError:
                            print(" * Incorrect input * ")
                    except ValueError:
                        print("* Incorrect input *")
                else:
                    print("The list is empty")
            except FileNotFoundError:
                print("There is no list created")

        case "edit" | "change":
            try:
                user_to_do_list = module_utdl_functions.function_open_list()
                if user_to_do_list:
                    module_utdl_functions.function_show_positions(user_to_do_list_arg=user_to_do_list)
                    edit_number = input("\nEdit position number: ")
                    edit_number = edit_number.strip()
                    if edit_number.isdigit():
                        edit_number = int(edit_number)
                        if 0 < edit_number <= len(user_to_do_list):
                            edit_entry = input("Replace position with: ")
                            edit_entry = edit_entry.strip()
                            if edit_entry:
                                edit_entry = edit_entry + '\n'
                                user_to_do_list[edit_number - 1] = edit_entry
                                module_utdl_functions.function_save_list(user_to_do_list_arg=user_to_do_list)
                                print("Position replaced")
                                print("New position:", edit_entry.strip("\n").capitalize())
                            else:
                                print("* Incorrect input *")
                        else:
                            print(" * Incorrect input * ")
                    else:
                        print(" * Incorrect input * ")
                else:
                    print("The list is empty")
            except FileNotFoundError:
                print("There is no list created")

        case "exit" | "end" | "terminate":
            exit("Program ended")

        case _:
            print(" * Incorrect input * ")
