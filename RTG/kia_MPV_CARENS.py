import tkinter as tk
from tkinter import *

root = tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.geometry("%dx%d" % (width1, height1))

def create_horizontal_table(root, data):
    
    headers = ["VARIANT", "ENGINE", "GEAR",'BOOT SPACE','GROUND CLREARANCE','DIFFERENTIATING FEATURE','PRICE']
    for i, header in enumerate(headers):
        header_label = tk.Label(root, text=header, font=('Helvetica', 12, 'bold'),bg='white')
        header_label.grid(row=0, column=i, padx=10, pady=5)


    for row_idx, car_data in enumerate(data):
        for col_idx, value in enumerate(car_data):
            cell_label = tk.Label(root, text=value, font=('Helvetica', 12),bg='white')
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=10, pady=5, sticky='w')

    
    


car_data = [
    ["carens premium ", "1.0 TSI,113 KW power , 178 Nm Torque", "automatic","521 L","179 mm", "fog light, Air conditioner , air purifier","11.34 L"],
    ["carens prestige ", "1.0 TSI,105 KW power , 178 Nm Torque","automatic","412 L","167 mm", "fog light , wireless charging","12.22 L"],
    ["carens luxury", "1.5 TSI,110 KW power , 180 Nm Torque","automatic","551 L","168 mm", "fog light , wireless charging, sun roof","13.1 L"],
    ["carens luxury plus", "2 TSI,120 KW power , 185 Nm Torque","automatic","545 L","155 mm", "fog light , wireless charging","13.99 L"],
    
]



root.title("Kia MPV")


bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\Kia-Carens-Clear-White-removebg-preview.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+300,y=325+25-200+100+10)



create_horizontal_table(root, car_data)




root.mainloop()

