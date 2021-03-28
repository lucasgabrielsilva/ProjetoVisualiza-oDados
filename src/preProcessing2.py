import pandas as pd
import numpy as np


newBase = pd.read_csv('./bases/processedBase.csv')
count = 0

for i, rowNewBase in newBase.iterrows():
    if((rowNewBase['Clube'] == "ERRO") or (rowNewBase['Posição'] == "ERRO")):
        newBase.drop(index=i, axis=0, inplace=True)
        print(count)
        count += 1

newBase.to_csv("./bases/newBase.csv", index=False)