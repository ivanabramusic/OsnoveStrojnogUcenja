import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                           random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=5)

# Zadatak a)

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', label='Train')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test,
            cmap='bwr', marker='x', label='Test')
plt.legend()
plt.show()

# Zadatak b)

model = LogisticRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)


# Zadatak c)


theta_0 = model.intercept_
theta_1 = model.coef_[0][0]
theta_2 = model.coef_[0][1]

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', label='Train')

x_min, x_max = np.min(X_train[:, 1]), np.max(X_train[:, 1])

x2 = np.linspace(x_min, x_max, 100)
x1 = -theta_0/theta_1 - theta_2/theta_1*x2

plt.plot(x1, x2)

plt.fill_between(x1, x2, x_min, alpha=0.2, color='red')
plt.fill_between(x1, x2, x_max, alpha=0.2, color='blue')


plt.show()

# Zadatak d)

y_test_p = model.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()

print("Tocnost: ", accuracy_score(y_test, y_test_p))
print("Preciznost: ", precision_score(y_test, y_test_p))
print("Odziv: ", recall_score(y_test, y_test_p))
print(classification_report(y_test, y_test_p))

# Zadatak e)

for i in range(len(y_test)):
    if y_test[i] == y_test_p[i]:
        plt.plot(X_test[i, 0], X_test[i, 1], 'go', markersize=10)
    else:
        plt.plot(X_test[i, 0], X_test[i, 1], 'ko', markersize=10)

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Test data')
plt.show()
