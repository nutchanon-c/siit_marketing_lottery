from cgitb import text
import datetime
import json
import os
import PySimpleGUI as sg
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
currentDir = dir_path.replace('\\', '/')

# read an extract data from config.json
with open(currentDir + "/config.json", 'r', encoding="utf8") as f:
    data = json.loads(f.read())
    backgroundColor = data['backgroundColor']
    textColor = data['textColor']
    labelColor = data['labelColor']







def main():
    with open(currentDir + '/' + 'result_log.txt', 'a') as f:
        f.write('----------Results for ' + str(datetime.datetime.now()) + '----------\n')
        f.close()


    colors = {
        "backgroundColor" :backgroundColor,
        "labelColor" : labelColor,
        "textColor" : textColor,
    }
 

    def resetWindow():
        window['-RANDOMNUMBER-'].update('')
        window['-RANDOMBUTTON-'].update(visible=True)
        window['-RESULTOKBUTTON-'].update(visible=False)
        
    r = False
     
    layout = [   
            
        [
            [
                sg.Text('', size=(10, 5), font=("Helvetica", 0), key='-SPACER-', background_color=colors['backgroundColor'])
            ]
        ],
        [
            [
                [sg.Text('LOTTERY', key='-MEMBERLABEL-', font=('Arial', 20), visible=True, text_color=colors['labelColor'], background_color=colors['backgroundColor'])],
                [sg.Text('', key='-SPACER-', font=('Arial', 25), size=(40,2), justification='c', text_color=colors['textColor'], background_color=colors['backgroundColor'])],
            ]
        ],
        [
            sg.Text(text='', key='-RANDOMNUMBER-', font=('Arial', 80), background_color=colors['backgroundColor'], size=(5,1), justification='c', text_color=colors['textColor']),
        ],
         [
            [
                sg.Text('', size=(10, 5), font=("Helvetica", 0), key='-SPACER-', background_color=colors['backgroundColor'])
            ]
        ],
        [
            
            sg.Button('Random', key='-RANDOMBUTTON-', visible= True, size=(20, 2), button_color='#9907fe'), 
        ],
        [
            sg.Stretch(background_color=colors['backgroundColor']),
            
        ],
        [
            sg.Text('Made by Nutchanon Charnwutiwong',expand_x=True, justification='r', background_color=colors['backgroundColor'],text_color="#000000")
        ]

        
        
        ]
    window = sg.Window(title='Lottery', layout=layout, resizable=False,size=(800,600), element_justification='c', font=('Arial', 11), icon=currentDir + '/icon.ico',titlebar_icon=currentDir + '/icon.ico', background_color=colors['backgroundColor'])
    cnt = 0
    a = 0
    t = 50
    num = 0
    while True:
        if r:
            cnt += 1
            if cnt == 1000/t:
                cnt = 0
                a += 1
                print(a)
            if a == 4: # 5 seconds
                r = False
                window['-RANDOMBUTTON-'].update(visible=True)
                
                with open(currentDir + '/' + "result_log.txt", 'a') as f:
                    f.write(str(num).zfill(3) + '\n')
                    f.close()          
                print('Result', num)
                
        event, values = window.read(timeout=t)
        # continuous random number

            

        if event == sg.WIN_CLOSED:
            break


        if event == '-RANDOMBUTTON-':
            cnt = 0
            a = 0
            r = True
            window['-RANDOMBUTTON-'].update(visible=False)



        if event == '-RESULTOKBUTTON-':
            resetWindow()
            window['-COMBO-'].update(disabled=False)
            r = False
        if r:
            num = random.randint(1,300)
            window['-RANDOMNUMBER-'].update(str(num).zfill(3))
            

if __name__ == '__main__':
    main()
