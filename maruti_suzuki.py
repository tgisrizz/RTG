import tkinter as tk

root= tk.Tk()

root.title("Maruti Suzuki")


root.geometry("1000x1000")
lbl=tk.Label(root,text = "SELECT YOUR SEGMENT" , font = ("Bold Italic",30))
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Hatchback", variable=choice, value=1 , font = ("Bold Italic", 20))
radio2 = tk.Radiobutton(root, text="SUV", variable=choice, value=2 , font = ("Bold Italic", 20))
radio3 = tk.Radiobutton(root, text="Sedan", variable=choice, value=3 , font = ("Bold Italic", 20))
radio4 = tk.Radiobutton(root, text="MPV", variable=choice, value=4 , font = ("Bold Italic", 20))

radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)
radio3.pack(padx=20 , pady=20)
radio4.pack(padx=20 , pady=20)




root.mainloop()
