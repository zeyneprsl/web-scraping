import requests #request ile sadece veri çekilebilir
from bs4 import BeautifulSoup
url = requests.get('https://w3schools.com/python/demopage.htm')
if url.status_code ==200: #print(url) cekebiliyosa 200 döner 
     print(f"page is accessible, url.satus code:{url.status_code}")
else:
     print(f"Page not found,url.satus code: {url.status_code}")

x=url.content # suan burası bize urlnin html kodlarını verir
x=url.encoding # karsıladığı dili verir

soup=BeautifulSoup(url.content,"html.parser")
#(soup)
#print(soup.prettify())
#print(soup.title.name)

# sitenin sadece belli bir kısmını çekmek için;
sp=soup.find_all("div") #div tagini bulur
sp=soup.find_all("div",{"class":"the-subtitle"}) # class ismi bu olan div tagini bulur ve bu etiketin kodunu basar
sp=soup.find_all("div",{"class":"the-subtitle"}).text # class ismi bu olan div tagini bulur ve bu etiketteki texti yazar 
#.a deseydin a etkietini basardı
print(sp.get("href")) # bu ise htmlde href içinde tanımlanır link ve linki cekmek istediğinde kullanırsın
