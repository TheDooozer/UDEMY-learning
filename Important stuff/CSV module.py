import csv

with open("test/test.csv", "r") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city:")

for pozycja in data[1:]:
    if pozycja[0] == city:
        print(pozycja[1])
