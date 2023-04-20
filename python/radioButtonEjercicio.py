from tkinter import *

root = Tk()

select = StringVar()


languages = [
    ("Python", "Python"),
    ("Perl", "Perl"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("C#", "C#")
]

def show_choice():
    print(select.get())
    
for text, languages in languages:
    Radiobutton(root,text=text,variable=select,value=languages,command=show_choice).pack(anchor=W)
    
Button(root, text="Reiniciar", command=lambda: select.set(None)).pack()


root.mainloop()