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
print('''This is "To-Do" List maker.
- to add another position, type it in and press ENTER 
- to end editing, type END and press ENTER \n''')

user_prompt = "Enter a to-do: "

user_todo_list = []

x = 0

while x == 0:
    user_todo = input(user_prompt)
    if user_todo == "end":
        print(user_todo_list)
        break
    else:
        user_todo_list.append(user_todo.capitalize())
        print(user_todo_list)

