import PySimpleGUI

text_feet = PySimpleGUI.Text("Enter feet:")
input_feet = PySimpleGUI.Input(key="feet")

text_inches = PySimpleGUI.Text("Enter inches:")
input_inches = PySimpleGUI.Input(key="inches")

button_convert = PySimpleGUI.Button("Convert")
button_exit = PySimpleGUI.Button("Exit")

result_of_convert = PySimpleGUI.Text(key="result")

left_column_content = [[text_feet],
                       [text_inches]]
left_column = PySimpleGUI.Column(left_column_content)

right_column_content = [[input_feet],
                        [input_inches]]
right_column = PySimpleGUI.Column(right_column_content)

main_window = PySimpleGUI.Window("Convertor, hehe.",
                                 layout=[[left_column, right_column],
                                         [button_exit, button_convert, result_of_convert]])

while True:
    event, values = main_window.read()

    match event:
        case "Convert":
            try:
                feet = float(values['feet'] or 0)
                inches = float(values['inches'] or 0)
                meters = feet * 0.3048 + inches * 0.0254
                meters_rounded = round(meters, 2)
                main_window["feet"].update(value="")
                main_window["inches"].update(value="")
                main_window["result"].update(value=f"{int(feet)} feet and {int(inches)} inches "
                                                   f"are equal to {meters_rounded} meter(s)")
            except ValueError:
                main_window["result"].update(value="Invalid input. Please enter a valid number.")
                main_window["feet"].update(value="")
                main_window["inches"].update(value="")

        case "Exit":
            main_window.close()
            break
