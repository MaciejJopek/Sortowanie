import matplotlib.pyplot as plt
import random


print ("Sortowanie bombelkowe")
def sortowanie (tablica):
    for i in range (len(tablica)-1):
        for j in range (len(tablica)-1):
            if tablica[j]>tablica[j+1]:
                tablica[j],tablica[j+1] = tablica [j+1], tablica[j]
                plt.cla()
                plt.bar(x, tablica)
                plt.pause(0.001)
    return (tablica)
x = []
for y in range(8):
    x.append(y)
tablica = []
for z in range(len(x)):
    tablica.append(z)
random.shuffle(tablica)
print ("Tablica nieposortowana ", tablica)
print("Tablica posortowana algorytmem babelkowym\n",sortowanie(tablica))
sortowanie(tablica)
plt.bar(x, tablica)
plt.show()
