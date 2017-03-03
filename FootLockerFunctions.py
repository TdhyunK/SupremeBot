from productClass import *
import Tkinter as tk
from Tkinter import *

class FootLockerBot:
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.initialize_footlocker()



    def initialize_footlocker(self):
        self.SupremeButton.grid_forget()

        self.productList = []
        self.productURLList = []
        self.grid()

        # Product URL
        self.url = tk.Entry(self)
        self.url.delete(0, None)
        self.url.insert(0, "Product URL")

        # Size of Product
        self.size = tk.Entry(self)
        self.size.delete(1, None)
        self.size.insert(1, "Size")

        # Add Product Button
        self.addProduct = tk.Button(self, text=u"Add Product")
        self.addProduct.bind("<Button-1>", self.add_product)

        productList = tk.Label(self, text="\n".join(map(str, self.productList)))
        productList.grid(column=0, row=15)

        # String to separate product info & Payment/billing info
        textSeparator = StringVar()
        self.textSeparatorLabel = Label(self, textvariable=textSeparator, bd="10", font=(NONE, 16, "bold"))
        textSeparator.set("Personal Information. None of this information will be stored.")

        # Add previous labels/entry into grid
        self.url.grid(column=0, row=0, sticky='EW')
        self.size.grid(column=0, row=1, sticky='EW')
        self.addProduct.grid(column=0, row=2)
        self.textSeparatorLabel.grid(column=0, row=3, sticky="EW")

        self.name = tk.Entry(self)
        self.name.delete(0, None)
        self.name.insert(0, "Full name")
        self.name.grid(column=0, row=4, sticky='EW')

        self.email = tk.Entry(self)
        self.email.delete(0, None)
        self.email.insert(0, "Email")
        self.email.grid(column=0, row=5, sticky='EW')

        self.tel = tk.Entry(self)
        self.tel.delete(0, None)
        self.tel.insert(0, "Telephone Number")
        self.tel.grid(column=0, row=6, sticky='EW')

        self.add1 = tk.Entry(self)
        self.add1.delete(0, None)
        self.add1.insert(0, "Address Line 1")
        self.add1.grid(column=0, row=7, sticky='EW')

        self.add2 = tk.Entry(self)
        self.add2.delete(0, None)
        self.add2.insert(0, "Address Line 2")
        self.add2.grid(column=0, row=8, sticky='EW')

        self.add3 = tk.Entry(self)
        self.add3.delete(0, None)
        self.add3.insert(0, "Address Line 3")
        self.add3.grid(column=0, row=9, sticky='EW')

        self.city = tk.Entry(self)
        self.city.delete(0, None)
        self.city.insert(0, "City")
        self.city.grid(column=0, row=10, sticky='EW')

        self.state = tk.Entry(self)
        self.state.delete(0, None)
        self.state.insert(0, "State")
        self.state.grid(column=0, row=11, sticky="EW")

        self.postcode = tk.Entry(self)
        self.postcode.delete(0, None)
        self.postcode.insert(0, "Post Code")
        self.postcode.grid(column=0, row=12, sticky='EW')

        self.country = tk.Entry(self)
        self.country.delete(0, None)
        self.country.insert(0, "Country")
        self.country.grid(column=0, row=13, sticky='EW')

        # Right Side of Personal Info

        self.card = tk.Entry(self)
        self.card.delete(0, None)
        self.card.insert(0, "Card Type")
        self.card.grid(column=1, row=4, sticky='EW')

        self.cardnum = tk.Entry(self)
        self.cardnum.delete(0, None)
        self.cardnum.insert(0, "Card Number")
        self.cardnum.grid(column=1, row=5, sticky='EW')

        self.expmonth = tk.Entry(self)
        self.expmonth.delete(0, None)
        self.expmonth.insert(0, "Card Expiration Month")
        self.expmonth.grid(column=1, row=6, sticky='EW')

        self.expdate = tk.Entry(self)
        self.expdate.delete(0, None)
        self.expdate.insert(0, "Card Expiration Date")
        self.expdate.grid(column=1, row=7, sticky='EW')

        self.cvv = tk.Entry(self)
        self.cvv.delete(0, None)
        self.cvv.insert(0, "Card CVV Number")
        self.cvv.grid(column=1, row=8, sticky='EW')

        self.purchase = tk.Button(self, text=u"Purchase Items")
        self.purchase.grid(column=0, row=14)

        self.grid_columnconfigure(0, weight=1)

def newFootLockerBot(event):
    return FootLockerBot(None)