import PySimpleGUI as sg

label1 = sg.Text("Select Files to compress:")
input1 = sg.Input()
input_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
input_button2 = sg.FilesBrowse("Choose")



compress_button = sg.Button("Compress")
window = sg.Window(title="Zip File", layout=[[label1, input1, input_button1],
                                            [label2, input2, input_button2],
                                            [compress_button]])
window.read()
window.close()