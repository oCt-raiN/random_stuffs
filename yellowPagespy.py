import pandas as pd
import requests
from bs4 import BeautifulSoup
data=[]
obj={}
for i in range(0,100):
    try:
        target_website = "https://www.yellowpages.com/search?search_terms=Florists&geo_location_terms=sweden&page="+str(i)
        # target_website = "https://www.yellowpages.com.sg/?select=Restaurants&lp_s_loc=&lp_s_tag=&lp_s_cat=1098&s=home&post_type=listing"  

        resp = requests.get(target_website)
        soup=BeautifulSoup(resp.text, 'html.parser')
        allResults = soup.find_all("div",{"class":"result"})
        for i in range(0,len(allResults)):
            try:
                lateral_string=allResults[i].find("a",{"class":"business-name"}).get('href')
            except:
                lateral_string=None
            target_website = 'https://www.yellowpages.com{}'.format(lateral_string)
            print(lateral_string)
            resp = requests.get(target_website).text
            soup=BeautifulSoup(resp, 'html.parser')
            try:
                obj["Website"]=soup.find("p",{"class":"website"}).find("a").get("href")
            except:
                obj["Website"]=None
            try:
                obj["Email"]=soup.find("a",{"class":"email-business"}).get('href').replace("mailto:","")
            except:
                obj["Email"]=None
            try:
                obj["Contact"]=soup.find("a",{"class":"phone dockable"}).get('href').replace("tel: ","")
            except:
                obj["Contact"]=None
            data.append(obj)
            obj={}
    except:
        continue
df=pd.json_normalize(data)
print(df)
df.to_csv("sweden_florists.csv")
