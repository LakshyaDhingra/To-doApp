import functions

import FreeSimpleGUI as slim_shady

import time

slim_shady.theme("Black")

clock = slim_shady.Text(key="clock")
label = slim_shady.Text("Type to add, show, edit, tick off or exit: ")
input_box = slim_shady.InputText(tooltip="Enter a to-do: ", key="to-do")
add_button = slim_shady.Button("Add", size=10)
list_box = slim_shady.Listbox(values=functions.get_todos("userdatafiles/todos.txt"),
                              key="to-dos",
                              enable_events=True,
                              size=[45, 5])
edit_button = slim_shady.Button("Edit", size=10)
complete_button = slim_shady.Button("Complete", size=10)
exit_button = slim_shady.Button("Exit", size=10)

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = slim_shady.Window("To-DoWave", layout=layout,
                           font=("Helvetica", 18))
while True:
    event, values = window.read(timeout=20)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos("userdatafiles/todos.txt")
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.writelines_todos("userdatafiles/todos.txt", todos)
            window['to-dos'].update(values=todos)
            window['to-do'].update(value="")

        case "Edit":
            try:
                todos = functions.get_todos("userdatafiles/todos.txt")
                todo_to_edit = values["to-dos"][0]
                new_todo = values["to-do"]
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.writelines_todos("userdatafiles/todos.txt", todos)
                window['to-dos'].update(values=todos)
            except IndexError:
                slim_shady.popup("Please select an item first!", font=("Helvetica", 17), title="Error!")

        case "Complete":
            todos = functions.get_todos("userdatafiles/todos.txt")

            todo_to_complete = values["to-dos"][0]
            todos.remove(todo_to_complete)
            functions.writelines_todos("userdatafiles/todos.txt", todos)
            window['to-dos'].update(values=todos)
            window['to-do'].update(value="")
        case "Exit":
            break
        case "to-dos":
            window["to-do"].update(value=values['to-dos'][0])
        case slim_shady.WIN_CLOSED:
            break
window.close()
