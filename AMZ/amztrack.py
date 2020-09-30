import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.message import EmailMessage
import time

while(True):

    CHROMEDRIVER = r"C:\Users\KEV\AppData\Local\Temp\Temp2_chromedriver_win32.zip\chromedriver"
    URL = "https://www.amazon.com/gp/product/B087N4ZRXV"

    product_id = 'productTitle'
    price_id = 'priceblock_ourprice'
    image_url_id = 'landingImage'

    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(CHROMEDRIVER, options=options)
    driver.get(URL)


    product_title = driver.find_element_by_id(product_id).text
    try:
        product_price = driver.find_element_by_id(price_id).text[1:]
    except:
        product_price = None
    product_image_url = driver.find_element_by_id(image_url_id).get_attribute('src')

    '''print(product_title)
    print(product_price)
    print(product_image_url)'''

    MAX_PRICE = '800'


    def check():
        if product_price == None:
            print('NONE')
        elif float(product_price) <= float(MAX_PRICE):
            send_mail()

    def send_mail():
        msg = EmailMessage()
        msg['Subject'] = "Amazon Price Tracker Notification"
        msg['From'] = 'huynguyenkev@gmail.com'
        msg['To'] = 'anh00327@gmail.com, huynguyenkev@gmail.com',
        msg.set_content('Your products is under $' + MAX_PRICE + '\n' + product_title +
                        '\n' + 'New price: $' + product_price + '\n' + 'Link :' + URL)
        '''msg.add_alternative("""
            <!DOCTYPE html>
            <html>
                <body>
                    <h2> Your featured product is under $""" + MAX_PRICE """. Don't miss it out!</h2>
                    <ul>
                    <li><b>Name:</b> """ + product_title + """</li>
                    <li><b>Price:</b> $""" + product_price + """</li>
                    <li><b>URL:</b> """ + URL + """</li>
                    </ul>
                    <img src='""" + product_image_url + """' width="300" height="250">
                    <h2>Curious Coding</h2>
                </body>
            </html>
        """, subtype='html')'''

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login('huynguyenkev@gmail.com', 'Kuguranagaru7')
            smtp.send_message(msg)

    
    check()
    time.sleep(60)