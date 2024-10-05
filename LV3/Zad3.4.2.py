import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    r'C:\Users\Abram\Desktop\osu_lv-main\LV3\data_C02_emission.csv')

MAKE = 'Make'
MODEL = 'Model'
VEHCILE_CLASS = 'Vehicle Class'
ENGINE_SIZE = 'Engine Size (L)'
CYLINDERS = 'Cylinders'
TRANSIMSSION = 'Transmission'
FUEL_TYPE = 'Fuel Type'
FUEL_CONSUMPTION_CITY = 'Fuel Consumption City (L/100km)'
FUEL_CONSUMPTION_HWY = 'Fuel Consumption Hwy (L/100km)'
FUEL_CONSUMPTION_COMB_L = 'Fuel Consumption Comb (L/100km)'
FUEL_CONSUMPTION_COMB_MPG = 'Fuel Consumption Comb (mpg)'
CO2_EMISSIONS = 'CO2 Emissions (g/km)'

# A dio zadatka

plt.figure()
data[CO2_EMISSIONS].plot(kind='hist', bins=len(data[CO2_EMISSIONS].unique()))


# B dio zadatka
grouped_by_fuels = data.groupby(FUEL_TYPE)
types = data[FUEL_TYPE].unique()

fig, ax = plt.subplots()
for name, group in grouped_by_fuels:
    ax.scatter(group[FUEL_CONSUMPTION_CITY], group[CO2_EMISSIONS], s=5)
ax.legend(types)

# C dio zadatka

grouped = data.groupby(FUEL_TYPE)
grouped.boxplot(column=FUEL_CONSUMPTION_HWY)

# D dio zadatka

grouped_by_feul_type = data.groupby(FUEL_TYPE).agg(Size=(FUEL_TYPE, 'size'))
grouped_by_feul_type.plot(kind='bar')


# E dio zadatka

grouped_by_cylinders = data.groupby(CYLINDERS).agg(
    Average_CO2=(CO2_EMISSIONS, 'mean'))
grouped_by_cylinders.plot(kind='bar')


plt.show()
