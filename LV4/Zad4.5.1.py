from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

data = pd.read_csv(
    r'C:\Users\Abram\Desktop\osu_lv-main\LV4\data_C02_emission.csv')

data = data.drop(["Make", "Model"], axis=1)

input_variables = ['Engine Size (L)',
                   'Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Cylinders']

# Zadatak pod a)

output_variable = ['CO2 Emissions (g/km)']
x = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test = train_test_split(x, test_size=0.2, random_state=1)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=1)

# Zadatak pod b)

for i in range(len(input_variables)):
    train_data_x = X_train[:, i]
    train_data_y = y_train
    test_data_x = X_test[:, i]
    test_data_y = y_test
    plt.scatter(train_data_x, train_data_y, color="blue", label="Train")
    plt.scatter(test_data_x, test_data_y, color="red", label="Train")
    plt.xlabel("Input varijabla")
    plt.ylabel("C02 Emission")
    plt.show()


# Zadatak pod c)

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

fig, ax = plt.subplots(1, 2, sharex='col', sharey='row')
fig.subplots_adjust(hspace=0.5, wspace=0.5)
ax[0].hist(X_train[:, 2], bins=20)
ax[0].set_title('Izvorni podatci')

ax[1].hist(X_train_n[:, 2], bins=10)
ax[1].set_title('Skalirani podatci')

plt.show()

# Zadatak pod d)

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print("Intercept", linearModel.intercept_)
print(linearModel.coef_)

# Zadatak pod e)

y_pred_test = linearModel.predict(X_test_n)

fig, ax = plt.subplots(1, 2, sharex='col', sharey='row')
ax[0].scatter(X_test_n[:, 0], y_test)
ax[1].scatter(X_test_n[:, 0], y_pred_test)
plt.show()

# Zadatak pod f)

RMSE = mean_squared_error(y_test, y_pred_test, squared=False)
MAE = mean_absolute_error(y_test, y_pred_test)
MAPE = mean_absolute_percentage_error(y_test, y_pred_test)
R2 = r2_score(y_test, y_pred_test)

# Zadatak pod g)

print("RMSE", RMSE)
print("MAE", MAE)
print("MAPE", MAPE)
print("R2", R2)
