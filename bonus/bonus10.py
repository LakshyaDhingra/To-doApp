try:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    if length == breadth:
        exit("That looks like a square")
    area = length * breadth
    print("Area of rectangle: ", area)
except ValueError:
    print("Please enter a number!")
