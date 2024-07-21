"""
seyahatsever sitesindeki listeden parcalayarak sadece siteleri çekmeye calıstım. 
Sehilerde alt alta bir kaç kere yazılmıştı. onuda düzelltim
"""
import requests 
from bs4 import BeautifulSoup
url = requests.get('https://seyahatsever.gsb.gov.tr/')
if url.status_code ==200: #print(url) cekebiliyosa 200 döner 
     print(f"page is accessible, url.satus code:{url.status_code}")
else:
     print(f"Page not found,url.satus code: {url.status_code}")

soup=BeautifulSoup(url.content,"html.parser")
temp_td_text="temp"
num=1
for row in soup.find("main",{"class":"content"}).find_all("tr"):
    first_td = row.find("td")  #.find_all("li","class": "x") ile yapmak istersen 
    if first_td:
        first_td_text = first_td.text.strip()
        if first_td_text != temp_td_text:
            print(num,"=",first_td_text)
            num=num+1
        temp_td_text = first_td_text