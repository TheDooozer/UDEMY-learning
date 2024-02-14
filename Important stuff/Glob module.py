#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import glob

myfiles = glob.glob("test/*.txt")

print(myfiles)

for filepath in myfiles:
    with open(filepath, "r") as file:
        result = file.read()
        print(result)
