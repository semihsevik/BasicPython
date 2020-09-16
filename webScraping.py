import requests 
from bs4 import BeautifulSoup 

#Siteye bir get isteği gönderip html içeriğini çekelim.
url = "https://www.doviz.com/"
response = requests.get(url)
htmlContent = response.content 

#Bir soup objesi oluşturup html ile parse etmesini isteyelim.
soup = BeautifulSoup(htmlContent , "html.parser")

#İsimleri ve değerleri 'span' etiketinden 'class' isimlerine göre çekelim.
names = soup.find_all("span" , {"class" : "name"})
values = soup.find_all("span" , {"class" : "value"})

#Çektiğimiz verilerin text kısımlarını alarak 'döviz.txt' dosyasına yazalım.
for name , value in zip(names , values):
    name = name.text 
    value = value.text 
    with open("döviz.txt" , "a" , encoding="UTF-8") as file: 
        file.write(f"{name} - {value}\n")


        
