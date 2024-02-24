import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select Files to compress:")
input1 = sg.Input()
input_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
input_button2 = sg.FolderBrowse("Choose", key="folder")





compress_button = sg.Button("Compress")
label3 = sg.Text(key="output", text_color="green")

window = sg.Window(title="Zip File", layout=[[label1, input1, input_button1],
                                            [label2, input2, input_button2],
                                            [compress_button, label3]])

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event is None:
        break
    print(event, values)
    #Selecting muliples files
    filepaths = values["files"].split(";")
    #Select an empty folder for the files to be compressed into
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")
    
window.close()