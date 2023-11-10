import tkinter as tk
from tkinter import *

root= tk.Tk()


width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()


root.title("Honda")


lbl=tk.Label(root,text = "SELECT YOUR SEGMENT" , font = ("Bold Italic",30),bg='white')
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()

bg = PhotoImage(file='C:\\Users\\admin\\Downloads\\honda_logo_png_3_5443-removebg-preview (1).png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)

lbl=tk.Label(root,text = "SELECT YOUR SEGMENT" , font = ("Bold Italic",30),bg='white')
lbl.pack(padx=20 , pady =20)
radio1 = tk.Radiobutton(root, text="Sedan", variable=choice, value=1 , font = ("Bold Italic", 20),bg='white')
radio2 = tk.Radiobutton(root, text="SUV", variable=choice, value=2 , font = ("Bold Italic", 20),bg='white')

test_label1 = Label(root, image=bg, bg = 'white').place(x=150+200+100+40+20+20,y=525)

root.geometry("%dx%d" % (width1, height1))

######################################## add enter button

button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 20))
button.place(x=650, y = 150*2+60)

button1 = tk.Button(root, text="Back", command=lambda: back(), font = ("Bold Italic" , 20))
button1.place(x=650, y = 150*2+80*2-20)


radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)


def back():
     root.destroy()
     import car_brand

def process_choice():

  ch = choice.get()
  if ch == 1:
        root.destroy()
        import honda_SEDAN_CITY
        
  elif ch == 2:
        root.destroy()
        import honda_SUV_ELEVATE

'''button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 50))
button.grid(row=8, column=3)'''

root.mainloop()
