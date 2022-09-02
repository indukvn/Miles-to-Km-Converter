from tkinter import *
# def btn_clicked():
#     my_label.config(text=input.get())
#
#
# window = Tk()
# window.minsize(width=500, height=300)
# window.title("GUI using tkinter")
# window.config(padx=15, pady=15)
#
# my_label = Label(text="I am a Label", font=("Arial", 20, "bold"))
# my_label.grid(column=0, row=0)
# my_label.config(padx=10, pady=10)
#
# my_btn1 = Button(text="Click me", command=btn_clicked)
# my_btn1.grid(column=1, row=1)
# my_btn1.config(padx=10, pady=10)
#
# my_btn2 = Button(text="Hello")
# my_btn2.grid(column=2, row=0)
# my_btn2.config(padx=10, pady=10)
#
# input = Entry(width=10)
# input.grid(column=3, row=2)
#
# window.mainloop()

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=160)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(iput.get())
    km = round(miles * 1.6, 4)
    label3.config(text=km, fg="green")


iput = Entry(width=10)
iput.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Arial", 12, "bold"))
label1.config(padx=5, pady=5)
label1.grid(column=2, row=0)

label2 = Label(text="is equal to ", font=("Arial", 12, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 15, "bold"))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 12, "bold"))
label4.grid(column=2, row=1)

btn = Button(text="Calculate", background="yellow", font=("Arial", 10, "bold"), border=5, command=miles_to_km)
btn.grid(column=1, row=2)


window.mainloop()
