feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Tryna strike a chord its prolly a minorrrrrr")
else:
    print("Kid unable for Drake")
