import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv('C:/Users/CAGUAYA/Downloads/dataset_354/heart_failure_clinical_records.csv')

# Separar las características y la variable objetivo
X = data.drop(columns=['DEATH_EVENT'])
y = data['DEATH_EVENT']

print(X)
print(y)

# Identificar las columnas categóricas y numéricas
categorical_columns = ['anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking']
numeric_columns = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']

# Crear transformadores para el preprocesamiento
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder())
])

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Combinar transformadores
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_columns),
        ('num', numeric_transformer, numeric_columns)
    ])

# Aplicar preprocesamiento a los datos
X_preprocessed = preprocessor.fit_transform(X)

# Mostrar los datos preprocesados
print(X_preprocessed)
