python
list_id=[]
id_index=0
password_index=0
import tkinter as Gui
from tkinter import messagebox
names={"215321701332":{"Name":"Ahmed Abdelrazek Mohamed","Password":"1783","Balance":3500166},"203659302214":{"Name":"Salma Mohamed Foaad","Password":"1390","Balance":520001},
         "126355700193":{"Name":"Adel Khaled Abdelrahman","Password":"1214","Balance":111000},"201455998011":{"Name":"Saeed Amin Elsawy","Password":"2001","Balance":1200},
         "201122369851":{"Name":"Amir Salama Elgendy","Password":"8935","Balance":178933},"201356788002":{"Name":"Wael Mohamed khairy","Password":"3420","Balance":55000},
         "203366789564":{"Name":"Mina Sameh Bishoy","Password":"1179","Balance":18000},"201236787812":{"Name":"Omnia Ahmed Awad","Password":"1430","Balance":180350}}  
new_clients=clients.copy()  
def init():
    window=Gui.Tk()
    window.title("welcom to ATM")
    window.configure(background="black")
    
    label=Gui.Label(window,text="please enter your account number")
    label.place(x=20,y=0)
    reading=Gui.Entry(window)
    reading.place(x=20,y=30)
    my_variable=Gui.StringVar() #the options of radi button is string
#here we take reading from the entry and then check if the reading is an id that exist in dictionary so after check id we call another funcation to destroy reading and delete entry content to get the password
    def check_id():
        id=reading.get()
        list_id.append(id)
        if id="215321701332" and id in clients:
            password()
        elif id=="203659302214" and id in clients:
            password()
        elif id=="126355700193"and  id in clients:
            password()
        elif id=="201455998011" and id in clients:
            password()
        elif id=="201122369851" and id in clients:
            password()
        elif id=="201356788002" and id in clients :
            password()
        elif id=="203366789564" and id in clients :
            password()
        elif id=="201236787812" and id in clients :
            password()    
        else:
            if list_pass[password_index]>=2:
                messagebox.showwarning("Not valid","blocked account go to bank")
                Exit()
            else:
                messagebox.showwarning("Not valid","please enter a right id")
                Exit();
                
            
# this funcation to check password but in addition to check  a certain password of certain id so we should use and 
    def check_password():
#here we get the password and check the password of certain id that we get from the first entry
        password0=reading.get()
        if(new_clients["215321701332"]["Password"]==password0 and list_id[id_index]=="215321701332"):
            create_radio() 
        elif(new_clients["203659302214"]["Password"]==password0 and list_id[id_index]=="203659302214"):
            create_radio() 
        elif(new_clients["126355700193"]["Password"]==password0 and list_id[id_index]=="126355700193"):
            create_radio() 
        elif(new_clients["201455998011"]["Password"]==password0 and list_id[id_index]=="201455998011"):
            create_radio() 
        if(new_clients["201122369851"]["Password"]==password0 and list_id[id_index]=="201122369851"):
            create_radio() 
        elif(new_clients["201356788002"]["Password"]==password0 and list_id[id_index]=="201356788002"):
            create_radio() 
        elif(new_clients["203366789564"]["Password"]==password0 and list_id[id_index]=="203366789564"):
            create_radio() ;
        elif(new_clients["201236787812"]["Password"]==password0 and list_id[id_index]=="201236787812"):
             create_radio() 
        else:
            new_reading=reading.get()
            if list_pass[password_index]<3 and (clients[list_id[id_index]]["Password"]!=new_reading):
                messagebox.showwarning("Incorrect Password","incorrect password")
                list_pass[password_index]+=1
                iterator=list_pass[password_index]
                reading.delete(0,Gui.END)
                new_reading=reading.get()
                if(list_pass[password_index]=3 and iterator<4 ):
                    messagebox.showwarning("account blocked","account blocked go bank")
                    clients.pop(list_id[id_index])
                    
                elif list_pass[password_index]<3 and clients[list_id[id_index]]["Password"]==new_reading:
                    create_radio()
    button=Gui.Button(window,text="enter",command=check_id)
    button.place(x=150,y=30)
