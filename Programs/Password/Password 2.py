def password_creator():
    print("Password requirements: Minimum eight characters, \nminimum one digit and one uppercase character.")
    password = input("> Enter new password: ")
    password_strength = {"length": False, "digit": False, "uppercase": False}

    if len(password) >= 8:
        password_strength["length"] = True

    for char in password:
        if char.isdigit():
            password_strength["digit"] = True

    for char in password:
        if char.isupper():
            password_strength["uppercase"] = True

    if all(password_strength.values()):
        password_state = "Password accepted"
        return password_state
    else:
        password_state = "Password not strong enough"
        return password_state


password_creator = password_creator()
print(password_creator)
