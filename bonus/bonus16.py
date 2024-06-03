import FreeSimpleGUI as hawwww
import zipcreator

label = hawwww.Text("Select files to compress:")
input1 = hawwww.Input()
choose_button1 = hawwww.FilesBrowse("Choose Files", key="files")

label2 = hawwww.Text("Select destination folder:")
input2 = hawwww.Input()
choose_button2 = hawwww.FolderBrowse("Choose Destination", key="folder")

compress_button = hawwww.Button("Compress")
output_label = hawwww.Text(key="output")

window = hawwww.Window("File Compressor", layout=([label, input1, choose_button1],
                                                  [label2, input2, choose_button2],
                                                  [compress_button, output_label]))
while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zipcreator.make_archive(filepaths, folder)
    window["output"].update("The file has been compressed!", text_color="Blue")


window.close()
