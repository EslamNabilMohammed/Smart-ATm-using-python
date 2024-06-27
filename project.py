import tkinter as Gui
from tkinter import messagebox

# Dictionary containing client information
clients = {
    "215321701332": {"Name": "Ahmed Abdelrazek Mohamed", "Password": "1783", "Balance": 3500166},
    "203659302214": {"Name": "Salma Mohamed Foaad", "Password": "1390", "Balance": 520001},
    "126355700193": {"Name": "Adel Khaled Abdelrahman", "Password": "1214", "Balance": 111000},
    "201455998011": {"Name": "Saeed Amin Elsawy", "Password": "2001", "Balance": 1200},
    "201122369851": {"Name": "Amir Salama Elgendy", "Password": "8935", "Balance": 178933},
    "201356788002": {"Name": "Wael Mohamed khairy", "Password": "3420", "Balance": 55000},
    "203366789564": {"Name": "Mina Sameh Bishoy", "Password": "1179", "Balance": 18000},
    "201236787812": {"Name": "Omnia Ahmed Awad", "Password": "1430", "Balance": 180350}
}

list_id = []
id_index = 0
password_index = 0
list_pass = [0] * len(clients)  # Track password attempts for each client

def init():
    window = Gui.Tk()
    window.title("Welcome to ATM")
    window.configure(background="black")

    label = Gui.Label(window, text="Please enter your account number")
    label.place(x=20, y=0)
    reading = Gui.Entry(window)
    reading.place(x=20, y=30)
    my_variable = Gui.StringVar()  # The options of radio button are strings

    def check_id():
        id = reading.get()
        list_id.append(id)
        if id in clients:
            password()
        else:
            global password_index
            if list_pass[password_index] >= 2:
                messagebox.showwarning("Not valid", "Blocked account. Go to bank.")
                Exit()
            else:
                messagebox.showwarning("Not valid", "Please enter a valid ID.")
                Exit()

    def check_password():
        password0 = reading.get()
        if clients[list_id[id_index]]["Password"] == password0:
            create_radio()
        else:
            global password_index
            if list_pass[password_index] < 3:
                messagebox.showwarning("Incorrect Password", "Incorrect password")
                list_pass[password_index] += 1
                reading.delete(0, Gui.END)
                if list_pass[password_index] == 3:
                    messagebox.showwarning("Account blocked", "Account blocked. Go to bank.")
                    del clients[list_id[id_index]]
                    Exit()
            else:
                messagebox.showwarning("Account blocked", "Account blocked. Go to bank.")
                Exit()

    def password():
        label.configure(text="Please enter the password")
        reading.delete(0, Gui.END)
        reading.configure(show="*")
        button.configure(command=check_password)

    def create_radio():
        reading.destroy()
        button.destroy()
        label.destroy()
        Gui.Radiobutton(window, text="Cash Withdraw", variable=my_variable, value="Cash Withdraw", command=cash_withdraw).place(x=0, y=0)
        Gui.Radiobutton(window, text="Balance Inquiry", variable=my_variable, value="Balance Inquiry", command=Balance_Inquiry).place(x=150, y=0)
        Gui.Radiobutton(window, text="Password Change", variable=my_variable, value="Password Change", command=Password_Change).place(x=0, y=70)
        Gui.Radiobutton(window, text="Fawry Service", variable=my_variable, value="Fawry Service", command=Fawry_Service).place(x=150, y=70)
        Gui.Radiobutton(window, text="Exit", variable=my_variable, value="Exit", command=Exit).place(x=0, y=140)

    def cash_withdraw():
        window.destroy()
        windoW = Gui.Tk()

        def cash_check():
            value = cash.get()
            global id_index
            if int(value) <= clients[list_id[id_index]]["Balance"]:
                if int(value) % 100 == 0 and int(value) <= 5000:
                    clients[list_id[id_index]]["Balance"] -= int(value)
                    messagebox.showwarning("Thank you", "Operation is done")
                    windoW.destroy()
                    id_index += 1
                    global password_index
                    password_index += 1
                    init()
                elif int(value) > 5000:
                    messagebox.showerror("Exceeded value", "You exceed the allowed value per transaction")
                    windoW.destroy()
                    id_index += 1
                    password_index += 1
                    init()
                else:
                    messagebox.showerror("Invalid amount", "Repeat again with a number divisible by 100")
                    windoW.destroy()
                    id_index += 1
                    password_index += 1
                    init()
            else:
                messagebox.showerror("Insufficient balance", "Not sufficient balance")
                windoW.destroy()
                id_index += 1
                password_index += 1
                init()

        Gui.Label(text="Maximum allowed value per transaction is 5000 L.E").place(x=0, y=0)
        cash = Gui.Entry(windoW)
        cash.place(x=0, y=30)
        Gui.Button(windoW, text="OK", command=cash_check).place(x=120, y=30)

    def Balance_Inquiry():
        window.destroy()
        windoW = Gui.Tk()
        global id_index
        messagebox.showwarning(clients[list_id[id_index]]["Name"], clients[list_id[id_index]]["Balance"])
        windoW.destroy()
        id_index += 1
        global password_index
        password_index += 1
        init()

    def Password_Change():
        def check():
            reading1 = first_time.get()
            reading2 = second_time.get()
            global id_index
            if reading1 == reading2 and len(reading1) == 4:
                clients[list_id[id_index]]["Password"] = reading1
                Gui.Label(windoW, text="Password changed").pack()
                windoW.destroy()
                id_index += 1
                global password_index
                password_index += 1
                init()
            else:
                Gui.Label(windoW, text="Repeat the operation").pack()
                windoW.destroy()
                id_index += 1
                password_index += 1
                init()

        window.destroy()
        windoW = Gui.Tk()
        first_time = Gui.Entry(windoW, show="*")
        first_time.pack()
        second_time = Gui.Entry(windoW, show="*")
        second_time.pack()
        Gui.Label(windoW, text="Please enter a password of four numbers only").pack()
        Gui.Button(windoW, text="Verify", command=check).pack()

    def Fawry_Service():
        def phone_number():
            windoW.destroy()
            new_window = Gui.Tk()
            Gui.Label(new_window, text="Please enter your phone number").pack()
            phone_number = Gui.Entry(new_window)
            phone_number.pack()
            Gui.Label(new_window, text="Please enter the recharge amount").pack()
            amount = Gui.Entry(new_window)
            amount.pack()

            def check():
                recharge = amount.get()
                global id_index
                if int(recharge) < clients[list_id[id_index]]["Balance"]:
                    Gui.Label(new_window, text="The operation is done").pack()
                    clients[list_id[id_index]]["Balance"] -= int(recharge)
                    new_window.destroy()
                    id_index += 1
                    global password_index
                    password_index += 1
                    init()
                else:
                    Gui.Message(new_window, text="No sufficient balance").pack()
                    new_window.destroy()
                    id_index += 1
                    password_index += 1
                    init()

            Gui.Button(new_window, text="Verify", command=check).pack()

        window.destroy()
        windoW = Gui.Tk()
        Gui.Label(windoW, text="Fawry Service").pack()
        Gui.Radiobutton(windoW, text="Orange Recharge", variable=my_variable, value="Orange Recharge", command=phone_number).place(x=0, y=0)
        Gui.Radiobutton(windoW, text="Etisalat Recharge", variable=my_variable, value="Etisalat Recharge", command=phone_number).place(x=150, y=0)
        Gui.Radiobutton(windoW, text="Vodafone Recharge", variable=my_variable, value="Vodafone Recharge", command=phone_number).place(x=0, y=70)
        Gui.Radiobutton(windoW, text="We Recharge", variable=my_variable, value="We Recharge", command=phone_number).place(x=150, y=70)

    def Exit():
        window.destroy()
        global id_index
        global password_index
        password_index += 1
        init()

    button = Gui.Button(window, text="Enter", command=check_id)
    button.place(x=150, y=30)

    window.mainloop()

init()
