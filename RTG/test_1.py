import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.font as font

a = {}

f = open('C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\login_info.txt','r+')

def back():
    root.destroy()
    import RTG_automobile_ip


def login():
   
    password = password_entry.get()
    username = mail_entry.get()
    mail = mail1_entry.get()
    L=[]
    
    f.seek(0)
    a = f.read()
    
    if password == '' or mail == '' or username == '':
        messagebox.showinfo(title="Missing Fields!", message="Every Field must be filled in order to proceed!")
        pass
    else:
        b=''
        b+="{'"
        b+=mail
        b+="': ['"
        b+=username
        b+="', '"
        b+=password
        b+="']}"
        print (b)
        if b in a:
            messagebox.showinfo(title="Login Success", message="You have logged in successfully!")
            root.destroy()
            import car_brand


#{'tharun': ['123', '222']}

root = tk.Tk()
root.title("Login Form")

aaa=11
bbb=1+1
width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

print (width1,height1)

root.geometry("%dx%d" % (width1, height1))
frame = Frame(root,height = height1, width = width1).place(x=0,y=0)

'''
canvas1 = Canvas(root, width=width1, height=height1)
canvas1.pack(fill='both', expand=True)

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\ewwcity.png')
canvas1.create_image(0,0, image=bg, anchor='nw')

canvas1.create_text(170,40, text="Mail:", font=("Copperplate Gothic Bold", 20), fill="white")
canvas1.create_text(width1/2,250, text="Password:", font=('Franklin Gothic Demi', 70, 'bold'), fill='White')
canvas1.create_text(width1/2,320, text="Forgot password", font=('Franklin Gothic Demi', 20), fill='white')
'''

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\porsche white bg.png')


frame = Frame(root,height = height1, width = width1,bg='White').place(x=0,y=0)
test_label1 = Label(root, image=bg).place(x=0,y=0)

mail_label = tk.Label(root, text="Name:" , font = ("Arial" , 50), bg='#ffffff')
mail_entry = tk.Entry(root , font = ("Arial" , 50))

mail1_label = tk.Label(root, text="User Number:" , font = ("Arial" , 50), bg='#ffffff')
mail1_entry = tk.Entry(root , font = ("Arial" , 50))

password_label = tk.Label(root, text="Password:" , font = ("Arial" , 50), bg= '#ffffff')
password_entry = tk.Entry(root, show="*" , font = ("Arial" , 50))

heading_label = tk.Label(root, text="Login:", font =("Arial" , 50), bg='#ffffff')
heading_label.grid(row=1,column=1)
login_button = tk.Button(root, text="Login", command=login, font = ("Arial",20))

mail1_label.grid(row=2, column=0) 
mail1_entry.grid(row=2, column=1)
mail_label.grid(row=3, column=0)
mail_entry.grid(row=3, column=1)

password_label.grid(row=4, column=0)
password_entry.grid(row=4, column=1)

login_button.grid(row=5, column=1)

back_button = tk.Button(root, text = 'back', command = lambda: back(), font = ("Arial",20))
back_button.grid(row=6, column=1)
root.mainloop()

