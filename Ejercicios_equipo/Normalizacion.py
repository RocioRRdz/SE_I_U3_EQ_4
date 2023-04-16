import csv
import numpy

lista = []
with open("C:/Users/rocio/PycharmProjects/SE_I_U3_EQ_4/Python/DatasetSuperHeroes.csv", newline="") as file:
    read = csv.reader(file)
    for fila in read:
        if fila[0]!= "NO":
            lista.append([float(x) for x in fila[1:7]])
#########################################################################################
#Normalizacion
def normalizacion(instancia):
    mayor = max(instancia)
    menor = min(instancia)
    InstanciaNormalizada = [(i-menor) / (mayor-menor) for i in instancia]
    return InstanciaNormalizada

datos_normalizados = []

for instancia in lista:
    instancia_normalizada = normalizacion(instancia)
    datos_normalizados.append(instancia_normalizada)

print("Datos normalizados:")
for instancia in datos_normalizados:
    print(instancia)