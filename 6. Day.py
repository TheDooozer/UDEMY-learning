x = 1

while x == 1:
    print("> Type add, show, complete, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    match user_input:

        case "add":
            to_do = input(">> Enter a \"to-do\": ")
            to_do = to_do.strip()
            if to_do:
                to_do = to_do + "\n"
                file = open("Files/user_to_do_list.txt", "r")
                user_to_do_list = file.readlines()
                file.close()
                user_to_do_list.append(to_do)
                file = open("Files/user_to_do_list.txt", "w")
                file.writelines(user_to_do_list)
                file.close()
                print("Position added")
            else:
                print("* Incorrect input *")

        case "show" | "display":
            file = open("Files/user_to_do_list.txt", "r")
            user_to_do_list = file.readlines()
            file.close()
            if user_to_do_list:
                print("The list currently contains: ")
                for number, item in enumerate(user_to_do_list):
                    row = f"{number + 1}. {item.capitalize()}"
                    print(row)
            else:
                print("The list is empty")

        case "flush":
            file = open("Files/user_to_do_list.txt", "r")
            user_to_do_list = file.readlines()
            file.close()
            user_to_do_list.clear()
            file = open("Files/user_to_do_list.txt", "w")
            file.writelines(user_to_do_list)
            file.close()
            print("List cleared")

        case "remove" | "delete" | "complete":
            print("Current positions: ")
            file = open("Files/user_to_do_list.txt", "r")
            user_to_do_list = file.readlines()
            file.close()
            for number, item in enumerate(user_to_do_list):
                row = f"{number + 1}. {item.capitalize()}"
                print(row)
            if user_input == "complete":
                remove_number = input("Complete position number: ")
            else:
                remove_number = input("Remove position number: ")
            if remove_number.isdigit():
                remove_number = int(remove_number)
                if 0 <= remove_number <= len(user_to_do_list):
                    del user_to_do_list[remove_number - 1]
                    file = open("Files/user_to_do_list.txt", "w")
                    file.writelines(user_to_do_list)
                    file.close()
                    if user_input == "complete":
                        print("Position completed")
                    else:
                        print("Position removed")
                else:
                    print("* Invalid position number *")
            else:
                print("* Invalid input, please enter a number *")

        case "edit" | "change":
            print("Current positions:")
            file = open("Files/user_to_do_list.txt", "r")
            user_to_do_list = file.readlines()
            file.close()
            for number, item in enumerate(user_to_do_list):
                row = f"{number + 1}. {item.capitalize()}"
                print(row)
            edit_number = int(input("Edit position number: "))
            if 0 <= edit_number <= len(user_to_do_list):
                edit_entry = input("Replace position with: ") + "\n"
                user_to_do_list[edit_number - 1] = edit_entry
                file = open("Files/user_to_do_list.txt", "w")
                file.writelines(user_to_do_list)
                file.close()
                print("Position replaced")
                print("New position: ", edit_entry)
            else:
                print("* Invalid position number *")

        case "exit" | "end":
            print("Program ended")
            x -= 1

        case _:
            print(" * Incorrect input * ")
