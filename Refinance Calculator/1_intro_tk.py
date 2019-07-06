


from tkinter import *

window = Tk()
label = Label(window, text="Hola tkinter")
text = Text(window, cnf={'bg': '#007fff'})
button = Button(window, text="Clickeame!")

label.pack()
text.pack()
button.pack()

window.mainloop( )