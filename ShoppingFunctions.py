from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import Tkinter
import tkMessageBox
from threading import Thread



from productClass import *
import time

driver = webdriver.Chrome("/Users/thomaskim/Downloads/chromedriver")


# ----------------- Supreme Functions ------------------

def SupremeAddToCart(product, name, email, tel, address1, zip, city, state, country,
              ccType, ccNum, ccMonth, ccYear, cvv, address2 = None ):

    driver.get(product.getURL())



    assert "Supreme" in driver.title

    supremeSizeOptions(driver, product)

    driver.find_element_by_name("commit").click()




def supremeSizeOptions(driver, product):
    if driver.find_element_by_id("size").get_attribute("type") != "hidden":
        # print driver.find_element_by_id("size").get_attribute("type")
        Select(driver.find_element_by_id("size")).select_by_visible_text(product.getSize())


def supremeCheckout(driver, name, email, tel, address1, zip, city, state, country, ccType, ccNum, ccMonth, ccYear, cvv, address2 = None):
    name_form = driver.find_element_by_id("order_billing_name")
    email_form = driver.find_element_by_id("order_email")
    tel_form = driver.find_element_by_id("order_tl")
    address1_form = driver.find_element_by_id("bo")
    zip_form = driver.find_element_by_id("order_billing_zip")
    city_form = driver.find_element_by_id("order_billing_city")
    state_form = driver.find_element_by_id("order_billing_state")
    country_form = driver.find_element_by_id("order_billing_country")
    credit_card_form = driver.find_element_by_id("credit_card_type")
    credit_card_number_form = driver.find_element_by_id("cnb")
    credit_card_month_form = driver.find_element_by_id("credit_card_month")
    credit_card_year_form = driver.find_element_by_id("credit_card_year")
    cvv_form = driver.find_element_by_id("vval")
    paymentButton = driver.find_element_by_css_selector("input.checkout")



    name_form.clear()
    name_form.send_keys(name)

    email_form.clear()
    email_form.send_keys(email)

    tel_form.clear()
    tel_form.send_keys(tel)

    address1_form.clear()
    address1_form.send_keys(address1)

    zip_form.clear()
    zip_form.send_keys(zip)

    city_form.clear()
    city_form.send_keys(city)

    state_form.send_keys(state)

    country_form.send_keys(country)

    credit_card_form.send_keys(ccType)

    credit_card_number_form.clear()
    credit_card_number_form.send_keys(ccNum)

    credit_card_number_form.send_keys(ccMonth)

    credit_card_year_form.send_keys(ccYear)

    cvv_form.clear()
    cvv_form.send_keys(cvv)

    classList = driver.find_elements_by_class_name("iCheck-helper")

    classList[1].click()  # terms and conditions agreement

    # paymentButton.click()

# ----------------- Footlocker --------------------
def FootLockerAddToCart(product):
    # background_thread = Thread(target=popUpBoxCheck, args=(driver,))
    # background_thread.daemon = True
    # background_thread.start()
    size_id = "Size " + str(product.getSize())
    driver.get(product.getURL())

    driver.find_element_by_id("pdp_size_select_mask").click()
    time.sleep(3)

    # Checks if size is in stock
    if FootLockerInStock(size_id):
        #Click the ize
        driver.find_element_by_xpath('//*[@title="' + size_id + '"]').click()
        driver.find_element_by_id("pdp_addtocart_button").click()
    else:
        quit()



