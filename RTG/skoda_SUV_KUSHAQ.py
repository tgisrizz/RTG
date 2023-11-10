import tkinter as tk
from tkinter import *


def create_horizontal_table(root, data):
    
    headers = ["VARIANT", "ENGINE", "GEAR",'MILEAGE','BOOT SPACE','GROUND CLREARANCE','DIFFERENTIATING FEATURE','PRICE']
    for i, header in enumerate(headers):
        header_label = tk.Label(root, text=header, font=('Helvetica', 12, 'bold'),bg='white')
        header_label.grid(row=0, column=i, padx=10, pady=5)


    for row_idx, car_data in enumerate(data):
        for col_idx, value in enumerate(car_data):
            cell_label = tk.Label(root, text=value, font=('Helvetica', 12),bg='white')
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=10, pady=5, sticky='w')

    
    


car_data = [
    ["Kushaq Active", "1.0 TSI,85 KW power , 178 Nm Torque", "automatic","20","385 L","155 mm", "fog light, Air conditioner , air purifier","11.59 L"],
    ["Kushaq Ambition", "1.0 TSI,85 KW power , 178 Nm Torque","automatic", "20","385 L","155 mm", "fog light , wireless charging","13.34 L"],
    ["Kushaq style", "1.0 TSI,85 KW power , 178 Nm Torque","automatic", "20","385 L","155 mm", "fog light , wireless charging, sun roof","15.79 L"],
    ["Kushaq Ambition", "1.5 TSI,110 KW power , 250 Nm Torque","automatic", "19","385 L","155 mm", "fog light , wireless charging","14.99 L"],
    ["Kushaq style", "1.5 TSI,110 KW power , 250 Nm Torque","automatic", "19","385 L","155 mm", "fog light , wireless charging, sun roof","17.79 L"],
]



root = tk.Tk()
root.title("Skoda SUV")

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.geometry("%dx%d" % (width1, height1))

screen_width = width1
screen_height = height1

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\skoda-kushaq-removebg-preview.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+300,y=325+25-200+100+10)




create_horizontal_table(root, car_data)




root.mainloop()
