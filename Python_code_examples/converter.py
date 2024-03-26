import PySimpleGUI as sg
from decoupling import convert

sg.theme('black')
label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key='inches')

convert_button = sg.Button("Convert", pad=((0, 10), 0))
exit_button = sg.Button('Exit', pad=((0, 10), 0))
meter_amount = sg.Text(key='amount', justification='right')

layout = [[label1, input1],
          [label2, input2],
          [convert_button, exit_button, meter_amount]]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()
    if event == "Convert":
        try:
            feet_input = values['feet']
            inch_input = values['inches']
            result = convert(feet_input, inch_input)
            result_str = str(result) + 'm' 
            window['amount'].update(result_str)
        except ValueError:
            sg.popup('Please enter two numbers.')
    elif event == "Exit" or event == sg.WINDOW_CLOSED:
        break

window.close()
