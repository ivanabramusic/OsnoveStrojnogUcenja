import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data (1).csv", skiprows = 1, delimiter = ',')

print(len(data))

#Prodji kroz sve retke al uzmi samo index [2], prodji kroz sve retke al uzmi samo index [1]
plt.scatter(data[:,2], data[:,1])
plt.title("Omjer tezina i visine")
plt.xlabel("Tezina")
plt.ylabel("Visina")
plt.show()

#Kreni od 0 do kraja sa korakom 50
x = data[::50]
y = data[::50]

plt.scatter(x[:,2], y[:,1])
plt.title("Omjer tezina i visine")
plt.xlabel("Tezina")
plt.ylabel("Visina")
plt.show()

print(np.max(data[:,1]))
print(np.min(data[:,1]))
print(np.mean(data[:,1]))

man = (data[:,0]==1)
woman = (data[:,0]==0)

print(np.max(data[woman,1]))
print(np.min(data[woman,1]))
print(np.mean(data[woman,1]))

print(np.max(data[man,1]))
print(np.min(data[man,1]))
print(np.mean(data[man,1]))