import pandas as pd
import numpy as np


data = {'team': ['RCB', 'CSK', 'MI']}
DF = pd.DataFrame(data)


teams = DF['team'].unique()


DF_encoded = pd.DataFrame()


for cricket in teams:
    DF_encoded[cricket] = np.where(DF['team'] == cricket, 1, 0)


DF1 = pd.concat([DF, DF_encoded], axis=1)

print(DF1)