import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Time: ", now)
while True:
    # Get user input and strip spaces from it
    user_action = input("Type add, show, edit, tick off or exit: ")
    user_action = user_action.strip()
    # Using if...else loop

    # Adding to-dos
    if user_action.startswith("add") or user_action.startswith("Add"):
        if len(user_action) > 3:
            todo = user_action[4:]

            todos = functions.get_todos("userdatafiles/todos.txt")

            todos.append(todo + "\n")

            functions.writelines_todos("userdatafiles/todos.txt", todos)

            print("The to-do has been added to your to-do list!")
        else:
            todo = input("Enter a to-do: ")
            todos = functions.get_todos("userdatafiles/todos.txt")
            todos.append(todo)

            functions.writelines_todos("userdatafiles/todos.txt", todos)
            print("The to-do has been added to your to-do list!")

        # Showing to-do list
    elif user_action.startswith("show"):
        todos = functions.get_todos("userdatafiles/todos.txt")
        if len(todos) == 0:
            print("Chill, Your to-do list is empty")

        else:
            functions.print_todos()

        # Editing todos if there was a mistake
    elif user_action.startswith("edit"):
        if len(user_action) == 4:
            print("Which todo do you want to edit?")
            print("Pick the number of the todo you want to edit: ")
            todos = functions.get_todos("userdatafiles/todos.txt")
            functions.print_todos()
            try:
                number = int(input("Enter number of the to-do to edit: "))
                number = number - 1
                index_number = todos[number]
                new_todo = input("Enter the new todo: ")
                todos[number] = new_todo + "\n"
                functions.writelines_todos("userdatafiles/todos.txt", todos)

                print("This is how it is now:")
                todos = functions.get_todos("userdatafiles/todos.txt")
                functions.print_todos()
            except IndexError:
                print("Enter a valid number of the to-do to edit!")
                continue

        elif user_action[5:].isdigit():
            try:
                number = int(user_action[5:])
                number = number - 1
                todos = functions.get_todos("userdatafiles/todos.txt")
                index_number = todos[number]
                new_todo = input("Enter the new todo: ")
                todos[number] = new_todo + "\n"
                functions.writelines_todos("userdatafiles/todos.txt", todos)

                print("This is how it is now:")
                todos = functions.get_todos("userdatafiles/todos.txt")
                functions.print_todos()
            except IndexError:
                print("No to-do exists with the number entered, try a different one!")
                continue
        elif len(user_action) > 4 and (str(user_action[5:])):
            text = (user_action[5:])
            todos = functions.get_todos("userdatafiles/todos.txt")
            new_todos = [item.strip("\n") for item in todos]
            for i in new_todos:
                if text.lower() == i.lower():
                    number = new_todos.index(i)
                    new_todo = input("Enter the new todo: ")
                    todos[number] = new_todo + "\n"
                else:
                    print("The to-do entered doesn't exist in the to-do list")
                    break

                functions.writelines_todos("userdatafiles/todos.txt", todos)

                print("This is how it is now:")
                todos = functions.get_todos("userdatafiles/todos.txt")
                functions.print_todos()
        # Completing and checking off todos
    elif user_action.startswith("tick off"):
        if len(user_action) == 8:
            todos = functions.get_todos("userdatafiles/todos.txt")
            functions.print_todos()
            tick_off_number = int(input("Which todo do you want to tick off?, Enter it's number: "))
            try:
                number = tick_off_number
                number = number - 1
                popped = todos.pop(number).strip("\n")
                functions.writelines_todos("userdatafiles/todos.txt", todos)

                print(f"Todo \"{popped}\" was checked off from the To-do list")
                print("This is how it is now:")
                todos = functions.get_todos("userdatafiles/todos.txt")
                functions.print_todos()
            except IndexError:
                print("Enter a valid number of the to-do to check off!")
                continue
        else:
            try:
                number = int(user_action[9:])
                number = number - 1
                todos = functions.get_todos("userdatafiles/todos.txt")
                popped = todos.pop(number).strip("\n")
                functions.writelines_todos("userdatafiles/todos.txt", todos)

                print(f"Todo \"{popped}\" was checked off from the To-do list")
                print("This is how it is now:")
                todos = functions.get_todos("userdatafiles/todos.txt")
                functions.print_todos()
            except IndexError:
                print("No to-do exists with the number entered, try a different one!")
                continue

        # Exiting application
    elif user_action.startswith("exit"):
        break
    else:
        print("The command entered is invalid, try again!")
print("Thank you so much for using the app!")
