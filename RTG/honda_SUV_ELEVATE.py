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
    ["Elevate SV", "1.5 i-VTEC with VTC,89 KW power", "manual","15.31","458 L","220 mm", "fog light, Air conditioner, air purifier","11.08 L"],
    ["Elevate V", "1.5 i-VTEC with VTC,89 KW power","manual", "15.31","458 L","220 mm", "fog light , wireless charging","12.19 L"],
    ["Elevate VX", "1.5 i-VTEC with VTC,89 KW power","manual", "15.31","458 L","220 mm", "fog light , wireless charging, sun roof","13.58 L"],
    ["Elevate ZX", "1.5 i-VTEC with VTC,89 KW power","manual", "15.31","458 L","220 mm", "fog light , wireless charging, sun roof , nitro booster","14.98 L"],
    ["Elevate V", "1.5 i-VTEC with VTC,89 KW power", "Automatic","16.92","458 L","220 mm", "fog light, Air conditioner , air purifier","13.29 L"],
    ["Elevate VX", "1.5 i-VTEC with VTC,89 KW power", "Automatic","16.92","458 L","220 mm", "fog light, Air conditioner , air purifier , sun roof","14.69 L"],
    ["Elevate ZX", "1.5 i-VTEC with VTC,89 KW power", "Automatic","16.92","458 L","220 mm", "fog light, Air conditioner , air purifier , sun roof ","16.08 L"],
    
]



root = tk.Tk()

width1= root.winfo_screenwidth()               
height1= root.winfo_screenheight()

root.geometry("%dx%d" % (width1, height1))

screen_width = width1
screen_height = height1

bg = PhotoImage(file='C:\\Users\\admin\\OneDrive\\Desktop\\vs rtg x goat\\RTG\\slazzer-edit-image.png')
frame = Frame(root,height = height1, width = width1,bg='white').place(x=0,y=0)
test_label1 = Label(root, image=bg, bg = 'white').place(x=100+300,y=325+25-200+100+10)

root.title("honda SUV")






create_horizontal_table(root, car_data)




root.mainloop()

