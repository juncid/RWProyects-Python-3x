
from tkinter import *
import numpy as np

class RefiEval:
    def __init__(self):
        window = Tk()
        window.title("Refinance Evaluator")

        # Loan inputs
        Label(window, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest Rate").grid(row=2, column=1, sticky=W)
        Label(window, text="Term (years)").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1, sticky=W)

        #outputs
        Label(window, text="Payment:").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments:").grid(row=6, column=1, sticky=W)

        #Variable que guarda el input
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

        #Variables para imprimir pmt
        self.pmt = StringVar()
        self.total = StringVar()

        Entry(window, textvariable= self.pv,
              justify=RIGHT).grid(row=1, column=2, padx=(0,5))

        Entry(window, textvariable=self.interest_rate,
              justify=RIGHT).grid(row=2, column=2, padx=(0, 5))

        Entry(window, textvariable=self.term,
              justify=RIGHT).grid(row=3, column=2, padx=(0, 5))

        Label(window, textvariable=self.pmt,
              font="Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2, sticky=E)

        Label(window, textvariable=self.pmt,
              font="Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2, sticky=E)

        window.mainloop()

RefiEval()