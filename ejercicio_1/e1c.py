import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/CAGUAYA/Downloads/dataset_354/heart_failure_clinical_records.csv')

media = data.mean()

mediana = data.median()

moda = data.mode().iloc[0]

media_geometrica = np.exp(np.mean(np.log(data), axis=0))

for column, mean_val, median_val, mode_val, geometric_mean_val in zip(data.columns, media, mediana, moda, media_geometrica):
    print(f"Columna '{column}':")
    print(f"  Media = {mean_val}")
    print(f"  Mediana = {median_val}")
    print(f"  Moda = {mode_val}")
    print(f"  Media Geométrica = {geometric_mean_val}")
    print()
