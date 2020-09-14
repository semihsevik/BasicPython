# Python ile Shell Sort algoritması

def shellSort(arr, n):
    interval = n // 2
    while interval > 0:

        for i in range(interval, n):
            temp = arr[i]
            j = i

            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2

data = list()
print("Dizi elemanlarını giriniz. (Çıkmak için 'q')")

while True:
    element = input()

    if element != 'q':
        data.append(int(element))

    else: break

size = len(data)
shellSort(data, size)
print(f'Girilen dizinin artan şekilde sıralanmış hali --> {data}')








