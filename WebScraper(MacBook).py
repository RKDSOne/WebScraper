from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# my_url = "https://www.amazon.in/gp/search/ref=sr_as_oo?rh=i%3Aaps%2Ck%3Amacbook+air&keywords=macbook+air&ie=UTF8&qid=1504761408"
# my_url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook&rh=i%3Aaps%2Ck%3Amacbook"
my_url = "https://www.amazon.in/s/ref=sr_as_oo?rh=i%3Aaps%2Ck%3Amacbook&keywords=macbook&ie=UTF8&qid=1504762401"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


# html parsing
page_soup = soup(page_html, "html.parser")


# grabs each product
containers = page_soup.findAll("div", {"class":"s-item-container"})


# Creates New File:
fileName = "Products_MacBook.csv"
headers = "Product Name, Current Price, Original Price\n"

f = open(fileName, "w")
f.write(headers)


errorMsg = "Error!"
# obtains the data
for contain in containers:
	try:
		title = contain.h2.text
	except IndexError:
		title =  errorMsg
	except UnicodeEncodeError:
		f.write("\n")
		continue

	print("title: " + title)
	f.write(title.replace(",", "|").replace("/", "|") + ",")


	try:
		priceCurrent = contain.findAll("span", {"class":"a-size-base a-color-price s-price a-text-bold"})
		CurrentSP = priceCurrent[0].text.strip()
	except IndexError:
		CurrentSP =  errorMsg

	print("CurrentSP: " + CurrentSP)
	f.write(CurrentSP.replace(",", "") + ",")


	try:
		priceSuggested = contain.findAll("span", {"class":"a-size-small a-color-secondary a-text-strike"})
		SuggestedSP = priceSuggested[0].text.strip()
	except IndexError:
		SuggestedSP =  errorMsg

	print("SuggestedSP: " + SuggestedSP)
	f.write(SuggestedSP.replace(",", "") + "\n")

f.close()
