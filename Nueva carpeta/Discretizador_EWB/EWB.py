
archivo = open("iris_completa.csv")
#archivo = open("wine.csv")
contenido = archivo.readlines()
#############################################################################################
instancia = []
for i in contenido:
    instancia.append(i.split(","))
encabezados = instancia[0]
del instancia[0]  ##encabezados
#############################################################################################
###GRUPOS A GENERAR
v_K = 6    # Pagina de referencia comparativa ->>>>  https://orange.readthedocs.io/en/latest/reference/rst/Orange.feature.discretization.html#Orange.feature.discretization.Discretization
#############################################################################################
intervalos = []
for index_atributo in range(len(instancia[0])-1): #por cada atributo a excepcion de la clase
    auxiliar = []
    for index_registro in range(len(instancia)):
        auxiliar.append(float(instancia[index_registro][index_atributo]))
    v_max = max(auxiliar)
    v_min = min(auxiliar)
    v_width = round((v_max-v_min)/v_K,4)
    ######################################################################
    print("Atributo analizado:" , encabezados[index_atributo])
    print("min: ", v_min)
    print("max: ", v_max)    
    print("width: ", v_width)
    ######################################################################    
    control  = round(v_min+v_width,4)
    temp = ["<" + str(control)]
    for j in range(1,v_K-1):
        s = "[" + str(control) + ", " #izquierda
        control = round(control+v_width,4)
        s += str(control) + ")" #derecha
        temp.append(s)
    temp.append(">=" + str(control))
    intervalos.append(temp)
    auxiliar.clear()
#############################################################################################
for i in intervalos:
    print(i)