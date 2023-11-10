import tkinter as tk
from tkinter import *

root = tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()


root.geometry("%dx%d" % (width1, height1))

screen_width = width1
screen_height = height1

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\logo.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+100,y=325+25)

x_center = screen_width // 2
y_center = screen_height // 2

# Define the size of the buttons
button_width = 10
button_height = 6

root.title("Available brands")

lbl=tk.Label(root,text = "SELECT YOUR CAR BRAND" , font = ("Bold Italic",30),bg='white')
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()


# Create four buttons and place them in the center
button1 = tk.Button(root, text="Hyundai", width=button_width, height=button_height, command = lambda: hyundai(), padx=10, pady=10)
button2 = tk.Button(root, text="Kia", width=button_width, height=button_height, command = lambda: kia(), padx=10, pady=10)
button3 = tk.Button(root, text="Skoda", width=button_width, height=button_height, command = lambda: skoda(), padx=10, pady=10)
button4 = tk.Button(root, text="Honda", width=button_width, height=button_height,  command = lambda: honda(), padx=10, pady=10)
button5 = tk.Button(root, text="Back", width=button_width, height=button_height,  command = lambda: back(), padx=5, pady=5)

#button1.pack(padx=20 , pady=20)
button1.place(x=200+100, y=300/2+50)
button2.place(x=400+100, y=300/2+50)
button3.place(x=600+100, y=300/2+50)
button4.place(x=800+100 ,y=300/2+50)
button5.place(x=800-100-50-30-20 ,y=600/2+50)

def hyundai():
  root.destroy()
  import hyundai

def kia():
  root.destroy()
  import Kia

def skoda():
  root.destroy()
  import skoda

def honda():
  root.destroy()
  import honda

def back():
  root.destroy()
  import test_1

root.mainloop()
