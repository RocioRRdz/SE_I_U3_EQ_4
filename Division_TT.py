import random

# Ruta del archivo de texto
archivo = "datos.txt"

# Cargar datos desde el archivo de texto
datos = {}
with open(archivo, "r") as file:
    for line in file:
        index, valor = line.strip().split(",")
        datos[int(index)] = int(valor)

# Dividir los datos en conjuntos de entrenamiento y prueba
train_percentage = 0.8
num_train = int(len(datos) * train_percentage)
indices = list(datos.keys())
random.shuffle(indices)
train_indices = indices[:num_train]
test_indices = indices[num_train:]
train_data = {k: datos[k] for k in train_indices}
test_data = {k: datos[k] for k in test_indices}

# Guardar datos de entrenamiento en un archivo de texto
train_file = "Potenciometro_train.txt"
with open(train_file, "w") as file:
    for index, valor in train_data.items():
        file.write(f"{index}, {valor}\n")

# Guardar datos de prueba en un archivo de texto
test_file = "Potenciometro_test.txt"
with open(test_file, "w") as file:
    for index, valor in test_data.items():
        file.write(f"{index}, {valor}\n")

print("Listo")
