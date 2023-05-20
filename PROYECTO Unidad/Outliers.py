import numpy

def outliers(datos):
    #Cuartiles
    Q1 = numpy.percentile(datos, 25)
    Q2 = numpy.percentile(datos, 50)
    Q3 = numpy.percentile(datos, 75)

    IQR = Q3 - Q1 #Rango intercuartilico
    Val_A_L_inf = Q1 - (1.5 * IQR)
    Val_A_L_sup = Q3 + (1.5 * IQR)

    #Val_A_E_inf = Q1 - (3.0 * IQR)
    #Val_A_E_sup = Q3 + (3.0 * IQR)
    OutliersporQuartiles = [v for v in datos if v >= Val_A_L_inf and v <= Val_A_L_sup]
    #OutlersporQuartiles = [v for v in instancia if v >= Val_A_E_inf and v <= Val_A_E_inf]
    return OutliersporQuartiles

