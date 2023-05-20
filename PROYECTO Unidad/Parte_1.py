import sys
import serial
import time
import serial.tools.list_ports
from PyQt5 import uic, QtWidgets

potenciometro = "A0"
qtCreatorFile = "PROYECTO-Numeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        for i in serial.tools.list_ports.comports():
            print(i)
            self.cbxCOM.addItem(str(i)[3:4])
        self.arduino = None
        self.btnConnect.clicked.connect(self.connect)
        self.btnAccept.clicked.connect(self.accept)
        self.btnAccept.setEnabled(True)

    def connect(self):
        if self.arduino == None:
            com = "COM" + self.cbxCOM.itemText(self.cbxCOM.currentIndex())
            self.arduino = serial.Serial(com, baudrate=9600, timeout=1)
            self.lblCOM.setText(com)
        else:
            self.message("Ya se ha realizado la conexión.")

    def accept(self):
        number = 0
        if self.rB_one.isChecked():
            number = 1
        elif self.rB_thirty.isChecked():
            number = 30
        elif self.rB_fifty.isChecked():
            number = 50
        elif self.rB_one_hundred.isChecked():
            number = 100
        else:
            self.mensaje("No ha seleccionado alguna opción de la Tabla.")
            return
        print("Tamaño de la muestra:", number)

        contador = 1
        with open("datos.txt", "w") as file:
            while self.arduino.inWaiting() > 0:
                if contador > number:
                    self.menssage(str(number) + " números guardados en el archivo de texto 'Datos'")
                    self.close()
                    break

                value = self.arduino.readline().decode().strip()
                time.sleep(0.2)
                print(value)
                file.write(f"{contador}, {value}\n")
                contador += 1  # indice

    def menssage(self, texto):
        msj = QtWidgets.QMessageBox()
        msj.setText(texto)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

