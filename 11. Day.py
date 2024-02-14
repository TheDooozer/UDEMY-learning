def open_list():
    with open("files/user_to_do_list.txt", "r") as file_local:
        user_to_do_list_local = file_local.readlines()
    return user_to_do_list_local


def save_list():
    with open("files/user_to_do_list.txt", "w") as file_local:
        file_local.writelines(user_to_do_list)


def show_positions():
    print("Current positions: ")
    for number, item in enumerate(user_to_do_list):
        item = item.strip("\n")
        row = f"{number + 1}. {item.capitalize()}"
        print(row)


while True:
    print("\n> Type add, show, complete, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    match user_input:

        case "add" | "new":
            new_to_do = input(">> Enter a \"to-do\": ")
            new_to_do = new_to_do.strip()
            if new_to_do:
                new_to_do = new_to_do + "\n"
                user_to_do_list = open_list()
                user_to_do_list.append(new_to_do)
                save_list()
                print("Position added")
            else:
                print("* Incorrect input *")

        case "show" | "display":
            user_to_do_list = open_list()
            if user_to_do_list:
                show_positions()
            else:
                print("The list is empty")

        case "flush":
            user_input = input('''Do you want to remove current list?
Type "yes" or "no": ''').lower()
            if user_input == "yes":
                user_to_do_list = open_list()
                user_to_do_list.clear()
                save_list()
                print("List has been cleared")
            elif user_input == "no":
                print("List has not been cleared")
            else:
                print("* Incorrect input *")

        case "remove" | "delete" | "complete":
            user_to_do_list = open_list()
            if user_to_do_list:
                show_positions()
                if user_input == "complete":
                    remove_number = input("\nComplete position number: ")
                else:
                    remove_number = input("\nRemove position number: ")
                try:
                    remove_number = int(remove_number)
                    try:
                        del user_to_do_list[remove_number - 1]
                        save_list()
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

        case "edit" | "change":
            user_to_do_list = open_list()
            if user_to_do_list:
                show_positions()
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
                            save_list()
                            print("Position replaced")
                            print("New position: ", edit_entry.strip("\n"))
                        else:
                            print("* Incorrect input *")
                    else:
                        print(" * Incorrect input * ")
                else:
                    print(" * Incorrect input * ")
            else:
                print("The list is empty")

        case "exit" | "end":
            exit("Program ended")

        case _:
            print(" * Incorrect input * ")
