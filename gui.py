import functions

import FreeSimpleGUI as slimshady

label = slimshady.Text("Type to add, show, edit, tick off or exit: ")
input_box = slimshady.InputText(tooltip="Enter a to-do: ", key="to-do")
add_button = slimshady.Button("Add")

window = slimshady.Window("To-DoWave", layout=[[label], [input_box, add_button]],
                          font=("Helvetica", 18))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos("userdatafiles/todos.txt")

            todos.append(values["to-do"] + "\n")

            functions.writelines_todos("userdatafiles/todos.txt", todos)

            print("The to-do has been added to your to-do list!")
        case slimshady.WIN_CLOSED:
            break



window.close()
