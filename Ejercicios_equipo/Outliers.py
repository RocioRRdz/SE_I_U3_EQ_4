import csv
import numpy

lista = []
with open("C:/Users/rocio/PycharmProjects/SE_I_U3_EQ_4/Python/DatasetSuperHeroes.csv", newline="") as file:
    read = csv.reader(file)
    for fila in read:
        if fila[0]!= "NO":
            lista.append([float(x) for x in fila[1:7]])
#########################################################################################
#SIN Outlers por Quartiles
def outliers(instancia):
    #Cuartiles
    Q1 = numpy.percentile(instancia, 25)
    Q2 = numpy.percentile(instancia, 50)
    Q3 = numpy.percentile(instancia, 75)

    IQR = Q3 - Q1 #Rango intercuartilico
    Val_A_L_inf = Q1 - (1.5 * IQR)
    Val_A_L_sup = Q3 + (1.5 * IQR)

    #Val_A_E_inf = Q1 - (3.0 * IQR)
    #Val_A_E_sup = Q3 + (3.0 * IQR)
    OutliersporQuartiles = [v for v in instancia if v >= Val_A_L_inf and v <= Val_A_L_sup]
    #OutlersporQuartiles = [v for v in instancia if v >= Val_A_E_inf and v <= Val_A_E_inf]
    return OutliersporQuartiles

datos_outliers = []

for instancia in lista:
    instancia_outliers = outliers(instancia)
    datos_outliers.append(instancia_outliers)

print("Datos outliers:")
for instancia in datos_outliers:
    print(instancia)
