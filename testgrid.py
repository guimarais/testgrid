import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('testdata.txt')

cols = 3
rows = 2

fig, ax = plt.subplots(rows, cols)

ids = df['S_DeviceID'].unique()
idnum = 0

for c in range(cols):
    for r in range(rows):
        id_to_plot = ids[c + cols*r]

        ax[r, c].plot(df[df['S_DeviceID']==id_to_plot].tr_i, df[df['S_DeviceID']==id_to_plot].tr_u)


plt.tight_layout()
plt.show()

