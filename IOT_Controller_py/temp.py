'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-17 15:11:26
LastEditors: Mar Ping
LastEditTime: 2021-03-22 19:31:38
'''
# import sys,os
# import PySide2

# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# print(plugin_path)

import PySimpleGUI as sg

# with sg.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
#     

#      button, values = form.LayoutAndRead(layout)


# This is a "Traditional" PySimpleGUI window code. First make a layout, then a window, the read it
layout = [
    [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText()],
    [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
    [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything')],
    [sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
        sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
    [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
        sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
        sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
        sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
    [sg.Text('_'  * 100, size=(70, 1))],
    [sg.Text('Choose Source and Destination Folders', size=(35, 1))],
    [sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'), sg.FolderBrowse()],
    [sg.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Dest'),
        sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel(), sg.SimpleButton('Customized', button_color=('white', 'green'))]
        ]


window = sg.Window('Hello world', layout, size=(920,720))
event, values = window.read()

window.close()

