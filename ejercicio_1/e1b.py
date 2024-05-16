import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/CAGUAYA/Downloads/dataset_354/heart_failure_clinical_records.csv')

q3 = np.percentile(data, 75, axis=0)
p80 = np.percentile(data, 80, axis=0)

for column, q3_val, p80_val in zip(data.columns, q3, p80):
    print(f"{column}: Q3 = {q3_val}, Percentil 80 = {p80_val}")
