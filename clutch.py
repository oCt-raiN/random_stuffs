import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
data=[]
obj={}
for i in range(1):
    try:
        target_website = "https://clutch.co/real-estate?page="+str(i)
        resp = requests.get(target_website)
        soup=BeautifulSoup(resp.text, 'html.parser')
        allResults = soup.find_all("ul",{"class":"directory-list"})

    
    
    
    
    except:
        continue