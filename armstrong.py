#Armstrong sayılar 

#Basamak sayısını dönen fonksiyon
def getNumOfDigits(num):
    numOfDigits = 0
    while num >= 1:
        numOfDigits += 1 
        num //= 10   
    return numOfDigits

#Her basamağı bir listeye alıp, listeyi ters çevirip dönen fonksiyon.
def getAllDigits(num):
    digitList = []
    while num > 0: 
        digitList.append(num % 10)
        num //= 10   
    return digitList[::-1]

#Kullanıcı tarafından Armstrong sayı girilene kadar döner.
while True:
    num = int(input("Sayı: "))

    numOfDigits = getNumOfDigits(num) #Basamak sayısı
    allDigits = getAllDigits(num)     #Basamaklar listesi

    sum = 0
    for digit in allDigits:
        sum += (digit**numOfDigits) 

    if sum == num:
        print(f"{num} bir Armstrong sayısıdır !")
        break

    else:
        print(f"{num} bir Armstrong sayısı değildir !")

        
        
