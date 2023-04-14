import pandas as pd
import requests 
from bs4 import BeautifulSoup


product_name=[]
Prices=[]
Description=[]
Ratings=[]
for i in range(0,8):
 url= "https://www.flipkart.com/search?q=tablets+under+20000&sid=tyy%2Chry&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tablets+under+20000%7CTablets&requestId=e7275f12-5fcc-4825-b1e0-1198cc102379&as-searchtext=TABLETS+UNDER+20&page="+str(i)

 r= requests.get(url)

 soup = BeautifulSoup(r.text,"lxml")
 box= soup.find("div",class_="_1YokD2 _3Mn1Gg")
 names = box.find_all("div",class_="_4rR01T")
 for i in names:
    name=i.text
    product_name.append(name)
#print(product_name)
 prices= box.find_all("div",class_="_30jeq3 _1_WHN1")
 for i in prices:
    price="Rs "+ i.text.split("₹")[1]
    Prices.append(price)

#print(Prices)

 ratings= box.find_all("div",class_="_3LWZlK")
 for i in ratings:
    rating=i.text
    Ratings.append(rating)

 #print(Ratings)

 descriptions= box.find_all("ul",class_="_1xgFaf")
 for i in descriptions:
    description=i.text
    Description.append(description)

#print(Description)

a= {"product_name":product_name,"ratings":Ratings,"Prices":Prices,"description":Description}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_csv("tablets_under_20k.csv")

