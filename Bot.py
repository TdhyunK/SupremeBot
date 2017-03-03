from ShoppingFunctions import *
from productClass import *

productList = [productClass("http://www.footlocker.com/product/model:221030/sku:26628608/nike-flyknit-racer-mens", "15.0")]



# productURL = "http://www.supremenewyork.com/shop/tops-sweaters/qtczf2v37"

name = "Thomas Kim"
firstName = "Thomas"
lastName = "Kim"
email = ""
tel = ""
address1 = ""
# address2 = '' #optional address if you have multiple lines
zip = ""
city = ""
state = ""
country = ""
credit_card_type = "Visa"
credit_card_number = ""
exp_month = ""
exp_year = ""
cvv = ""
size = "Medium"
shipping = "1 Business Day"


for product in productList:
    FootLockerAddToCart(product)

FootLockerCheckout(driver, firstName, lastName, email, tel, address1, zip, city, state, country, credit_card_number, exp_month, exp_year, cvv, shipping)
# time.sleep(1)
# if(driver.find_element_by_css_selector("b.in-cart") != None):
#     driver.find_element_by_css_selector("a.checkout").click()
#
# assert "https://www.supremenewyork.com/checkout" in driver.current_url
#
# FootLockerCheckout(driver, name, email, tel, address1, zip, city, state, country, credit_card_type, credit_card_number, exp_month, exp_year, cvv)
