import tkinter as tk
from tkinter import *



def create_horizontal_table(root, data):
    
    headers = ["VARIANT", "ENGINE", "GEAR",'MILEAGE','BOOT SPACE','GROUND CLREARANCE','DIFFERENTIATING FEATURE','PRICE']
    for i, header in enumerate(headers):
        header_label = tk.Label(root, text=header, font=('Helvetica', 12, 'bold'), bg='white')
        header_label.grid(row=0, column=i, padx=10, pady=5)


    for row_idx, car_data in enumerate(data):
        for col_idx, value in enumerate(car_data):
            cell_label = tk.Label(root, text=value, font=('Helvetica', 12),bg='white')
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=10, pady=5, sticky='w')

    
    


car_data = [
    ["creta EX", "1.0 TSI,113 KW power , 178 Nm Torque", "automatic","20","521 L","179 mm", "fog light, Air conditioner , air purifier","11.34 L"],
    ["creta S ", "1.0 TSI,105 KW power , 178 Nm Torque","automatic", "22","412 L","167 mm", "fog light , wireless charging","12.22 L"],
    ["creta SX", "1.5 TSI,110 KW power , 180 Nm Torque","automatic", "18","551 L","168 mm", "fog light , wireless charging, sun roof","13.1 L"],
    ["creta SX plus", "2 TSI,120 KW power , 185 Nm Torque","automatic", "23","545 L","155 mm", "fog light , wireless charging","13.99 L"],
    
]

def back():
    root.destroy()
    import hyundai


root = tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

bg = PhotoImage(file='C:\\Users\\admin\\Downloads\\creta-su2-design-deep-forest-m-removebg-preview.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=150+200,y=325)

button = tk.Button(root, text="Back", command=lambda: back(), font = ("Bold Italic" , 20))
button.grid(row=8, column=4, padx=10, pady=10)

root.geometry("%dx%d" % (width1, height1))

root.title("hyundai SUV")






create_horizontal_table(root, car_data)




root.mainloop()

