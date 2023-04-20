
import tkinter
from tkinter import ttk

def select():
    pass
    
root = tkinter.Tk()

def reset():
    pass

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

boton = tkinter.Button(root, text='Resetear')
boton.grid(column=3,row=3,padx=5,pady=5)
boton.bind('<Button-1>',reset)

seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(root, text='Si',value='1', variable=seleccionado)
r2 = ttk.Radiobutton(root, text='No',value='2', variable=seleccionado)
r3 = ttk.Radiobutton(root, text='Quiza',value='3', variable=seleccionado)

r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)







root.mainloop()