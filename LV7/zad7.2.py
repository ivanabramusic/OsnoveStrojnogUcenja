import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread(r"C:\Users\Abram\Desktop\osu_lv-main\LV7\imgs\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w, h, d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# Zadatak 1

colors = np.unique(img_array_aprox, axis=0)
print(len(colors))

# Zadatak 2


km = KMeans(n_clusters=10, init='random', n_init=5)
km.fit(img_array_aprox)
labels = km.predict(img_array_aprox)

# Zadatak 3

for i in range(len(labels)):
    img_array_aprox[i] = km.cluster_centers_[labels[i]]

print(
    f'Broj boja u aproksimiranoj slici: {len(np.unique(img_array_aprox, axis=0))} (jednak predodredenom broju grupa)')
# povratak na originalnu dimenziju slike
img_aprox = np.reshape(img_array_aprox, (w, h, d))
# povratak iz raspona 0 do 1 u int
img_aprox = (img_aprox*255).astype(np.uint8)
plt.figure()
plt.title("Aproksimirana slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()

img = Image.imread(r"C:\Users\Abram\Desktop\osu_lv-main\LV7\imgs\test_1.jpg")
img = img.astype(np.float64) / 255

color_table = img.reshape(-1, 3)

distortions = []
K = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for k in K:

    km = KMeans(n_clusters=k, init='random', n_init=5)
    km.fit(color_table)

    distortions.append(km.inertia_)

plt.figure(figsize=(16, 8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()