# destroy label and create a new one to enter the password then delete entry content
    def password():
        label.configure(text="")
        label.config(text="please enter the password")
        reading.delete(0,Gui.END)
        reading.configure(show="*")
        button.configure(command=check_password)
    def create_radio():
        reading.destroy()
        button.destroy()
        label.destroy()
        Gui.Radiobutton(window,text="Cash Withdraw",variable=my_variable,value="Cash Withdraw",command=cash_withdraw).place(x=0,y=0)
        Gui.Radiobutton(window,text="Balance Inquiry",variable=my_variable,value="Balance Inquiry",command=Balance_Inquiry).place(x=150,y=0)
        Gui.Radiobutton(window,text="Password Change",variable=my_variable,value="Password Change",command=Password_Change).place(x=0,y=70)
        Gui.Radiobutton(window,text="Fawry Service",variable=my_variable,value="Fawry Service",command=Fawry_Service).place(x=150,y=70)
        Gui.Radiobutton(window,text="Exit",variable=my_variable,value="Exit",command=Exit).place(x=0,y=140)
    def cash_withdraw():
        window.destroy()
        windoW=Gui.Tk()    
        def cash_check():
            value=cash.get()
            global id_index
            #here we are dealing with the new window
            if  int(value)<=clients[list_id[id_index]]["Balance"] :
                if int(value) %100==0 and (int(value)<=5000):
                    clients[list_id[id_index]]["Balance"]-=int(value)
                    messagebox.showwarning("Thank you","operation is done")
                    windoW.destroy()
                    id_index+=1
                    global password_index
                    password_index+=1
                    init()
                elif (int(value)>5000):
                    messagebox.showerror("you exess the allowed value per one transaction","you exess the allowed value per one transaction")
                    windoW.destroy()
                    id_index+=1
                    password_index+=1
                    init()
                else:
                    messagebox.showerror("repaet again by a number duplicated by 100","repaet again by a number duplicated by 100")
                    windoW.destroy()
                    id_index+=1
                    password_index+=1
                    init()
            else:
                messagebox.showerror("Not sufficient balance","Not sufiicient balacne")
                #here we should go to home page
                windoW.destroy()
                id_index+=1
                
                password_index+=1
                init()
        Gui.Label(text="Maximum allowed value per transaction is 5000 L.E").place(x=0,y=0)
        cash=Gui.Entry(windoW)
        cash.place(x=0,y=30)
        Gui.Button(windoW,text="ok",command=cash_check).place(x=120,y=30)
    def Balance_Inquiry():
        window.destroy()
        windoW=Gui.Tk()
        global id_index
        #here we should go to home page with button
        messagebox.showwarning(clients[list_id[id_index]]["Name"],clients[list_id[id_index]]["Balance"])
        windoW.destroy()
        id_index+=1
        global password_index
        password_index+=1
        init()
    def Password_Change():
        #error
        def check():
            reading1=first_time.get()
            reading2=second_time.get()
            global id_index
            if(reading1==reading2 and len(reading1)==4):
                clients[list_id[id_index]]["Password"]=reading1
                Gui.Label(windoW,text="password changed").pack()
                windoW.destroy()
                id_index+=1
                global password_index
                password_index+=1
                init()
            else:
                Gui.Label("rebeat the operation").pack()
                windoW.destroy()
                id_index+=1
            
                password_index+=1
                init()
        window.destroy()
        windoW=Gui.Tk()
        first_time=Gui.Entry(windoW,show="*")
        first_time.pack()
        second_time=Gui.Entry(windoW,show="*")
        second_time.pack()
        Gui.Label(windoW,text="please enter a password of four numbers only").pack()
        Gui.Button(windoW,text="verify",command=check).pack()
    def Fawry_Service():
        def phone_number():
            windoW.destroy()
            new_window=Gui.Tk()
            Gui.Label(new_window,text="please enter your phone number").pack()
            phone_number=Gui.Entry(new_window)
            phone_number.pack()
            Gui.Label(new_window,text="please enter the recharge amount").pack()
            amount=Gui.Entry(new_window)
            amount.pack()
            def check():
                recharge=amount.get()
                global id_index
                if(int(recharge)<clients[list_id[id_index]]["Balance"]):
                    Gui.Label(new_window,text="the operation is done").pack()
                    clients[list_id[id_index]]["Balance"]-=int(recharge)
                    new_window.destroy()
                    id_index+=1
                    global password_index
                    passwordindex+=1
                    init()
                else:
                    Gui.Message(new_window,text="No sufficient balance").pack()
                    new_window.destroy()
                    id_index+=1
                    
                    password_index+=1
                    init();
                    
            button=Gui.Button(new_window,text="verify",command=check).pack()
    
       
        
        window.destroy()
        windoW=Gui.Tk()
        Gui.Label(windoW,text="Fawry Service").pack()
        Gui.Radiobutton(windoW,text="Orange Recharge",variable=my_variable,value="Orange Recharge",command=phone_number).place(x=0,y=0)
        Gui.Radiobutton(windoW,text="Etisalat Recharge",variable=my_variable,value="Etisalat Recharge",command=phone_number).place(x=150,y=0)
        Gui.Radiobutton(windoW,text="Vodafone Recharge",variable=my_variable,value="Vodafone Recharge",command=phone_number).place(x=0,y=70)
        Gui.Radiobutton(windoW,text="We Recharge",variable=my_variable,value="We Recharge",command=phone_number).place(x=150,y=70)
    def Exit():
        window.destroy()
        global id_index
  
        global password_index
        password_index+=1
        init()
       
init()