
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

        window.mainloop()

RefiEval()