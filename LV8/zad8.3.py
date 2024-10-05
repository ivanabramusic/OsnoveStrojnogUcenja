import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.image as Image

model = tf.keras.models.load_model(
    r"C:\Users\Abram\Desktop\osu_lv-main\FCN")

img = Image.imread(r"C:\Users\Abram\Desktop\osu_lv-main\LV8\test.png")[:, :, 0]
normalized_img = tf.keras.utils.normalize(img, axis=1)
normalized_img = normalized_img.reshape(1, 784)
plt.imshow(img, cmap='gray')
plt.show()

predictions = model.predict(normalized_img)
print(f"Predicted: {np.argmax(predictions)}")
