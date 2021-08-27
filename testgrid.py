import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('testdata.txt')

#Defines number os rows and columns
cols = 3
rows = 2

fig, ax = plt.subplots(rows, cols)## Maybe add this option: sharex=True)

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
        
        df['tr_u'].plot(ax=ax[r, c])
        df['tr_i'].plot(ax=ax[r, c])
    
    
plt.tight_layout()
plt.show()
