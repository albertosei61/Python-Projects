import PySimpleGUI as sg
from decoupling import convert


label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key='inches')

convert_button = sg.Button("Convert")
meter_amount = sg.Text(key='amount')


layout = [[label1, input1],
         [label2, input2],
         [convert_button, meter_amount]]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()
    if event == "Convert":
        feet_input = values['feet']
        inch_input = values['inches']
        result = convert(feet_input, inch_input)
        result_str = str(result) + 'm' 
        window['amount'].update(result_str)
    if event == sg.WIN_CLOSED:
        break
window.close()
