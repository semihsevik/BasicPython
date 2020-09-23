# Python - Matplotlib
import matplotlib.pyplot as plt

#Örnek verileri tanımlayalım.
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

#Renkler ve dilimler arası mesafeyi ayarlayalım.
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = [0.05 for i in range(6)]

#Pasta grafiğini çizdirelim.
plt.pie(popuratity, explode=explode, labels=languages, 
colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

#Grafiği gösterelim.
plt.show()





















