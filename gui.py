import functions

import FreeSimpleGUI as slim_shady

label = slim_shady.Text("Type to add, show, edit, tick off or exit: ")
input_box = slim_shady.InputText(tooltip="Enter a to-do: ", key="to-do")
add_button = slim_shady.Button("Add")
list_box = slim_shady.Listbox(values=functions.get_todos("userdatafiles/todos.txt"),
                              key="to-dos",
                              enable_events=True,
                              size=[45, 5])
edit_button = slim_shady.Button("Edit")
window = slim_shady.Window("To-DoWave", layout=[[label], [input_box, add_button], [list_box, edit_button]],
                           font=("Helvetica", 18))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos("userdatafiles/todos.txt")
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.writelines_todos("userdatafiles/todos.txt", todos)
            window['to-dos'].update(values=todos)

        case "Edit":
            todos = functions.get_todos("userdatafiles/todos.txt")

            todo_to_edit = values["to-dos"][0]
            new_todo = values["to-do"]
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.writelines_todos("userdatafiles/todos.txt", todos)
            window['to-dos'].update(values=todos)
        case "to-dos":
            window["to-do"].update(value=values['to-dos'][0])
        case slim_shady.WIN_CLOSED:
            break

window.close()
