from convertersbonus14 import convert
from parsersbonus14 import parse

feet_inches = input("Enter feet and inches: ")

dictionary = parse(feet_inches)

result = convert(dictionary['feet'], dictionary['inches'])

print(f"{dictionary['feet']} feet and {dictionary['inches']} inches is equal to {result} meters")

if result < 1:
    print("Tryna strike a chord its prolly a minorrrrrr")
else:
    print("Kid unable for Drake")
