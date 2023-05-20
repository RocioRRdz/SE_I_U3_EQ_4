import sys
from PyQt5 import uic, QtWidgets

import Red_Neuronal, Naive_Bayes, KNN

qtCreatorFile = "PROYECTO-Final.ui"  # Nombre del archivo aquí.
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
        if self.rB_ID3.isChecked():
            print("ID3 (Árbol de decisión).")
        elif self.rB_AL.isChecked():
            print("Asociador Lineal.")
        elif self.rB_KNN.isChecked():
            print("KNN -  K-Nearest Neighbors.")
            self.ejecutar_KNN()
        elif self.rB_NB.isChecked():
            print("Naive Bayes.")
            self.ejecutar_Naive_Bayes()
        elif self.rB_RNA.isChecked():
            print("RNA (Red Neuronal).")
            self.ejecutar_RNA()
        else:
            self.mensaje("Falta por seleccionar alguna opción de alguna Tabla.")

    def ejecutar_RNA(self):
        Red_Neuronal.ejecutar_RNA()

    def ejecutar_Naive_Bayes(self):
        Naive_Bayes.ejecutar_Naive_Bayes()

    def ejecutar_KNN(self):
        KNN.ejecutar_KNN()

    def mensaje(self, texto):
        msj = QtWidgets.QMessageBox()
        msj.setText(texto)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())