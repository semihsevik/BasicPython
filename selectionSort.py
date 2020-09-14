#Python -- Selection Sort

arr = [56, 14, 22, 29, 3 ,1210] 

for i in range(len(arr)): 
	
	#Dizideki min. elemanı bulalım.
	min_idx = i 
	for j in range(i+1, len(arr)): 
		if arr[min_idx] > arr[j]: 
			min_idx = j 
			
    
    #Bulunan minimum elemanı başa alalım.
	arr[i], arr[min_idx] = arr[min_idx], arr[i] 


print ("Sıralanmış Dizi:" , *arr) 











