mode_selection = input('''Select converter mode:
> F for feet and inches to meters
> M for meters to feet and inches
> ''')


def feet_inches_meters_converter(mode_selection_local):
    while True:
        mode = mode_selection_local.upper().strip()

        if mode == "F" or mode == "M":
            match mode:
                case "F":
                    try:
                        feet_inches = input("Enter feet and/or inches: ")
                        feet_inches.lstrip().rstrip()
                        if " " in feet_inches:
                            parts = feet_inches.split(" ")
                            feet = float(parts[0])
                            inches = float(parts[1])
                        else:
                            feet = float(feet_inches)
                            inches = 0
                        while inches >= 12:
                            inches -= 12
                            feet += 1
                        meters = feet * 0.3048 + inches * 0.0254
                        kilometers = 0
                        while meters >= 1000:
                            meters -= 1000
                            kilometers += 1
                        if kilometers > 0:
                            exit(f"{feet} feet and {inches} inches is equal to {kilometers} kilometers "
                                 f"and {round(meters, 2)} meters.")
                        else:
                            exit(f"{feet} feet and {inches} inches is equal to {round(meters, 2)} meters.")
                    except ValueError:
                        print(" * Incorrect input * \n")

                case "M":
                    try:
                        meters = float(input("Enter meters: "))
                        inches = meters * 39.3701
                        feet = 0
                        while inches >= 12:
                            inches -= 12
                            feet += 1
                            if inches < 0:
                                inches = 0
                        exit(f"{meters} meters is equal to {feet} feet and {round(inches)} inches.")
                    except ValueError:
                        print(" * Incorrect input * \n")

        else:
            print(" * Incorrect input * \n")
            break


feet_inches_meters_converter(mode_selection_local=mode_selection)
