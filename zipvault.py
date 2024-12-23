import PySimpleGUI as fein

import zipextractor

import zipcreator

fein.theme("Black")

label1 = fein.Text("Select files to compress:")
input1 = fein.Input(key="input1")
choose_button1 = fein.FilesBrowse("Choose Files", key="files")

label2 = fein.Text("Select destination folder:")
input2 = fein.Input(key="input2")
choose_button2 = fein.FolderBrowse("Choose Destination", key="folder")

zip_name_label = fein.Text("Enter zipfile name:")
input_zip_name = fein.Input(key="input_zip")

label3 = fein.Text("Select archive: ")
input3 = fein.Input(key="input3")
choose_button3 = fein.FileBrowse("Choose File", key="archive")

label4 = fein.Text("Select destination directory:")
input4 = fein.Input(key="input4")
choose_button4 = fein.FolderBrowse("Choose Destination", key="folder2")

compress_button = fein.Button("Compress")
output_label = fein.Text(key="output")

extract_button = fein.Button("Extract")
output_label2 = fein.Text(key="output2")

window = fein.Window("File Compressor & Extractor", layout=([label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [zip_name_label, input_zip_name],
                                                [compress_button, output_label],
                                                [label3, input3, choose_button3],
                                                [label4, input4, choose_button4],
                                                [extract_button, output_label2]), font=("Helvetica", 20))
while True:
    try:
        event, values = window.read()
        match event:

            case "Compress":
                filepaths = values["files"].split(";")
                folder = values["folder"]
                zip_name = values["input_zip"]
                zipcreator.make_archive(filepaths, folder, zip_name)
                window["output"].update("The file has been compressed!", text_color="Green")
                window['input1'].update(value="")
                window['input2'].update(value="")
                window["input_zip"].update(value="")

            case "Extract":
                filepath = values["archive"]
                folder2 = values["folder2"]
                zipextractor.extract_archive(filepath, folder2)
                window["output2"].update("Extraction completed!", text_color="Green")
                window['input3'].update(value="")
                window['input4'].update(value="")
            case window.was_closed():
                break
    except ValueError:
        fein.popup("Please select the file/destination first", font=("Helvetica", 17))

window.close()
