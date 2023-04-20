from tkinter import *
from tkinter import Tk
import tkinter
root = Tk()


def show_choice(event):

    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    label.config(text=value)


label = Label(root, text="Selecciona un elemento de la lista")
label.pack()


lista = ['PHP', 'PYTHON', 'JAVA', 'c#', 'JAVASCRIPT']

lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(root, listvariable=lista_items)
listbox.bind('<<ListboxSelect>>', show_choice)
listbox.pack()

root.mainloop()
