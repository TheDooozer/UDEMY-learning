def password_creator():
    password = input("Enter new password: ")

    password_strength = []

    # Checking for length

    if len(password) >= 8:
        password_strength.append(True)
    else:
        password_strength.append(False)

    # Checking if at least one character is digit

    digit = False
    for char in password:
        if char.isdigit():
            digit = True
            break
    password_strength.append(digit)

    # Checking if at least one character is uppercase

    uppercase = False
    for char in password:
        if char.isupper():
            uppercase = True
            break
    password_strength.append(uppercase)

    if all(password_strength):
        print("Password accepted")
    else:
        print("Password not strong enough")


password_creator()
