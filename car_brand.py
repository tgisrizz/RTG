import tkinter as tk
root = tk.Tk()
root.title("Available brands")
root.geometry("1000x1000")
lbl=tk.Label(root,text = "SELECT YOUR CAR BRAND" , font = ("Bold Italic",30))
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Maruti suzuki", variable=choice, value=1 , font = ("Bold Italic", 20))
radio2 = tk.Radiobutton(root, text="Tata motors", variable=choice, value=2 , font = ("Bold Italic", 20))
radio3 = tk.Radiobutton(root, text="Hyundai", variable=choice, value=3 , font = ("Bold Italic", 20))
radio4 = tk.Radiobutton(root, text="Kia", variable=choice, value=4 , font = ("Bold Italic", 20))
radio5 = tk.Radiobutton(root, text="Skoda", variable=choice, value=5 , font = ("Bold Italic", 20))
radio6 = tk.Radiobutton(root, text="Honda", variable=choice, value=6 , font = ("Bold Italic", 20))
radio7 = tk.Radiobutton(root, text="Volkswagen", variable=choice, value=7 , font = ("Bold Italic", 20))

radio1.pack(padx=15 , pady=15)
radio2.pack(padx=15 , pady=15)
radio3.pack(padx=15 , pady=15)
radio4.pack(padx=15 , pady=15)
radio5.pack(padx=15 , pady=15)
radio6.pack(padx=15 , pady=15)
radio7.pack(padx=15 , pady=15)

def process_choice():

  ch = choice.get()
  if ch == 1:
      root.destroy()
      import maruti_suzuki
        
  elif ch == 2:
      root.destroy()
      import tata_motors
  elif ch == 3:
      root.destroy()
      import hyundai
  elif ch == 4:
      root.destroy()
      import Kia

  elif ch == 5:
      root.destroy()
      import skoda

  elif ch == 6:
      root.destroy()
      import honda

  elif ch == 7:
      root.destroy()
      import volkswagen


button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 50))
button.pack(padx=20 , pady=20)


    




root.mainloop()
