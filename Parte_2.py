import sys
import statistics
import numpy as np
from PyQt5 import uic, QtWidgets

import Outliers, Puntuacion_z

qtCreatorFile = "PROYECTO-Completo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btnAceptar.clicked.connect(self.aceptar)

    # Área de los Slots
    def aceptar(self):
        datos = np.loadtxt('datos.txt', delimiter=',', skiprows=1, usecols=1)
        numeros = datos.tolist()

        if self.rB_media.isChecked():
            media = statistics.mean(numeros)
            print("Media: " + str(media))
        elif self.rB_moda.isChecked():
            moda = statistics.mode(numeros)
            print("Moda: " + str(moda))
        elif self.rB_mediana.isChecked():
            mediana = statistics.median(numeros)
            print("Mediana: " + str(mediana))
        elif self.rB_vMayor.isChecked():
            mayor = max(numeros)
            print("Valor mayor: " + str(mayor))
        elif self.rB_vMenor.isChecked():
            menor = min(numeros)
            print("Valor menor: " + str(menor))


        if self.rB_normalizacion.isChecked():
            normalizacion = (np.array(numeros) - np.min(numeros)) / (np.max(numeros) - np.min(numeros))
            print("Normalización: " + str(normalizacion))
        elif self.rB_estandarizacion.isChecked():
            estandarizacion = (np.array(numeros) - np.mean(numeros)) / np.std(numeros)
            print("Estandarización:" + str(estandarizacion))
        elif self.rB_complemento.isChecked():
            complemento = []
            for numero in numeros:
                complemento.append(1 - numero)
            print("Complemento: "+ str(complemento))

        if self.rB_IQR.isChecked():
            Q = Outliers.outliers(numeros)
            print("IQR: "+str(Q))
        elif self.rB_PuntZ.isChecked():
            puntuacion_z = Puntuacion_z.calcular_puntuaciones_z(numeros)
            print("Puntuación Z: "+str(puntuacion_z))
        else:
            self.mensaje("Falta por seleccionar alguna opción de alguna Tabla.")

    def mensaje(self, texto):
        msj = QtWidgets.QMessageBox()
        msj.setText(texto)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

