import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.setWindowTitle("Artificial neuron")
    window.setWindowIcon(QIcon("icons\icon.png"))
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
