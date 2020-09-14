#Basit bir hesap makinesi örneği

num1 = float(input("Sayı 1: "))
num2 = float(input("Sayı 2: "))

choice = input("\nİşlem seçiniz\n1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme\n")

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}") 

elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}") 

elif choice == '3':
    print(f"{num1} x {num2} = {round((num1 * num2) , 2)}") 

elif choice == '4':

    # 0' a bölme hatasını "try - except" bloklarıyla yakalayalım.

    try:
        print(f"{num1} / {num2} = {round((num1 / num2) , 2)}") 
    
    except ZeroDivisionError as err:
        print("Bir sayıyı 0' a bölemezsiniz !")
        print(f"Orjinal hata mesajı: {err}")

else: 
    print("Lütfen geçerli bir işlem seçiniz.")


