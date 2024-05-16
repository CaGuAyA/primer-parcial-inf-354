import csv

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def calculate_q3(data):
    sorted_data = sorted(data)
    q3_index = int(0.75 * len(sorted_data))
    return sorted_data[q3_index]

def calculate_p80(data):
    sorted_data = sorted(data)
    p80_index = int(0.8 * len(sorted_data))
    return sorted_data[p80_index]

file_path = 'heart_failure_clinical_records.csv'

data = read_csv(file_path)

column_names = data[0][1:]

# Transponer los datos para que las columnas se conviertan en filas
data_transposed = list(map(list, zip(*data[1:])))

for i, (column_name, column_values) in enumerate(zip(column_names, data_transposed)):
    column_values = [float(value) for value in column_values]  # Convertir a flotante
    q3 = calculate_q3(column_values)
    p80 = calculate_p80(column_values)
    print(f"{column_name}: Q3 = {q3}, Percentil 80 = {p80}")

