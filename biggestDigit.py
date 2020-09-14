
number = input("Sayı: ") 
numOfDigits = len(number)
number = int(number)
digitList = []

for i in range(numOfDigits):
    digit = number % 10
    digitList.append(digit)
    number //= 10 

biggestDigit = max(digitList)

print(biggestDigit)




