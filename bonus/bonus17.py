import FreeSimpleGUI as fein
import zipextractor

fein.theme("Black")

label = fein.Text("Select archive: ")
input1 = fein.Input()
choose_button1 = fein.FileBrowse("Choose File", key="archive")

label2 = fein.Text("Select destination directory:")
input2 = fein.Input()
choose_button2 = fein.FolderBrowse("Choose Destination", key="folder")

extract_button = fein.Button("Extract")
output_label = fein.Text(key="output")

window = fein.Window("File Compressor", layout=([label, input1, choose_button1],
                                                  [label2, input2, choose_button2],
                                                  [extract_button, output_label]))
while True:
    event, values = window.read()
    filepath = values["archive"]
    folder = values["folder"]
    zipextractor.extract_archive(filepath, folder)
    window["output"].update("Extraction completed!", text_color="Green")


window.close()
