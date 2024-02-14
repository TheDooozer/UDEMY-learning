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
    user_input = input("> Type add, show, flush or exit: ")
    user_input = user_input.lower()
    user_input = user_input.strip()

    match user_input:
        case "add":
            to_do = input(">> Enter a \"to-do\": ")
            user_to_do_list.append(to_do)
            print("Position >", to_do, "< added to the list")
            continue
        case "show" | "display":
            print("The list currently contains:")
            for item in user_to_do_list:
                item = item.title()
                print(item)
            continue
        case "flush":
            user_to_do_list.clear()
            print("List cleared")
            continue
        case "exit":
            print("Program terminated")
            x -= 1
            continue
        case _:
            print(" * Incorrect input * ")
            continue
