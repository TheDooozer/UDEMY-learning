def get_valid_date():
    while True:
        user_day = input("Enter today's date in DD.MM.YYYY format: ")
        if all(characters.isdigit() or characters in [".", ",", ":", "/"] for characters in user_day):
            user_day = user_day.replace(",", ".").replace(":", ".").replace("/", ".")
            print(f"Entry for {user_day} created")
            return user_day
        else:
            print("* Invalid input *")


def get_mood():
    while True:
        user_mood = input("How do you rate your mood today, from 1 to 10? ")
        if user_mood.isdigit():
            return user_mood
        else:
            print("* Invalid input *")


def get_diary():
    while True:
        user_diary_input = input("Describe the day in a few words: \n ").capitalize()
        return user_diary_input


while True:
    date = get_valid_date()
    mood = get_mood()
    entry = get_diary()

    with open(f"files/{date}.txt", "w") as file:
        file.writelines("Today's date is " + date + "\n")
        file.writelines("Mood rating is " + mood + "\n" + "\n")
        file.writelines(entry)
        file.close()

    print("Thanks, see you later.")
    break
