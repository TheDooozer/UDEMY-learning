#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
user_to_do_list = ["pies", "dupa"]
x = 1

while x == 1:
    print("> Type add, show, flush, edit, remove or exit: ")
    user_input = input().lower().strip()

    match user_input:

        case "add":
            to_do = input(">> Enter a \"to-do\": ")
            user_to_do_list.append(to_do)
            print("Position >", to_do, "< added to the list")

        case "show" | "display":
            if user_to_do_list:
                print("The list currently contains:")
                for item in user_to_do_list:
                    print("-", item.title())
            else:
                print("The list is empty")

        case "flush":
            user_to_do_list.clear()
            print("List cleared")

        case "remove" | "delete":
            print("Current positions:")
            for number, item in enumerate(user_to_do_list):
                print(number, ".", item.title())
            remove_number = input("Remove position number:")
            if remove_number.isdigit():
                remove_number = int(remove_number)
                if 0 <= remove_number < len(user_to_do_list):
                    del user_to_do_list[remove_number]
                else:
                    print("* Invalid position number *")
            else:
                print("* Invalid input, please enter a number *")

        case "edit" | "change":
            print("Current positions:")
            for number, item in enumerate(user_to_do_list):
                print(number, ".", item.title())
            edit_number = int(input("Edit position number: "))
            if 0 <= edit_number < len(user_to_do_list):
                edit_entry = input("Replace position with: ")
                user_to_do_list[edit_number] = edit_entry
                print("Position replaced")
                print("New position: ", edit_entry)
            else:
                print("* Invalid position number *")

        case "exit" | "end":
            print("Program ended")
            x -= 1

        case _:
            print(" * Incorrect input * ")

