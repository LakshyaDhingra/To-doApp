import PySimpleGUI as fein

import zipextractor

import zipcreator

fein.theme("Black")

label1 = fein.Text("Select files to compress:")
input1 = fein.Input()
choose_button1 = fein.FilesBrowse("Choose Files", key="files")

label2 = fein.Text("Select destination folder:")
input2 = fein.Input()
choose_button2 = fein.FolderBrowse("Choose Destination", key="folder")

label3 = fein.Text("Select archive: ")
input3 = fein.Input()
choose_button3 = fein.FileBrowse("Choose File", key="archive")

label4 = fein.Text("Select destination directory:")
input4 = fein.Input()
choose_button4 = fein.FolderBrowse("Choose Destination", key="folder2")

compress_button = fein.Button("Compress")
output_label = fein.Text(key="output")

extract_button = fein.Button("Extract")
output_label2 = fein.Text(key="output2")

window = fein.Window("File Compressor", layout=([label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [compress_button, output_label],
                                                [label3, input3, choose_button3],
                                                [label4, input4, choose_button4],
                                                [extract_button, output_label2]))
while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zipcreator.make_archive(filepaths, folder)
    window["output"].update("The file has been compressed!", text_color="Blue")

    filepath = values["archive"]
    folder = values["folder2"]
    zipextractor.extract_archive(filepath, folder)
    window["output"].update("Extraction completed!", text_color="Green")


window.close()
