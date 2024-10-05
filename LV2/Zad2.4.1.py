import numpy as np
import matplotlib.pyplot as plt

#Indikacija polja
x = np.array([1,2,3,3,1], float)
y = np.array([1,2,2,1,1], float)

#Raspon x i y ose
plt.axis([0,4,0,4])

#Labele x i y ose
plt.xlabel('x')
plt.ylabel('y')
plt.title("Crtez")

#Crtanje
plt.plot(x,y, 'r', linewidth = 2, marker= "*", markersize = 15)
plt.show()