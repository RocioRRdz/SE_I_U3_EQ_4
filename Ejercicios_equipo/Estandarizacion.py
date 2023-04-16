import csv
import numpy

lista = []
with open("C:/Users/rocio/PycharmProjects/SE_I_U3_EQ_4/Python/DatasetSuperHeroes.csv", newline="") as file:
    read = csv.reader(file)
    for fila in read:
        if fila[0]!= "NO":
            lista.append([float(x) for x in fila[1:7]])
#########################################################################################
#Estandarizacion
def estandarizacion(instancia):
    #media = sum(instancia) / len(instancia)
    media = numpy.mean(instancia)
    desv_est = numpy.std(instancia)
    InstanciaEstandarizada = [(i-media) / desv_est for i in instancia]
    return InstanciaEstandarizada

datos_estandarizados = []

for instancia in lista:
    instancia_estandarizada = estandarizacion(instancia)
    datos_estandarizados.append(instancia_estandarizada)

print("Datos estandarizados::")
for instancia in datos_estandarizados:
    print(instancia)