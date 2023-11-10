import tkinter as tk 
import random as r
from tkinter import *
from tkinter import messagebox
import csv

write_flag = None 

root2 = tk.Tk()

width1= root2.winfo_screenwidth()               
height1= root2.winfo_screenheight()

bank_id = 0
k = True
op = None

bg = PhotoImage(file='C:\\Users\\admin\\Downloads\\bugatti.png')
frame = Frame(root2,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root2, image=bg, bg = 'white').place(x=100+100,y=325+25)

root2.title("Sign Up Form")
root2.geometry("1000x1000")

heading_label = tk.Label(root2, text="Login:", font =("Arial" , 50), bg='white')
heading_label.grid(row=0,column=4)

user_name = tk.Label(root2, text="User Number:", font = ("Arial",30), bg='white')
pwd2_entry = tk.Entry(root2, show="", font = ("Arial" , 30))

pwd = tk.Label(root2, text="Password:" ,font = ("Arial",30), bg='white')
pwd_entry = tk.Entry(root2, show="*", font = ("Arial" , 30))

pwd1 = tk.Label(root2, text=" Re-enter Password:" ,font = ("Arial",30), bg='white')
pwd1_entry = tk.Entry(root2, show="", font = ("Arial" , 30))

mail = tk.Label(root2, text="Name:" , font = ("Arial",30), bg='white')
mail_entry = tk.Entry(root2, font = ("Arial" , 30))

user_name.grid(row=1 , column=3)
pwd2_entry.grid(row=1, column=4)

mail.grid(row=2, column=3)
mail_entry.grid(row=2, column=1+3)

pwd.grid(row=3, column=3)
pwd_entry.grid(row=3, column=1+3)

pwd1.grid(row=4, column=3)
pwd1_entry.grid(row=4, column=4)

def back():
    root2.destroy()
    import RTG_automobile_ip
    pass



def new_login():
    user_name_value = pwd2_entry.get()
    pwd_value = pwd_entry.get()
    pwd1_value = pwd1_entry.get()
    mail_value = mail_entry.get()

    
    if user_name_value == '' or pwd1_value == '' or pwd_value == '' or mail_value == '':
        op = True
        if op:
            messagebox.showinfo(title="Missing field", message="Make sure to fill every field!")
        else:
            pass
    else:
        if pwd1_value != pwd_value:
            messagebox.showinfo(title="Error", message="Password does not match")
            pass
        else:
            flag = True
            pass

    value1 = mail_value
    value2 = pwd_value
    value3 = pwd1_value
    b=''
    b+="{'"
    b+=user_name_value
    b+="': ['"
    b+=mail_value
    b+="', '"
    b+=value2
    b+="']}"

    filename = 'C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\login_info.txt' 

    if flag:
        print ('hi')
        with open (filename , 'r' , newline='') as file:
           abc = file.read()
           print (abc)
           file.seek(0)
           if user_name_value not in abc:
             write_flag = True
             pass
           else:
               messagebox.showinfo(title="User Name error", message="Provided Username already exists, please provide a new User Number for your account!")
        
        if write_flag:
            with open (filename, 'a') as f:
                f.write(b)
            root2.destroy()
            messagebox.showinfo(title="Sign up Successful", message="Login to your new account.")
            import test_1

login_button = tk.Button(root2, text="Confirm", command= lambda: new_login() , font = ("Arial",20))
login_button.grid(row=5, column=4)

back_button = tk.Button(root2, text="Back", command= lambda: back() , font = ("Arial",20))
back_button.grid(row=6, column=4)


root2.mainloop()


