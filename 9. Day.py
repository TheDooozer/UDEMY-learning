x = 1

while x == 1:
    print("\n> Type add, show, complete, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    match user_input:

        case "add" | "new":
            new_to_do = input(">> Enter a \"to-do\": ")
            new_to_do = new_to_do.strip()
            if new_to_do:
                new_to_do = new_to_do + "\n"
                with open("Files/user_to_do_list.txt", "r") as file:
                    user_to_do_list = file.readlines()
                user_to_do_list.append(new_to_do)
                with open("Files/user_to_do_list.txt", "w") as file:
                    file.writelines(user_to_do_list)
                print("Position added")
            else:
                print("* Incorrect input *")

        case "show" | "display":
            with open("Files/user_to_do_list.txt", "r") as file:
                user_to_do_list = file.readlines()
            if user_to_do_list:
                print("The list currently contains: ")
                for number, item in enumerate(user_to_do_list):
                    item = item.strip("\n")
                    row = f"{number + 1}. {item.capitalize()}"
                    print(row)
            else:
                print("The list is empty")

        case "flush":
            user_input = input('''Do you want to remove current list?
Type "yes" or "no": ''').lower()
            if user_input == "yes":
                user_to_do_list.clear()
                with open("Files/user_to_do_list.txt", "w") as file:
                    file.writelines(user_to_do_list)
                print("List has been cleared")
            elif user_input == "no":
                print("List has not been cleared")
            else:
                print("* Incorrect input *")

        case "remove" | "delete" | "complete":
            with open("Files/user_to_do_list.txt", "r") as file:
                user_to_do_list = file.readlines()
            if user_to_do_list:
                print("Current positions: ")
                for number, item in enumerate(user_to_do_list):
                    item = item.strip("\n")
                    row = f"{number + 1}. {item.capitalize()}"
                    print(row)
                if user_input == "complete":
                    remove_number = input("Complete position number: ")
                else:
                    remove_number = input("Remove position number: ")
                if remove_number.isdigit():
                    remove_number = int(remove_number)
                    if 0 < remove_number <= len(user_to_do_list):
                        del user_to_do_list[remove_number - 1]
                        with open("Files/user_to_do_list.txt", "w") as file:
                            file.writelines(user_to_do_list)
                        if user_input == "complete":
                            print(f"Position {remove_number} completed")
                        else:
                            print(f"Position {remove_number} removed")
                    else:
                        print(" * Incorrect input * ")
                else:
                    print("* Incorrect input *")
            else:
                print("The list is empty")

        case "edit" | "change":
            with open("Files/user_to_do_list.txt", "r") as file:
                user_to_do_list = file.readlines()
            if user_to_do_list:
                print("Current positions:")
                for number, item in enumerate(user_to_do_list):
                    item = item.strip("\n")
                    row = f"{number + 1}. {item.capitalize()}"
                    print(row)
                edit_number = input("Edit position number: ")
                edit_number = edit_number.strip()
                if edit_number:
                    edit_number = int(edit_number)
                    if 0 < edit_number <= len(user_to_do_list):
                        edit_entry = input("Replace position with: ")
                        edit_entry = edit_entry.strip()
                        if edit_entry:
                            edit_entry = edit_entry + '\n'
                            user_to_do_list[edit_number - 1] = edit_entry
                            with open("Files/user_to_do_list.txt", "w") as file:
                                file.writelines(user_to_do_list)
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
            print("Program ended")
            x -= 1

        case _:
            print(" * Incorrect input * ")
