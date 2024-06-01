password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper-case"] = upper

if all(result.values()):
    print("Strong password")

elif result["length"] == False:
    print("Weak password, the length of the password must be more than 8 characters")

elif result["digits"] == False:
    print("Weak password, the password must contain at least 1 digit")

elif result["upper-case"] == False:
    print("Weak password, the password must contain at least 1 upper-case letter")
else:
    print("Weak password")
