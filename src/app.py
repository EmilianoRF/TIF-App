import sys

sys.path.append('lib')
from lib import MainWindow

# Se crea la aplicacion que contiene el main loop
app = MainWindow.QtWidgets.QApplication(sys.argv)

# Se crea el widget de la ventana principal
widget_mainwindow = MainWindow.QtWidgets.QMainWindow()

# Se crea la interfaz
ui = MainWindow.Ui_MainWindow()
# Se le pasa el widget de la ventana principal
ui.setupUi(widget_mainwindow)

# Se muestra la ventana
widget_mainwindow.show()

sys.exit(app.exec_())

