import FreeSimpleGUI as hawwww

label = hawwww.Text("Select files to compress:")
input1 = hawwww.Input()
choose_button1 = hawwww.FilesBrowse("Choose Files")

label2 = hawwww.Text("Select destination folder:")
input2 = hawwww.Input()
choose_button2 = hawwww.FolderBrowse("Choose Destination")

compress_button = hawwww.Button("Compress")

window = hawwww.Window("File Compressor", layout= ([label, input1, choose_button1],
                                                   [label2, input2, choose_button2],
                                                   [compress_button]))
window.read()
window.close()
