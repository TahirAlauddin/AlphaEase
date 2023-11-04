import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow
import ctypes

myappid = 'tahiralauddin.prank-app.1.0.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class PrankApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set window title

        # Set window geometry
        self.setGeometry(100, 100, 500, 300)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.setWindowTitle("Prank App")
        self.setWindowIcon(QIcon("logo.png"))
        self.ui.submitBtn.clicked.connect(self.validate_license)


    def validate_license(self):
        key = self.ui.lineEdit.text()
        if key in [
            "QJKL-1234-PMNT-5678",
            "ZRTS-5678-JVWX-1234",
            "FDGB-7890-KLMP-4321",
            "HVNC-9876-XRQP-4567",
            "ZVXW-3456-QTSD-8901",
            "KLPN-6543-MBQR-2109",
            "GDFR-8765-JKLP-3412",
            "ZXCV-2345-BNMJ-6789",
            "WERQ-4321-TYUI-9876",
            "GHVB-7890-POIN-1234",
        ]:  # Example check, replace with your actual validation logic
            QMessageBox.critical(self, "Error", "Your computer is Incompatible!")

        else:
            QMessageBox.critical(self, "Error", "Invalid License Key!")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrankApp()
    window.show()
    sys.exit(app.exec_())

