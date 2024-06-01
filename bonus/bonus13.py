feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254
    return meters

dict = parse(feet_inches)

result = convert(dict['feet'], dict['inches'])

print(f"{dict['feet']} feet and {dict['inches']} inches is equal to {result} meters")

if result < 1:
    print("Tryna strike a chord its prolly a minorrrrrr")
else:
    print("Kid unable for Drake")
