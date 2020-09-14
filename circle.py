#Daire alanı hesaplama.

import numpy as np

pi = np.pi

rad = float(input("Yarıçap: "))

perimeter = 2 * pi * rad
area = pi * (rad**2)

print(f"Çevre: {round(perimeter,2)}")
print(f"Alan: {round(area,2)}")





