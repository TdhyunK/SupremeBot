#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk
import ttk
from Tkinter import *
from productClass import *
from ShoppingFunctions import *
from FootLockerFunctions import *

class SupremeBot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent
        self.initialize()

    # Initialize European Site
    def initialize(self):

        self.grid()

        welcomeText = StringVar()
        self.welcomeLabel = Label(self, textvariable=welcomeText, bd="10", font=(NONE, 16, "bold"), anchor=CENTER)
        welcomeText.set("Welcome to HypeBot.")
        self.welcomeLabel.grid(column=0, row=0)

        self.SupremeButton = tk.Button(self, text=u"Supreme")
        self.SupremeButton.bind("<Button-1>", self.US_initialize)
        self.SupremeButton.grid(column=0, row=1)

        self.Footlockerbutton = tk.Button(self, text=u"Footlocker, Champs, Footaction")
        self.Footlockerbutton.bind("<Button-1>", self.FootLocker_Initialize)
        self.Footlockerbutton.grid(column=1, row=1)

        self.grid_columnconfigure(0, weight=1)

    def add_product(self, event):
        productURL = self.url.get()
        productSize = self.size.get()

        # print "URL : " + productURL
        # print "Size: " + productSize

        # newProd = productClass(productURL, productSize)
        # print newProd.getURL()

        if productSize == "None" or productSize == "NONE":
            print "NO SIZE"
            newProduct = productClass(productURL)
            print "GET URL: " + newProduct.getURL() + "GET SIZE : " + newProduct.getSize()
        else:
            print "SIZE"
            newProduct = productClass(productURL, productSize)
            print "GET URL: " + newProduct.getURL() + "GET SIZE : " + newProduct.getSize()


        self.productList.append(newProduct)
        self.productURLList.append(newProduct.getURL())
        productList = tk.Label(self, text="\n".join(map(str, self.productURLList)))
        productList.grid(column=0, row=15)


        print "ProdList Size: " + str(len(self.productList))

    def US_initialize(self, event):

        self.Footlockerbutton.grid_forget()

        self.productList = []
        self.productURLList = []
        self.grid()

        #EU_Button
        self.EU_button = tk.Button(self, text=u"Europe")
        self.EU_button.bind("<Button-1>", self.EU_initialize)
        self.EU_button.grid(column=1, row=3)

        #US_Button
        self.US_button = tk.Button(self, text=u"USA")
        self.US_button.bind("<Button-1>", self.US_initialize)
        self.US_button.grid(column=2, row=3)

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

    def EU_initialize(self, event):

        self.Footlockerbutton.grid_forget()

        self.productList = []
        self.productURLList = []
        self.grid()

        #EU_Button
        self.EU_button = tk.Button(self, text=u"Europe")
        self.EU_button.bind("<Button-1>", self.EU_initialize)
        self.EU_button.grid(column=1, row=3)

        #US_Button
        self.US_button = tk.Button(self, text=u"USA")
        self.US_button.bind("<Button-1>", self.US_initialize)
        self.US_button.grid(column=2, row=3)


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

        self.postcode = tk.Entry(self)
        self.postcode.delete(0, None)
        self.postcode.insert(0, "Post Code")
        self.postcode.grid(column=0, row=11, sticky='EW')

        self.country = tk.Entry(self)
        self.country.delete(0, None)
        self.country.insert(0, "Country")
        self.country.grid(column=0, row=12, sticky='EW')

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

    def FootLocker_Initialize(self, event):



        self.Footlockerbutton.grid_forget()

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
        self.add2.insert(0, "Address Line 2 - Optional")
        self.add2.grid(column=0, row=8, sticky='EW')

        self.add3 = tk.Entry(self)
        self.add3.delete(0, None)
        self.add3.insert(0, "Address Line 3 - Optional")
        self.add3.grid(column=0, row=9, sticky='EW')

        self.city = tk.Entry(self)
        self.city.delete(0, None)
        self.city.insert(0, "City")
        self.city.grid(column=0, row=10, sticky='EW')

        # self.state = tk.Entry(self)
        # self.state.delete(0, None)
        # self.state.insert(0, "State")
        statevar = StringVar()
        self.state_box = ttk.Combobox(self, textvariable=statevar)
        self.state_box.bind("<<ComboboxSelected>>", self.stateSelect)
        statevar.set("State afsdkflkasjdlkfjla;sdjklfjalj")
        self.state_box['values'] = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" )

        # self.state = tk.Combobox(self, textvariable=statevar)
        self.state_box.grid(column=0, row=11, sticky="EW")

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

        self.expyear = tk.Entry(self)
        self.expyear.delete(0, None)
        self.expyear.insert(0, "Card Expiration Date")
        self.expyear.grid(column=1, row=7, sticky='EW')

        self.cvv = tk.Entry(self)
        self.cvv.delete(0, None)
        self.cvv.insert(0, "Card CVV Number")
        self.cvv.grid(column=1, row=8, sticky='EW')

        shipping = "1 Business Day"
        self.purchase = tk.Button(self, text=u"Purchase Items")
        self.purchase.bind("<Button-1>", lambda event: self.checkout(driver, self.productList, self.name.get().split()[0], self.name.get().split()[1],
                                                            self.email.get(), self.tel.get(), self.add1.get(), self.postcode.get(), self.city.get(), self.state,
                                                            self.country.get(), self.cardnum.get(), self.expmonth.get(), self.expyear.get(), self.cvv.get(), shipping ,self.add2.get()))
        self.purchase.grid(column=0, row=14)

        self.grid_columnconfigure(0, weight=1)

    def checkout(self, driver, productList, firstName, lastName, email, tel, address1, zip, city, state, country, ccNum, ccMonth,
                           ccYear, cvv, shipping, address2=None):
        for product in productList:
            print "checkoutLoop"
            FootLockerAddToCart(product)

        FootLockerCheckout(driver, firstName, lastName, email, tel, address1, zip, city, state, country, ccNum, ccMonth, ccYear, cvv, shipping, address2=None)

    # State Selector
    def stateSelect(self, event):
        self.state=self.state_box.get()
        print "State: " + self.state

if __name__ == "__main__":
    app = SupremeBot(NONE)
    # Background process to check for annoying popup boxes
    # background_thread = Thread(target=popUpBoxCheck, args=(driver,))
    # background_thread.daemon = True
    # background_thread.start()
    app.mainloop()
