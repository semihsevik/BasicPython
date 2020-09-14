
#Girilen sayının faktöriyelini bulan program.

fact = 1
number = int(input("Sayı: "))
num = number

while num > 0:
    fact *= num
    num -= 1 

print(f"{number}! = {fact}")
                        


