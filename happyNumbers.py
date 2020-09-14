# Mutlu Sayılar 

def isHappyNumber(num):
    sum = 0 
    rem = 0
    while num > 0: 
        rem = num%10;    
        sum += (rem**2);    
        num = num//10; 
    return sum 

while True:
    num = int(input("Sayı: "))

    result = num 

# Result 1'e veya 4'e eşit olduğunda döngüden çıkılır. 
# Herhangi bir adımda result = 4 olursa, bu sayı mutlu sayı olamaz.
# Dolayısıyla bu iki koşulu kontrol edebiliriz.

    while result != 1 and result != 4:
        result = isHappyNumber(result)

    if result == 1 :
        print(f"{num} is a happy number !!!")
        break 

    else: 
        print(f"{num} is not a happy number.")



