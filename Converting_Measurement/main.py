from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)
border_color = Frame(window, background="blue")

input_miles = Entry(width=10, highlightthickness=2)
input_miles.insert(0, "0")
input_miles.config(highlightbackground="blue")
input_miles.grid(column=2, row=0)

Miles = Label(text="Miles")
Miles.grid(column=3, row=0)

Miles = Label(text="is equal to ")
Miles.grid(column=1, row=2)


Miles = Label(text=" Km")
Miles.grid(column=3, row=2)


def button_clicked():
    Miles = Label(text=f"{float(input_miles.get())*1.6}")
    Miles.grid(column=2, row=2)


Click_me = Button(text="Calculate", width=10, command=button_clicked)
Click_me.grid(column=2, row=3, pady=15)

window.mainloop()
