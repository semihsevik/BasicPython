#Fibonacci serisi

n = int(input("N sayısı: "))
a = 1
b = 1
fibonacci = [a,b]

for i in range(n - 2):
      
        c = a + b
        
        a,b = b,c  #a ya b yi ata, b ye ise c yi ata demek.
        
        fibonacci.append(c)

for num in fibonacci:
    print(num , end=" ")

























