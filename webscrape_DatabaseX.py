from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import sqlite3

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opening up connecting, grabbing the page
uClient = uReq(my_url)
# this will offload our content into a variable
page_html = uClient.read()
# closes our client
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS GraphicsCards(Brand1 TEXT, Product_Name1 TEXT, Shipping1 TEXT)')

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    cursor.execute("INSERT INTO GraphicsCards VALUES (?, ?, ?)", (brand, product_name, shipping))

conn.commit()
cursor.close()
conn.close()