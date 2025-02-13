import functions

import PySimpleGUI as slim_shady

import time

import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

slim_shady.theme("Black")

clock = slim_shady.Text(key="clock")
label = slim_shady.Text("Type to add, show, edit, tick off or exit: ")
input_box = slim_shady.InputText(tooltip="Enter a to-do", key="to-do")
add_button = slim_shady.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add to-do",
                               key="Add")
list_box = slim_shady.Listbox(values=functions.get_todos("todos.txt"),
                              key="to-dos",
                              enable_events=True,
                              size=[45, 5])
edit_button = slim_shady.Button("Edit", size=10)
complete_button = slim_shady.Button(size=2, image_source="complete.png",  mouseover_colors="LightBlue2",
                                    key="Complete")
exit_button = slim_shady.Button("Exit", size=10)

layout = [[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]

window = slim_shady.Window("To-DoWave", layout=layout,
                           font=("Helvetica", 18))
while True:
    event, values = window.read(timeout=100)
    if not window.was_closed():
        window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    else:
        break

    match event:

        case slim_shady.WIN_CLOSED:
            exit()

        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.writelines_todos("todos.txt", todos)
            window['to-do'].update(value="")
            window['to-dos'].update(values=todos)

        case "Edit":
            try:
                todos = functions.get_todos("todos.txt")
                todo_to_edit = values["to-dos"][0]
                new_todo = values["to-do"]
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.writelines_todos("todos.txt", todos)
                window['to-dos'].update(values=todos)
            except IndexError:
                slim_shady.popup("Please select an item first!", font=("Helvetica", 17), title="Error!")

        case "Complete":
            todos = functions.get_todos("todos.txt")

            todo_to_complete = values["to-dos"][0]
            todos.remove(todo_to_complete).
            functions.writelines_todos("todos.txt", todos)
            window['to-dos'].update(values=todos)
            window['to-do'].update(value="")
        case "Exit":
            exit()
        case "to-dos":
            window["to-do"].update(value=values['to-dos'][0])

window.close()
