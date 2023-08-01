import tkinter as tk 
import random as r
from tkinter import messagebox
import csv


bank_id = 0
k = True


root2 = tk.Tk()
root2.title("Sign Up Form")
root2.geometry("1000x1000")


pwd = tk.Label(root2, text="Password:" ,font = ("Arial",20))
pwd_entry = tk.Entry(root2, show="*")

pwd1 = tk.Label(root2, text=" Re-enter Password:" ,font = ("Arial",20))
pwd1_entry = tk.Entry(root2, show="")

mail = tk.Label(root2, text="Mail id:" , font = ("Arial",20))
mail_entry = tk.Entry(root2)

mail.pack(padx=20 , pady=20)
mail_entry.pack(padx=20 , pady=20)

pwd.pack(padx=20 , pady=20)
pwd_entry.pack(padx=20 , pady=20)

pwd1.pack(padx=20 , pady=20)
pwd1_entry.pack(padx=20 , pady=20)



def new_login():
    pwd_value = pwd_entry.get()
    pwd1_value = pwd1_entry.get()
    mail_value = mail_entry.get()
    
    if pwd_value == pwd1_value:
        flag = True
        pass
    else:
        flag = False
        pass

    value1 = mail_value
    value2 = pwd_value

    filename = 'RTG_acc_file.csv' 

    if flag:
        with open (filename , 'a' , newline='') as file:
           writer = csv.writer(file)
           writer.writerow([value1,value2])
           
        root2.destroy()
        messagebox.showinfo(title="Sign up Successful", message="Login to your new account.")
        import existing_user

login_button = tk.Button(root2, text="confirm", command=new_login , font = ("Arial",20))



login_button.pack(padx=20 , pady=20)



root2.mainloop()

