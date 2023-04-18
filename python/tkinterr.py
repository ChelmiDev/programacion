import tkinter
from tkinter import ttk

root =tkinter.Tk()
""" 
label_saludo = tkinter.Label(root,text='label1',bg='yellow',fg='blue')
label_saludo.pack(ipadx=50,ipady=15,fill='x')

label_adios = tkinter.Label(root,text='label2',bg='red',fg='white')
label_adios.pack(ipadx=100,ipady=100,fill='x')

label3 = tkinter.Label(root,text='label3',bg='red',fg='white')
label3.pack(ipadx=100,ipady=100,fill='x')

label4 = tkinter.Label(root,text='label3',bg='red',fg='white')
label4.pack(ipadx=100,ipady=100,side='left') """

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

username_label = ttk.Label(root,text='Username:')
username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1,row=0, sticky=tkinter.E,padx=5,pady=5)

#etiqueta password
password_label = ttk.Label(root,text='Password:')
password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

#campo password
password_entry = ttk.Entry(root,show='*')
password_entry.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)

#boton
login_button = ttk.Button(root,text='Login')
login_button.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)

root.mainloop()

