import tkinter as tk
from tkinter import messagebox
 

f = open('RTG_acc_file.csv','r+')



def login():
   
    password = password_entry.get()
    mail = mail_entry.get()

    if mail == "ragav" and password == "password":
        
        root.destroy()
        
        messagebox.showinfo(title="Login Successful", message="You have successfully logged in.")
        import car_brand
        
        
    else:
        messagebox.showerror(title="Login Failed", message="Invalid id or password.")

root = tk.Tk()
root.title("Login Form")
root.geometry("1000x3000")
mail_label = tk.Label(root, text="mail:" , font = ("Arial" , 50))
mail_entry = tk.Entry(root , font = ("Arial" , 50))

password_label = tk.Label(root, text="Password:" , font = ("Arial" , 50))
password_entry = tk.Entry(root, show="*" , font = ("Arial" , 50))

login_button = tk.Button(root, text="Login", command=login)

mail_label.grid(row=0, column=0)
mail_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
