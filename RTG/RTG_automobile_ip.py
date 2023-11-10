import tkinter as tk
from tkinter import *
root = tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.title("RTG car dealership online booking")

bg = PhotoImage(file='C:\\Users\\admin\\Downloads\\lamborghini-svj-white-autoart-2-removebg-preview.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+100,y=325)


root.geometry("1000x1000")

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="SIGN IN", variable=choice, value=1 , font = ("Bold Italic", 50), bg='white')
radio2 = tk.Radiobutton(root, text="SIGN UP", variable=choice, value=2 , font = ("Bold Italic" , 50), bg = 'white')

radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)

def process_choice():

  ch = choice.get()
  if ch == 1:
        root.destroy()
        import test_1
        
  elif ch == 2:
        root.destroy()
        import new_user

button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 50))
button.pack(padx=20 , pady=20)
        

root.mainloop()
