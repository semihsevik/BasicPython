# Girilen sayının asal olup olmadığını bulan program.

number = int(input("Enter a number: "))
count = 0

if number <= 0:
    print("Please enter a positive number.")

else:
    for i in range(1, number):
        if number % i == 0:
            count += 1

    if count == 1:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is not a prime number.")

sehirler = ["Ankara" , "İzmir" , "İstanbul" , "Kocaeli"]

for sehir in sehirler:
    #Tüm şehirleri yazdıralım.
    print(sehir)

"""number = int(input("Enter a number: "))
flag = True

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        flag = False
        break

if flag:
    print(f"{number} is a prime number.")"""





