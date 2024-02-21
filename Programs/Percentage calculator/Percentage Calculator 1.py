def calculate_percentage():
    try:
        total_value = float(input("Enter total value: "))
        value = float(input("Enter percent value: "))
        result = value / total_value * 100
        print(f"That is {result}%")

    except ValueError:
        print("You need to enter a number. Run the program again.")


calculate_percentage()
