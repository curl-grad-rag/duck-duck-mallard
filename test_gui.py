import PySimpleGUI as sg
sg.ChangeLookAndFeel('Reddit')
print("Font: {}".format(sg.POPOUT_WINDOW_FONT))
sg.POPOUT_WINDOW_FONT = 'LucidaSans'
sg.SetOptions(element_padding=(0,0))
print("Font: {}".format(sg.POPOUT_WINDOW_FONT))
layout = [  [sg.Text('Tech File', font='LucidaSans', size=(20,1)), sg.In(key='tech_file'), sg.FileBrowse()],
            [sg.Text('IPF List', font='LucidaSans', size=(20,1)), sg.In(key='ipf_list'), sg.FileBrowse()],
            [sg.Text("\n")],
            # [sg.InputText()],
            # [sg.InputOptionMenu([0, 1, 2,3])],
            [sg.Radio('From file', "RV_USE_CONDITIONS", default=True),
                sg.Radio('Create table', "RV_USE_CONDITIONS", enable_events=True)],
            [sg.Text('Conditions File', font='LucidaSans', size=(20,1)), sg.In(), sg.FileBrowse()],
            [sg.Submit(), sg.Cancel()]]      

window = sg.Window('StatEM', layout, font='LucidaSans')    

event, values = window.read()    
print("values: {}".format(values))
window.close()

# text_input = values[0]    
# sg.popup('You entered', text_input)
headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']  # the text of the headings
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]  # build header layout
input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(20)]
sub_canc = [sg.Submit(), sg.Cancel()]

layout = header + input_rows
layout.append([sg.Text("\n")])
layout.append(sub_canc)

window = sg.Window('Table Simulation', layout, font='Courier 12')
event, values = window.read()
print("values:\n{}".format(values))