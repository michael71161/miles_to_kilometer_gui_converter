from tkinter import * 

def milesto_km():
    miles = float(miles_input.get() )
    km = round( miles * 1.609 , 3)
    
    km_result_label.config(text = f"{km}")

window=Tk()
window.title("Miles to KMs converter")
window.config(padx=20 , pady=20) #adding some padding to the window

#widgets creation 

#we are using entry to create input entries to get data from user
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# we are giving a label to the entry which will be located near the 
#entry box

# then we will add grid to each of them to position them on the screen

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equals to ")
is_equal_label.grid(column=0, row=1)
km_result_label = Label(text = "0")
km_result_label.grid(column=1, row=1)
km_label = Label(text = "KM")
km_label.grid(column=2, row=1)


convert_button = Button(text = "convert", command=milesto_km)
convert_button.grid(column=1, row=2)








window.mainloop()