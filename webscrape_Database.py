# removed urllib.request per stackoverflow
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

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})


# ------ commenting this out .... replacing with create database
#filename = "products.csv"
#f = open(filename, "w")






#headers = "brand, product_name, shipping\n"

#f.write(headers)


#for container in containers:
#	brand = container.div.div.a.img["title"]

#	title_container = container.findAll("a", {"class":"item-title"})
#	product_name = title_container[0].text

#	shipping_container = container.findAll("li", {"class":"price-ship"})
#	shipping = shipping_container[0].text.strip()

#	print("brand: " +brand)
#	print("product_name: " +product_name)
#	print("shipping: " +shipping)


	#f.write(brand + "," +product_name.replace(",", "|") + "," + shipping + "\n")

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS GraphicsCards(Brand1 TEXT, Product_Name1 TEXT, Shipping1 TEXT)')


def dynamic_data_entry():
	brand_dyn = container.div.div.a.img["title"] # made container containers
	prod_name_dyn = title_container[0].text
	ship_dyn = shipping_container[0].text.strip() 
	c.execute("INSERT INTO GraphicsCards VALUES(Brand1, Product_Name1, Shipping1) VALUES (?, ?, ?, ?)", (brand_dyn, prod_name_dyn, ship_dyn))
	conn.commit()

create_table()
for i in range(10):
	dynamic_data_entry()
c.close()
conn.close()

