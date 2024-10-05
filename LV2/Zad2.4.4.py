import numpy as np
import matplotlib.pyplot as plt

white = np.ones([50,50])
black = np.zeros([50,50])

first_row = np.vstack((black,white))        #spajanje lijeve i desne matric
second_row = np.vstack((white,black))

img = np.hstack((first_row,second_row))     #spajanje gornje i donje matrice

plt.figure()
plt.imshow(img, cmap="gray")
plt.title("Zadatak 4")
plt.show()
