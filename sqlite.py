import sqlite3 

#Veritabanı
connection = sqlite3.connect("products.db")
cursor = connection.cursor()

#Veritabanına tablo ekler.
def createTable():
    sql = "CREATE TABLE productsTable (Category TEXT , Name TEXT , Price INT )"
    cursor.execute(sql)
    connection.commit()

#Tabloya ürün ekler.
def addProducts(category , name , price):
    sql = "Insert into productsTable Values(? , ? , ?)"
    cursor.execute(sql , (category , name , price))
    connection.commit()

createTable()
category = input("Kategori: ")
name = input("Ürün Adı: ")
price = int(input("Fiyat: "))

#Kullanıcıdan alınan ürün bilgilerini tabloya ekleyelim.
addProducts(category , name , price)

#DB bağlantısını keser.
connection.close()













































































