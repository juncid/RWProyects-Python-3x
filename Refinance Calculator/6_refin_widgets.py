
from tkinter import *
import numpy as np

class RefiEval:
    def __init__(self):
        window = Tk()
        window.title("Refinance Evaluator")

        # Loan inputs
        Label(window, text="Loan Amount: ", font="Helvetica 16").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest Rate: ", font="Helvetica 16").grid(row=2, column=1, sticky=W)
        Label(window, text="Term (years): ", font="Helvetica 16").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4, column=1, sticky=W)

        #outputs
        Label(window, text="Payment: ", font="Helvetica 16").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments: ", font="Helvetica 16").grid(row=6, column=1, sticky=W)

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
              font="Helvetica 16 bold",
              justify=RIGHT).grid(row=5, column=2, sticky=E)

        Label(window, textvariable=self.total,
              font="Helvetica 16 bold",
              justify=RIGHT).grid(row=6, column=2, sticky=E)

        Button(window, text="Calculate Payment",
               command=self.calcPayment,
               font="Helvetica 14").grid(row=7, column=2, padx=(100, 5), pady=5)

        #Variables de refinanciamiento
        self.old_pmt = StringVar()
        self.timeleft = StringVar()
        self.refi_cost = StringVar()


        Label(window, text="Current Payment",
              font="Helvetica 16").grid(row=8, column=1)

        Label(window, text="Time Remaining",
              font="Helvetica 16").grid(row=9, column=1)

        Label(window, text="Refi Cost",
              font="Helvetica 16").grid(row=10, column=1)


        #Entradas de evaluacion
        Entry(window, textvariable=self.old_pmt,
              justify=RIGHT).grid(row=8, column=2, padx=(0,5))

        Entry(window, textvariable=self.timeleft,
              justify=RIGHT).grid(row=9, column=2, padx=(0,5))

        Entry(window, textvariable=self.refi_cost,
              justify=RIGHT).grid(row=10, column=2, padx=(0,5))

        #Variables de Salida para la evaluacion
        self.monthly_savings = StringVar()
        self.payback = StringVar()
        self.overall_savings = StringVar()

        Label(window, text="Monthly Savings: ",
              font="Helvetica 16").grid(row=11, column=1)

        Label(window, text="Payback in Months: ",
              font="Helvetica 16").grid(row=12, column=1)

        Label(window, text="Overall Savings: ",
              font="Helvetica 16").grid(row=13, column=1)

        Button(window, text="Eval Refi",
               font="Helvetica 14",
               command=self.evalRefi).grid(row=14, column=2)

        window.mainloop()

    def calcPayment(self):
        pv = float(self.pv.get())
        rate = float(self.interest_rate.get())
        term = int(self.term.get())

        pmt = np.pmt(rate / 1200, term * 12, -pv, 0)
        total = pmt * 12 * term

        self.pmt.set("$" + format(pmt, "5,.2f"))
        self.total.set("$" + format(total, "8,.2f"))

    def evalRefi(self):
        pass


RefiEval()