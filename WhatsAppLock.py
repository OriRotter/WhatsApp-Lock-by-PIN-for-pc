import PySimpleGUI as sg
import os

password = '****'



def login():
    global username,password
    sg.theme("DefaultNoMoreNagging")
    column_to_be_centered = [[sg.Text("Enter the pin:", font=40)],[sg.InputText(key='-pwd-', password_char='*', font=16,enable_events=True)],
            [sg.Button('Ok',bind_return_key=True),sg.Button('Cancel'),sg.Text("Wrong!", font=("Courier New", 9),text_color='red',visible=False,key="_wrong_")]]
    layout = [[sg.VPush()],
              [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
              [sg.VPush()]]
    window = sg.Window(
        "Log in",
        layout,
        size=(200, 125),
        icon='D:\Desktops\Ori\WhatsApp\w.ico'
    )


    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok" or len(values['-pwd-']) == 4:
                if values['-pwd-'] == password:
                    os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
                    break
                else:
                    window['-pwd-'].update('')
                    window['_wrong_'].update(visible=True)
    window.close()

if __name__ == '__main__':
    login()

