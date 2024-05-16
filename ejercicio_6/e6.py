import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/CAGUAYA/Downloads/dataset_354/heart_failure_clinical_records.csv')

X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Visualizar el árbol y obtener las características y umbrales
fig, ax = plt.subplots(figsize=(15, 10))
plot_tree(clf, feature_names=X.columns, class_names=['No Muerte', 'Muerte'], filled=True, ax=ax)

# Obtener las características y umbrales
def get_decision_paths(tree, feature_names):
    left      = tree.tree_.children_left
    right     = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features  = [feature_names[i] for i in tree.tree_.feature]

    # Get all decision paths
    paths = []
    stack = [(0, [])] 
    while len(stack) > 0:
        node_id, path = stack.pop()
        if node_id != -1:
            path = path + [node_id]
            if left[node_id] != right[node_id]:
                stack.append((left[node_id], path))
                stack.append((right[node_id], path))
            else:
                paths.append(path)
    # For each path, generate condition
    conditions = []
    for path in paths:
        cond = ""
        for idx, node in enumerate(path):
            if idx > 0:
                cond += " and "
            if tree.tree_.feature[node] != -2:
                cond += f"{features[node]} <= {threshold[node]:.2f}"
        conditions.append(cond)
    return conditions

conditions = get_decision_paths(clf, X.columns)

# Imprimir las características y umbrales
for idx, condition in enumerate(conditions):
    print(f"Regla {idx+1}: {condition}")

# Mostrar el gráfico
plt.show()
