def character_counter():
    print("Enter a title of your book:")
    user_title = input()
    user_title_length = len(user_title)

    if 1 < user_title_length < 1000:
        print("Your book's title is", user_title_length, "characters long")
    elif user_title_length <= 1:
        print("Are you sure that this is the actual tittle?")
    else:
        print("What?")


character_counter()
