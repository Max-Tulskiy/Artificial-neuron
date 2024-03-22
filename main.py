import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
