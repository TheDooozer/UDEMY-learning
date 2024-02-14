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
print('''Welcome to The Ultimate To-Do List Creator!
- to add new position type ADD
- to count existing positions type COUNT
- to show existing positions type SHOW
- to delete the content of the list type DELETE
- to exit program type EXIT
''')

user_list = [1, 2, 3]
X = 1


def user_input():
    x = input("> ")
    x = x.upper()
    return x


def next_position():
    y = input("> ")
    y = y.title()
    return y


while X == 1:

    word = user_input()
    if word == "ADD":
        print("Enter another position")
        position = next_position()
        user_list.append(position)
        print("Position", position, "has been added")

    elif word == "DELETE":
        user_list.clear()
        print("The list has been cleared")

    elif word == "SHOW":
        print(user_list)

    elif word == "COUNT":
        print(len(user_list))

    elif word == "EXIT":
        X -= 1
