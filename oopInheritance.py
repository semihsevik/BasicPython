#Parent class
class Polygon:
    def __init__(self, numOfSides):
        self.numOfSides = numOfSides
        self.sides = []
    
    def inputSides(self):
        for i in range(self.numOfSides):
            side = float(input(f"{i+1}. Kenar : "))
            self.sides.append(side)
    
    def displaySides(self):
        for i in range(self.numOfSides):
            print(f"{i+1}. Kenar : {self.sides[i]}")

#Child class
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        longEdge , shortEdge = self.sides
        area = longEdge * shortEdge
        print(f"Dikdörtgenin Alanı : {area}")

obj = Rectangle()

obj.inputSides() 
obj.displaySides()
obj.findArea()
   
print(f"Rectangle, Polygon sınıfının bir alt sınıfıdır: {issubclass(Rectangle , Polygon)}")


# Inheritance (miras alma, kalıtım), bir nesnenin özelliklerinin farklı 
# nesneler tarafından da kullanılabilmesine olanak sağlayan OOP özelliğidir. 
# Yazılan bir sınıf bir başka sınıf tarafından miras alınabilir.
# Bu işlem yapıldığı zaman temel alınan sınıfın tüm özellikleri yeni sınıfa aktarılır.











