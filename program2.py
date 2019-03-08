#Importing GUI library
import PySimpleGUI as sg


#GUI Decoration
layout = [[sg.Text('Monthly Loan Repayment Calculator', size=(30, 1), font=("Arial", 25), justification='center', text_color='black')], #title
          #[sg.Text('Vishal Sharma - vs200 / 189034637', font=("Arial", 8), )], #sub-title
          [sg.Text('Loan Amount', size=(18,1), justification='left'), sg.InputText('')], #Loan amount + textbox
          [sg.Text('Interest Rate (decimal)', size=(17,1), justification='left'), sg.InputText('', size=(10,1)), #Interest Rate + textbox
            sg.Text('Repayment duration', size=(15,1), justification='left'), sg.InputText('', size=(10,1)),
            sg.Radio('Months', "RADIO1", default=True), sg.Radio('Years', "RADIO1")], #Duration + textbox
          [sg.Text('_' * 100, size=(70, 1))], #line divider
          [sg.Submit(button_color=('white', 'green')), sg.Cancel(button_color=('white', 'firebrick3'))]] #buttons


#Main Program
while True: #Keep application open

    main_window= sg.Window('Financial Information Systems - Assignment 2', auto_size_text=True,
                              default_element_size=(40, 1)).Layout(layout)    # Assigning Header and variable name to the window

    event, values = main_window.Read()  # Reading user input data from GUI text boxes

    #print(event,values)    #for debugging purpose
    if event is None or event == 'Cancel': #No input / Cancel -> Quit
       break



    main_window.Close()
    #Else perform calculations
    user_input = values

    #Empty inputs + Input validation
    if user_input[0] == '' or user_input[1] == '' or user_input[2] == '' or user_input[0].isalpha() or user_input[1].isalpha() or user_input[2].isalpha():
        sg.Popup('Input Error')
        break

    # variable initialization + data type conversion
    principal = int(user_input[0])
    rate = float(user_input[1])
    duration = int(user_input[2])
    if user_input[3] is False:   #Duration entered in years
        duration = duration * 12
    print(principal,rate,duration)
    payment = []
    principal_paid = []
    interest_paid = []
    loan_balance = []
    data = []

    #Main calculation
    for i in range(0,duration): #for number of months
        payment.append((((rate/12)*principal)*(1+(rate/12))**duration)/(((1+(rate/12))**duration)-1)) #payment calculation
        principal_paid.append(payment[i]/((1+(rate/12))**(1+duration-(i+1)))) #principal calculation
        interest_paid.append(payment[i]-principal_paid[i]) #interest calculation
        loan_balance.append((interest_paid[i]/(rate/12))-principal_paid[i]) #loan balance calculation
        #data.append(str(i)+','+str(payment[i])+','+str(principal_paid[i])+','+str(interest_paid[i])+','+str(loan_balance[i]))
        list=[(i+1),round(payment[i],2),round(principal_paid[i],2),round(interest_paid[i],2),round(loan_balance[i],2)] #To get list of each rows
        data.append(list) #appending rows in to single list
    #print(data)    #enabled for deubgging


    # function to output table
    def table_function(a):
        header_list = ['Payment No', 'Payment Amount', 'Principal Paid', 'Interest Paid', 'Loan balance']   #headers
        data_1 = a   #data is passed as parameter

        # table decoration
        sg.SetOptions(element_padding=(0, 0))
        layout = [[sg.Table(values=data_1,
                 headings=header_list,
                 max_col_width=25,
                 auto_size_columns=True,
                 justification='center',
                 alternating_row_color='lightblue',
                 num_rows=min(len(data_1),20))],
                  [sg.Exit()]]

       # show output
        window = sg.Window('Table', grab_anywhere=False).Layout(layout)
        event, values = window.Read()
        if event is None or event == 'Exit':
            window.Close() #Close table window on exit
        window.Close()
    table_function(data)  #calling function