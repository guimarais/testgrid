import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('testdata.txt')

#Defines number os rows and columns
cols = 3
rows = 2

fig, ax = plt.subplots(rows, cols, sharex=True, sharey=True)

## Get different device ids
ids = df['S_DeviceID'].unique()
idnum = 0

## Sets the indices as datetimes to easy plotting ahead
df['ts'] = pd.to_datetime(df['ts'])
df.set_index('ts', inplace=True)


# plotting loop
for c in range(cols):
    for r in range(rows):
        id_to_plot = ids[c + cols*r]

        df['tr_u'][df['S_DeviceID']==id_to_plot].plot(ax=ax[r, c])
        df['tr_i'][df['S_DeviceID']==id_to_plot].plot(ax=ax[r, c])
        ax[r,c].text(0.02, 0.9, id_to_plot, transform=ax[r, c].transAxes)

plt.tight_layout()
plt.show()

