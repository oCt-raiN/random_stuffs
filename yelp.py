import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

data = [] 
obj = {}
for i in range(0,300,10):
    # print(i)
    target_website = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Iceland%2C+CA%2C+United+States&start="+ str(i)
    # print(target_website)

    resp = requests.get(target_website)
    soup = BeautifulSoup(resp.text,"html.parser")
    allResults = soup.find_all("h3",{"class":"css-1agk4wl"})
    for i in range(0,len(allResults)):
        try:
            lateral_string=allResults[i].find("a",{"class":"css-19v1rkv"}).get('href')
        except:
            lateral_string=None
        resp1 = None
        print(lateral_string, i)
        target_website = "https://www.yelp.com{}".format(lateral_string)
        # print(target_website)
        resp1 = requests.get(target_website).text
        if resp1:
            soup1 = BeautifulSoup(resp1,"html.parser")
            # print(soup)
            url =soup1.find("a",{"class":"css-1idmmu3"}).get('href')
            print(url)
            # url = re.findall("%2F.+\.com",url)[0].replace("%2F%2F","")
        else:
            continue