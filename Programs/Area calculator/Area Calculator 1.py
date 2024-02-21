def area_calculator():

    width = 0
    length = 0

    while True:
        try:
            width = float(input("width: "))
            length = float(input("length: "))
            if width < 0.1 or length < 0.1:
                print("* incorrect input *")
                continue
            if width == length:
                print("That is a square, not rectangle")
                continue
            break
        except ValueError:
            print("enter digit value")
            continue

    area = width * length
    return area


area = area_calculator()
print(area)
