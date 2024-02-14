def celsius_fahrenheit_converter():

    mode = input('''Select converter mode:
> F for Fahrenheit to Celsius
> C for Celsius to Fahrenheit
> ''').capitalize()

    if mode == "F" or mode == "C":

        match mode:

            case "F":
                try:
                    fahrenheit_def = float(input("Temperature in Fahrenheit: "))
                    result = round((fahrenheit_def - 32) * 5/9, 1)
                    converted_temperature = f"Temperature in Celsius: {result}"
                    return converted_temperature
                except ValueError:
                    print(" * Incorrect input * ")

            case "C":
                try:
                    celsius_def = float(input("Temperature in Celsius: "))
                    result = round(celsius_def * 1.8 + 32, 1)
                    converted_temperature = f"Temperature in Fahrenheit: {result}"
                    return converted_temperature
                except ValueError:
                    print(" * Incorrect input * ")
    else:
        print(" * Incorrect input *")


temperature = celsius_fahrenheit_converter()
exit(temperature)
