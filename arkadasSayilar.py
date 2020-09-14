#Kendisi hariç bölenlerinin toplamını bulan fonksiyon
def sumOfDivisors(num):
    sum = 0
    for i in range(1 , num):
        if num % i == 0:
            sum += i
    return sum

#Pythonda emoji kullanımı için https://home.unicode.org/ sitesini ziyaret edebilirsiniz.
kalp_emoji = "\U0001f495"

num1 = int(input("Sayı 1: "))
num2 = int(input("Sayı 2: "))

sum1 = sumOfDivisors(num1)
sum2 = sumOfDivisors(num2)

if sum1 == num2 and sum2 == num1: 
    print(f"{num1} {kalp_emoji} {num2} arkadaş sayılardır.")




    
