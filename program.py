#Importing GUI library
import PySimpleGUI as sg

#GUI Decoration
layout = [[sg.Text('Equal Monthly Loan Repayment Calculator', size=(40, 1), font=("Arial", 20), justification='center', text_color='black')], #title
          #[sg.Text('Vishal Sharma - vs200 / 189034637', font=("Arial", 8), )], #sub-title
          [sg.Text('Loan Amount', size=(18,1), justification='left'), sg.InputText('')], #Loan amount + textbox
          [sg.Text('Interest Rate (decimal)', size=(17,1), justification='left'), sg.InputText('', size=(10,1)), #Interest Rate + textbox
            sg.Text('Repayment duration', size=(15,1), justification='left'), sg.InputText('', size=(10,1)),
            sg.Radio('Months', "RADIO1", key='_RADIO1_', default=True), sg.Radio('Years', "RADIO1")], #Duration + textbox
          [sg.Text('_' * 100, size=(70, 1))], #line divider
          [sg.Submit(button_color=('white', 'green')), sg.Cancel(button_color=('white', 'firebrick3'))]] #buttons

# function to output table
def table_function(a):
    header_list = ['Payment No', 'Payment Amount', 'Principal Paid', 'Interest Paid', 'Loan balance']  # headers
    data_1 = a  #data is passed as parameter

    # table decoration
    sg.SetOptions(element_padding=(0, 0))
    layout2 = [[sg.Table(values=data_1,
                         headings=header_list,
                         max_col_width=25,
                         auto_size_columns=True,
                         justification='center',
                         alternating_row_color='lightblue',
                         num_rows=min(len(data_1), 20))],
               [sg.Cancel()]]
    # show output
    table_window = sg.Window('Table', grab_anywhere=False).Layout(layout2)
    event = table_window.Read()
    table_window.Close() #Close on Exit




#Create a window
main_window = sg.Window('Loan Repayment Calculator', auto_size_text=True,
                        default_element_size=(40, 1)).Layout(layout)
main_window.SetIcon(r"C:\Users\Ramakant\OneDrive - University of Leicester\Financial Services Information\Assignment 2\i.ico")  # Assigning Header and variable name to the window

#Main Program
while True: #Keep application open

    values = main_window.Read()  # Reading user input data from GUI text boxes

    if values[0] is 'Cancel' or values[0] is None: #No input / Cancel -> Quit
       break

    #Else perform calculations
    user_input = values[1]
    print(user_input)

    # variable initialization + data type conversion

    # Empty inputs + Input validation
    try:
        principal = float(user_input[0])
        rate = float(user_input[1])
        duration = int(user_input[2])
        if user_input[3] is True:   #Duration entered in years
            duration = duration * 12
        print(principal,rate,duration)
        input_error = 0

    except: #initialize dummy values and throw error
        principal = 0
        rate = 1
        duration = 1
        input_error = 1
        sg.Popup("Input Error!", "Please check numbers & select radio!")

    #Calculation variables
    payment = []
    principal_paid = []
    interest_paid = []
    loan_balance = []
    data = []

    #Main calculation
    try: #Errors while calculations
        for i in range(0,duration): #for number of months
            payment.append((((rate/12)*principal)*(1+(rate/12))**duration)/(((1+(rate/12))**duration)-1)) #payment calculation
            principal_paid.append(payment[i]/((1+(rate/12))**(1+duration-(i+1)))) #principal calculation
            interest_paid.append(payment[i]-principal_paid[i]) #interest calculation
            loan_balance.append((interest_paid[i]/(rate/12))-principal_paid[i]) #loan balance calculation
            list=[(i+1),round(payment[i],2),round(principal_paid[i],2),round(interest_paid[i],2),round(loan_balance[i],2)] #To get list of each rows
            data.append(list) #appending rows in to single list
    except: #Numbers too big?
        input_error = 1
        sg.Popup("Input Error! Numbers out of range")

    if input_error == 0:
        table_function(data)  # calling function