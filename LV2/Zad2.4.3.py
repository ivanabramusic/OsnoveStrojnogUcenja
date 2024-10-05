import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("road (1).jpg")
img = img[:,:,0].copy()

print(img.shape)
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

brightImg = img + 100
brightImg[img>155] = 255

plt.figure()
plt.imshow(brightImg, cmap="gray")
plt.show()

#NP sa svim nulama velicine slike
filter = np.zeros(img.shape)
#Odredio pocetak 2. cetvrtine slike
querter = int((img.shape[1]/4)+1)
#Odredio pocetak polovice slike
half = int(img.shape[1]/2)
#U filter stavio sve retke, od 2. cetvrtine do pola slike stupaca
filter[:,querter:half] = img[:,querter:half]
plt.imshow(filter, cmap = "gray")
plt.show()


plt.imshow(np.rot90(img,3), cmap="gray")
plt.show()

plt.imshow(np.fliplr(img), cmap="gray")
plt.show()

