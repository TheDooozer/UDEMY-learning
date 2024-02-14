#
#
#
#
#
def get_valid_date():
    while True:
        user_day = input("Enter today's date in DD.MM.YYYY format: ")
        if all(characters.isdigit() or characters in [".", ":", "/"] for characters in user_day):
            print(f"Entry for {user_day} created")
            return user_day
        else:
            print("* Invalid input *")


while True:
    current_date = get_valid_date()

    user_day_rating = input("How do you rate your mood today, from 1 to 10? ")
    if user_day_rating.isdigit():
        with open(f"files/{current_date}.txt", "w") as file:
            file.writelines("Day " + current_date + "\n")
            file.writelines("Today's rating is " + user_day_rating + "\n")

        user_diary_input = input("Describe the day in a few words ").capitalize()

        with open(f"files/{current_date}.txt", "r") as file:
            current_day = file.readlines()

        current_day.append("\n" + user_diary_input)

        with open(f"files/{current_date}.txt", "w") as file:
            file.writelines(current_day)
        break
    else:
        print("* Incorrect input *")



#if user_input:
#    print(user_input)
#    with open("files/journal.txt", "r") as file:
#        user_journal = file.readlines()



#input("How do you rate your mood today from 1 to 10? ")
#input("Let your thoughts flow: ")