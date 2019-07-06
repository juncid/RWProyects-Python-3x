


from tkinter import *

def doOk():
    print("Boton OK seleccionado")

def doCancel():
    print("Boton cancel seleccionado")


window = Tk()

btnOK = Button(window, text="OK", bg='#0B962F', fg='#ffffff', command=doOk)

btnCancel = Button(window, text="Cancel", bg='#960b2d', fg='#ffffff', command=doCancel)

btnOK.grid(row=1, column=1, padx=(2,10), pady=5)
btnCancel.place(x=72, y=5)

window.mainloop()