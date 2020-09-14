#Buble Sort 

def bubbleSort(arr): 
	arrLen = len(arr) 

	for i in range(arrLen - 1): 
		for j in range(0, arrLen-i-1): 

			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [14 , 63 , 56 , 22 , 756 , 29 , 3] 
print("Array:" , arr)

bubbleSort(arr) 

#Sıralanmış listeyi list comprehension yapısı ile oluşturalım.
sortedArr = [i for i in arr] 

print ("Sorted array:" , sortedArr) 



