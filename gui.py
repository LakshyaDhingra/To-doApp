import functions

import FreeSimpleGUI as slimshady

label = slimshady.Text("Type to add, show, edit, tick off or exit: ")
input_box = slimshady.InputText(tooltip="Enter a to-do: ")
add_button = slimshady.Button("Add")

window = slimshady.Window("To-DoWave", layout=[[label], [input_box, add_button]])
window.read()
window.close()
