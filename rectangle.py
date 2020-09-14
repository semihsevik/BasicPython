#Kullanıcıdan alınan bilgilerle dikdörtgen çizimi

longEdge = int(input("Uzun kenar: "))
shortEdge = int(input("Kısa kenar: ")) 

for row in range(1 , shortEdge + 1):
    for col in range(1 , longEdge + 1):

        if row == 1:
            print("*" , end = " ")
        
        elif row == shortEdge:
            print("*" , end = " ")
            
        elif col == 1 or col == longEdge:
            print("*" , end = " ")S
        
        else: 
            print(" " , end = " ")
    
    print()


    
