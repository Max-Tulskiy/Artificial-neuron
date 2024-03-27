from PySide6.QtWidgets import QMessageBox, QDialog
from info import Ui_Dialog
from PySide6.QtGui import QPixmap
from description import descriptions

class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("info")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        paths = {
                 'linear': r'images\linear.jpg',
                 'neuron': r'images\neuron.png',
                 'binary': r'images\binary.jpg',
                 'sigmoid': r'images\sigmoid.jpg'
                 }
        
        self.descriptions = descriptions

        self.ui.neuronButton.clicked.connect(lambda _: self.show_info(paths['neuron'], 'neuron'))
        self.ui.neuronButton.click()
        self.ui.linearButton.clicked.connect(lambda _: self.show_info(paths['linear'], 'linear'))
        self.ui.binaryButton.clicked.connect(lambda _: self.show_info(paths['binary'], 'binary'))
        self.ui.sigmoidButton.clicked.connect(lambda _: self.show_info(paths['sigmoid'], 'sigmoid'))
        

    def show_info(self, path, item):
        pixmap = QPixmap(path)  
        
        if pixmap.isNull():
            messageBox = QMessageBox()
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.setText('Не удалось загрузить изображение')
            messageBox.exec()
        else:
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)

            self.ui.textLabel.setWordWrap(True)
            self.ui.textLabel.setStyleSheet("font-size: 10pt; font-family: Cascadia Code;")
            self.ui.textLabel.setText(self.descriptions[item])
             