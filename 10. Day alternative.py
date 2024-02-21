x = 1

while x == 1:
    print("\n> Type add, show, complete, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    if user_input.startswith("add"):
        new_to_do = str(user_input[4:])
        with open("Files/user_to_do_list.txt", "r") as file:
            user_to_do_list = file.readlines()
        user_to_do_list.append(new_to_do + "\n")
        with open("Files/user_to_do_list.txt", "w") as file:
            file.writelines(user_to_do_list)
        print("Position added")

    elif user_input.startswith("show"):
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

    elif user_input.startswith("delete"):
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

    elif user_input.startswith("remove"):
        with open("Files/user_to_do_list.txt", "r") as file:
            user_to_do_list = file.readlines()
        if user_to_do_list:
            print("Current positions: ")
            for number, item in enumerate(user_to_do_list):
                item = item.strip("\n")
                row = f"{number + 1}. {item.capitalize()}"
                print(row)
            remove_number = input("Remove position number: ")
            if remove_number.isdigit():
                remove_number = int(remove_number)
                if 0 < remove_number <= len(user_to_do_list):
                    del user_to_do_list[remove_number - 1]
                    with open("Files/user_to_do_list.txt", "w") as file:
                        file.writelines(user_to_do_list)
                    print(f"Position {remove_number} removed")
                else:
                    print(" * Incorrect input * ")
            else:
                print("* Incorrect input *")
        else:
            print("The list is empty")

    elif user_input.startswith("edit"):
        try:
            edit_number = int(user_input[5:])
            with open("Files/user_to_do_list.txt", "r") as file:
                user_to_do_list = file.readlines()
                edit_entry = input("Replace position with: ")
                edit_entry = edit_entry.strip()
                try:
                    if edit_entry:
                        edit_entry = edit_entry + '\n'
                        user_to_do_list[edit_number - 1] = edit_entry
                        with open("Files/user_to_do_list.txt", "w") as file:
                            file.writelines(user_to_do_list)
                        print("Position replaced")
                        print("New position: ", edit_entry.strip("\n"))
                    else:
                        print("* Incorrect input *")
                except IndexError:
                    print("* Incorrect index position *")
                    continue
        except ValueError:
            print("* Incorrect input *")
            continue

    elif user_input.startswith("exit"):
        print("Program ended")
        x -= 1

    else:
        print(" * Incorrect input * ")