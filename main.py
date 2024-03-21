import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from window import Ui_MainWindow, QWidget, QComboBox
import math


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=6, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.coordinates = []
        self.group = None # добавить проверку на установление группы

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.setSizePolicy(self, sizePolicy)

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)


    def onclick(self, event):
        d = 0

        if self.group == 'red':
            d = 1
        else:
            d = -1

        if event.button == 1:
            x = event.xdata
            y = event.ydata
            self.coordinates.append([x, y, d])

            self.ax.scatter(event.xdata, event.ydata, color=self.group)
            self.fig.canvas.draw_idle()
            print(self.coordinates)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setGeometry(100, 100, 800, 600)
       
        self.ui.comboBox.addItem("Линейная")
        self.ui.comboBox.addItem("Биполярная пороговая")
        self.ui.comboBox.addItem("Сигмоидальная")

        #настройка виджета
        self.setCentralWidget(self.ui.centralwidget)
        layout = QVBoxLayout(self.ui.centralwidget)
        self.canvas = MplCanvas()
        layout.addWidget(self.canvas)
        self.ui.centralwidget.setLayout(layout)

        self.canvas.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ui.centralwidget.setLayout(layout)

        #отслеживание radiobuttn
        self.ui.radioButton.toggled.connect(self.setGroupRed)
        self.ui.radioButton_2.toggled.connect(self.setGroupBlue)
        
        self.ui.pushButton_2.clicked.connect(self.button2_clicked)

    def setGroupRed(self, checked):
        if checked:
            self.canvas.group = 'red'
        
    def setGroupBlue(self, checked):
        if checked:
            self.canvas.group = 'blue'
            

    def button2_clicked(self):
        
        self.w1 = self.ui.lineEdit.text()
        self.w2 = self.ui.lineEdit_2.text()
        self.coefficient = self.ui.lineEdit_3.text()
        self.theta = self.ui.lineEdit_4.text()
        self.typeActivation = self.ui.comboBox.currentText()
        self.coordinates = self.canvas.coordinates
        self.neuron = Neuron(self.w1, self.w2, self.coefficient, self.theta, self.typeActivation, self.coordinates)

        answer = self.neuron.learn_neuron(self.coordinates)
        print(answer)


class Neuron:
    def __init__(self, w1, w2, coefficient, theta, typeActivation, coordinates):
        self.w1 = float(w1)
        self.w2 = float(w2)   
        self.k = float(coefficient)
        self.theta = float(theta)
        self.typeActivation = typeActivation

    def learn_neuron(self, coordinates):
        for p in (coordinates):
            x1 = p[0]
            x2 = p[1]
            d = p[2]

            result = self.find_output_signal(x1, x2)
            self.functional_value(result, d, x1, x2)

        return [self.w1, self.w2, self.theta]

    # поиск ответа Y по активационной функции
    def functional_value(self, result, d, x1, x2):
        Y = 0
        if self.typeActivation == 'Линейная':
            
            Y = self.k * result
            if Y != d:
                self.find_delta_w(d, x1, x2)

        elif self.typeActivation == 'Биполярная пороговая':

            if result > 0:
                Y = 1
            else:
                Y = -1

            if Y != d:
                self.find_delta_w(d, x1, x2)

        else:
            Y = 1 / (1 + math.pow(math.e, self.K * result))        
            if Y != d:
                self.find_delta_w(d, x1, x2)

    def find_output_signal(self, x1, x2):
        x = self.w1 * x1 + self.w2 * x2 + self.theta
        return self.sign(x)

    def find_delta_w(self, d, x1, x2):
        self.w1 += d * x1 
        self.w2 += d * x2
        self.theta += d * self.theta

    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
