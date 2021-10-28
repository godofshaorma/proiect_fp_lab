from tkinter import *

# Create windows object

app = Tk()

# Ziua

ziua_text = StringVar()
ziua_label = Label(app, text='Ziua ', font=('bold',16), pady=20)
ziua_label.grid(row=0, column=0, sticky=W)
ziua_entry = Entry(app, textvariable = ziua_text)
ziua_entry.grid(row=0, column=1)

# Suma

suma_text = StringVar()
suma_label = Label(app, text='Suma ', font=('bold',16), pady=20)
suma_label.grid(row=0, column=2, sticky=W)
suma_entry = Entry(app, textvariable = suma_text)
suma_entry.grid(row=0, column=3)


#Lista Cheltuieli

lista_cheltuieli = Listbox(app, height=10, width=100)
lista_cheltuieli.grid(row=3, column=0, columnspan=3,rowspan=6, pady=20, padx=20)

#Create scroll bar

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#Set scroll to listbox

lista_cheltuieli.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista_cheltuieli.yview)

#Buttons

"""add_btn = Button(app, text='Adauga cheltuiala', width=12, command=add_item)
add_btn.grid(row=2, column = 0)

remove_btn = Button(app, text='Sterge cheltuiala', width=12, command=add_item)
remove_btn.grid(row=2, column = 0)"""


app.title('Cheltuieli de familie')
app.geometry('850x450')

# Start program

app.mainloop()