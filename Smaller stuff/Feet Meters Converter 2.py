import module_fmc_function

user_input = input("feet and inches: ")

extracted = module_fmc_function.function_extract(feet_inches=user_input)

result = module_fmc_function.function_convert(extracted['feet'], extracted['inches'])

print(f"{extracted['feet']} feet and {extracted['inches']} is equal to {result}")

if result < 1:
    print("Not big enuf")
else:
    print("Big enuf")
