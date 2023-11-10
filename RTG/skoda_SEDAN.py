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
    ["Slavia ", "1.0 TSI,113 KW power , 178 Nm Torque", "automatic","20","521 L","179 mm", "fog light, Air conditioner , air purifier","13.34 L"],
    ["rapid", "1.0 TSI,105 KW power , 178 Nm Torque","automatic", "22","412 L","167 mm", "fog light , wireless charging","11.22 L"],
    ["superb", "2 TSI,120 KW power , 180 Nm Torque","automatic", "18","551 L","168 mm", "fog light , wireless charging, sun roof","21.1 L"],
    ["octavia", "1.5 TSI,110 KW power , 178 Nm Torque","automatic", "23","545 L","155 mm", "fog light , wireless charging","16.99 L"],
    
]



root = tk.Tk()
root.title("Skoda SEDAN")

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.geometry("%dx%d" % (width1, height1))

screen_width = width1
screen_height = height1

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\skoda_sedan.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+300,y=325+25-200+100+10)

create_horizontal_table(root, car_data)




root.mainloop()

