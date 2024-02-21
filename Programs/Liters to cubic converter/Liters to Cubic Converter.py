def foo(liters):
    m3 = liters / 1000
    result = f"{liters} liters equals to {m3} cubic meters."
    return result


liters_to_convert = float(input("Gib liters. "))

liters_converted = foo(liters=liters_to_convert)

print(liters_converted)
