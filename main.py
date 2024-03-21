import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy
from window import Ui_MainWindow
from neuron import Neuron
from graphics_widget import GraphicWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.comboBox.addItem("Линейная")
        self.ui.comboBox.addItem("Биполярная пороговая")
        self.ui.comboBox.addItem("Сигмоидальная")

        self.setCentralWidget(self.ui.centralwidget)
        layout = QVBoxLayout(self.ui.centralwidget)
        self.canvas = GraphicWidget()
        layout.addWidget(self.canvas)
        self.ui.centralwidget.setLayout(layout)
        self.canvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ui.centralwidget.setLayout(layout)

        self.ui.radioButton.toggled.connect(self.setGroupRed)
        self.ui.radioButton_2.toggled.connect(self.setGroupBlue)
        
        self.ui.solveButton.clicked.connect(self.solve_button_clicked)
        self.ui.clearButton.clicked.connect(self.canvas.clear_plot)

    def setGroupRed(self, checked):
        if checked:
            self.canvas.group = 'red'
        
    def setGroupBlue(self, checked):
        if checked:
            self.canvas.group = 'blue'

    def solve_button_clicked(self):
        self.w1 = self.ui.lineEdit.text()
        self.w2 = self.ui.lineEdit_2.text()
        self.coefficient = self.ui.lineEdit_3.text()
        self.theta = self.ui.lineEdit_4.text()
        self.typeActivation = self.ui.comboBox.currentText()
        self.coordinates = self.canvas.coordinates

        self.neuron = Neuron(self.w1,
                             self.w2,
                             self.coefficient,
                             self.theta,
                             self.typeActivation,
                             self.coordinates)

        answer = self.neuron.learn_neuron(self.coordinates)

        self.canvas.plot_discriminant_line(answer[0],
                                           answer[1],
                                           answer[2])
        print(answer)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
