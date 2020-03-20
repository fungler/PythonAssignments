import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2020K1&CIVILSTAND=F
divorced2008 = 428864
divorced2020 = 544588

change = ((divorced2020 - divorced2008) / divorced2008) * 100
print("%.2f" % change + "%")

#https://api.statbank.dk/v1/data/FOLK1A/CSV?lang=en&delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=U
nevermarried = pd.read_csv("nevermarried.csv", sep=";")
print(nevermarried.nlargest(5, 'INDHOLD'))

#https://api.statbank.dk/v1/data/FOLK1A/CSV?lang=en&delimiter=Semicolon&OMR%C3%85DE=084&CIVILSTAND=G&Tid=*
changes = pd.read_csv("changes.csv", sep=";")
data = np.array(changes)

x = data[:, 2]
y = data[:, 3]

y_pos = np.arange(len(x))
plt.bar(y_pos, y)
plt.xticks(y_pos, x)
plt.show()


