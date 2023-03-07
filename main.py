import PySimpleGUI as sg
from math import nan
import random

password = "If you see this text, this is a bug. Report it in the issues"
lenght_pass = 1
lenght_pass_raw = "2"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"

sg.theme('DarkTanBlue')
layout1 = [  [sg.Text('Password lenght...')],
            [sg.Slider(range=(4,12),
         default_value=8,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12), key="-LE-")],
            [sg.Text('This password can have:')],
            [sg.Checkbox('numbers', key="-NU-", default=True)],
            [sg.Checkbox('symbols', key="-SY-", default=True)],
            [sg.Button('Ok'), sg.Button('Cancel')]
            ]
#layout2 = [[sg.Text('Your password is')],[sg.Text(password)]]

window1 = sg.Window('Password maker v1.2', layout1)
#----------------------------------------------------------------
#event, values = window1.read()
#lenght_pass_raw = values["-LE-"]
#lenght_pass = int(lenght_pass_raw)
#Full_string = lower_case + upper_case
#if values["-NU-"] == True:
#    Full_string = Full_string + numbers
#if values["-SY-"] == True:
#    Full_string = Full_string + symbols
#lenght_pass = int(lenght_pass_raw)
#password = "".join(random.sample(Full_string, lenght_pass))
#layout2 = [[sg.Text('Your password is')],[sg.Text(password)]]
#window1 = sg.Window('Output', layout2, margins=(50, 50))
#----------------------------------------------------------------
while True:
    event, values = window1.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window1 or clicks cancel
        break
    elif event == 'Ok':
        lenght_pass_raw = values["-LE-"]
        lenght_pass = int(lenght_pass_raw)
        Full_string = lower_case + upper_case
        if values["-NU-"] == True:
            Full_string = Full_string + numbers
        if values["-SY-"] == True:
            Full_string = Full_string + symbols
        lenght_pass = int(lenght_pass_raw)
        password = "".join(random.sample(Full_string, lenght_pass))
        layout2 = [[sg.Text('Your password is')],[sg.Text(password)]]
        window1 = sg.Window('Output', layout2, margins=(50, 50))
window1.close()

