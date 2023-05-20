import statistics

def calcular_puntuaciones_z(datos):
    media = statistics.mean(datos)
    desviacion_estandar = statistics.stdev(datos)

    puntuaciones_z = [(x - media) / desviacion_estandar for x in datos]
    return puntuaciones_z

