import sys

from PyQt5 import uic, QtWidgets
import csv, random

qtCreatorFile = "LecturaInstancias.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_crear.clicked.connect(self.lector)

    # Área de los Slots
    def lector(self):
        name = str(self.txt_nombre.text())
        instance = int(self.txt_instancia.text())
        train = int(self.txt_ent.text())

        if train > instance:
            QtWidgets.QMessageBox.warning(self, "Advertencia",
                                          "Número de entrenamiento mayor que la instancia.")
            return

        test = instance - train
        self.lbl_prueba_t.setText(str(test))

        print("Nombre: "+name)
        print("Número total en instancias:" + str(instance))
        print("Número total en entrenamiento:" + str(train))
        print("Número total en prueba:" + str(test))

        train_set = set(random.sample(range(1, instance + 1), train))
        test_set = set(range(1, instance + 1)) - train_set
        n_instances = list(train_set)
        print("Números de entrenamiento: " + str(n_instances))
        n_instances = list(test_set)
        print("Números de prueba: " + str(n_instances))

        #for x in range(test):
            #print("Números random de la prueba: " + str(random.randint(1, instance)))
        #for x in range(train):
            #print("Números random de entrenamiento: " + str(random.randint(1, instance)))

        with open('C:/Users/rocio/PycharmProjects/SE_I_U3_EQ_4/Python/Ejercicios_equipo/A_Lectura/'+name+'_Entrenamiento.csv', 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['NO', 'Entrenamiento'])
            i = 1
            for j in range(1, instance + 1):
                if j in train_set:
                    writer.writerow([i, j])
                    i += 1

        with open('C:/Users/rocio/PycharmProjects/SE_I_U3_EQ_4/Python/Ejercicios_equipo/A_Lectura/'+name+'_Prueba.csv', 'w', newline='') as archivo_csv_2:
            writer = csv.writer(archivo_csv_2)
            writer.writerow(['NO', 'Prueba'])
            i = 1
            for k in range(1, instance + 1):
                if k in test_set:
                    writer.writerow([i, k])
                    i += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('Lector de instancias')
    window.show()
    sys.exit(app.exec_())