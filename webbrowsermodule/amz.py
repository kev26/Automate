import bs4, requests

def amzrequest(urlitem):
    res = requests.get(urlitem)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        '< span class="a-size-medium a-color-price header-price" > $17.99 < /span >')
    return elems[0].text.strip()


price = amzrequest(
    'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=')
print ("Item's price is " + price)


# <span id = "priceblock_ourprice" class = "a-size-medium a-color-price priceBlockBuyingPriceString" >$704.00 < /span >
