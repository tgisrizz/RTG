import tkinter as tk
from tkinter import *

root= tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.title("Kia")


root.geometry("%dx%d" % (width1, height1))

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\kia-motors-new-20211718-removebg-preview (1).png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+100+200,y=325+25)

lbl=tk.Label(root,text = "SELECT YOUR SEGMENT" , font = ("Bold Italic",30),bg='white')
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="MPV", variable=choice, value=1 , font = ("Bold Italic", 20),bg = 'white')
radio2 = tk.Radiobutton(root, text="SUV", variable=choice, value=2 , font = ("Bold Italic", 20), bg= 'white')


radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)

def process_choice():

  ch = choice.get()
  if ch == 1:
        root.destroy()
        import kia_MPV_CARENS
        
  elif ch == 2:
        root.destroy()
        import kia_SUV_SELTOS

def back():
     root.destroy()
     import car_brand
button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 20))
button.pack(padx=20 , pady=20)

button1 = tk.Button(root, text="Back", command=lambda: back(), font = ("Bold Italic" , 20))
button1.pack(padx=20 , pady=20)

root.mainloop()
