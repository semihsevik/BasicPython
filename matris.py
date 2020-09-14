import numpy as np
print()
row = int(input("Satır sayısı: "))
col = int(input("Sütun sayısı: "))
elements = list()

for i in range(row):
    for j in range(col):
        element = int(input("Element: "))
        elements.append(element)

mat = np.array(elements).reshape(row,col)
maxElement = np.amax(mat)
result = np.argwhere(mat == maxElement)[0]
maxRow , maxCol = result[0] , result[1]

print(f"\n******* Matris *******\n{mat}")
print(f"\nEn büyük: {maxElement}\nKonumu: {maxRow , maxCol}")


print()






