def FootLockerCheckout(driver, firstName, lastName, email, tel, address1, zip, city, state, country, ccNum, ccMonth, ccYear, cvv, shipping, address2=None):
    try:
        # # Background process to check for annoying popup boxes
        # background_thread = Thread(target=popUpBoxCheck, args=(driver,))
        # background_thread.daemon = True
        # background_thread.start()

        #click checkout button
        time.sleep(3)
        checkout_id = "View Full Cart Button"
        driver.find_element_by_xpath('//*[@title="' + checkout_id + '"]').click()

        zip_form = driver.find_element_by_id("estimator_zipcode")
        shipping_option_form = driver.find_element_by_id("estimator_shipping")


        zip_form.clear()
        zip_form.send_keys(zip)

        shipping_option_form.send_keys(shipping)

        #redirect to next page for payment info
        # actions = ActionChains(driver)
        # element = driver.find_element_by_id("footer-icons")
        # actions.move_to_element(element).perform();
        time.sleep(2)
        driver.find_element_by_id("cart_checkout_button_bottom").click()
        try:
            firstname_form = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "billFirstName"))
            )
        except TimeoutException:
            print "Page timeout"



        # firstname_form = driver.find_element_by_id("billFirstName")
        lastname_form = driver.find_element_by_id("billLastName")
        address1_form = driver.find_element_by_id("billAddress1")
        address2_form = driver.find_element_by_id("billAddress2")
        zip_form = driver.find_element_by_id("billPostalCode")
        city_form = driver.find_element_by_id("billCity")
        tel_form = driver.find_element_by_id("billHomePhone")
        email_form = driver.find_element_by_id("billEmailAddress")
        cardNum_form = driver.find_element_by_id("CardNumber")
        ccMonth_form = driver.find_element_by_id("CardExpireDateMM")
        ccYear_form = driver.find_element_by_id("CardExpireDateYY")
        cvc_form =driver.find_element_by_id("CardCCV")

        firstname_form.clear()
        firstname_form.send_keys(firstName)

        lastname_form.clear()
        lastname_form.send_keys(lastName)

        address1_form.clear()
        address1_form.send_keys(address1)

        if address2 != None:
            address2_form.clear()
            address2_form.send_keys(address2)

        zip_form.clear()
        zip_form.send_keys(zip)

        city_form.clear()
        city_form.send_keys(city)


        Select(driver.find_element_by_id("billState")).select_by_value(state)

        tel_form.clear()
        tel_form.send_keys(tel)

        email_form.clear()
        email_form.send_keys(email)


        driver.find_element_by_id("billPaneContinue").click()
        time.sleep(3)
        driver.find_element_by_id("shipMethodPaneContinue").click()


        time.sleep(2)
        # cardNum_form.clear()
        cardNum_form.send_keys(ccNum)

        # ccMonth_form.clear()
        ccMonth_form.send_keys(ccMonth)

        # ccYear_form.clear()
        ccYear_form.send_keys(ccYear)

        # cvc_form.clear()
        cvc_form.send_keys(cvv)

        driver.find_element_by_id("payMethodPaneContinue").click()

        # SUBMIT ORDER BUTTON
        # driver.find_element_by_id("orderSubmit").click()

        # paymentButton.click()
    except NoSuchElementException:
        top = Tkinter.Tk()
        top.tkMessageBox.showinfo("Say Hello", "Hello World")
        top.loop()

        print "An Element was not found. Restart the progrma."


def FootLockerInStock(element_id):
    hover(element_id)
    if len(driver.find_elements_by_class_name("in_stock_highlight")) > 0:
        if len(driver.find_elements_by_xpath('//*[@title="' + element_id + '"]')) > 0:

            element = driver.find_element_by_xpath('//*[@title="' + element_id + '"]' )
            return True
    else:
        print "not in stock"
        return False


def FootLockerShipping(shipping_option):
    if shipping_option == "5-6 Business Days":
        Select(driver.find_element_by_id("size")).select_by_value("Z")

    elif shipping_option == "3-4 Business Days":
        Select(driver.find_element_by_id("size")).select_by_value("T")

    elif shipping_option == "2 Business Days":
        Select(driver.find_element_by_id("size")).select_by_value("5")

    elif shipping_option == "1 Business Day":
        Select(driver.find_element_by_id("size")).select_by_value("U")

# --------- Helper Functions -------------


#Hover
def hover(element_id):
    if len(driver.find_elements_by_xpath('//*[@title="' + element_id + '"]' )) > 0:
        element = driver.find_element_by_xpath('//*[@title="' + element_id + '"]' )
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
    else:
        print "size not valid"


#Check for pop-up box

def popUpBoxCheck(driver):
    while True:
        print "loop started but not triggered"
        time.sleep(0.5)
        if len(driver.find_elements_by_class_name("vex-content")) > 0:
            print "triggered"
            driver.find_element_by_class_name("brdialog-close").click()