import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from window import Ui_MainWindow, QWidget, QComboBox


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=6, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.coordinates = []
        self.group = None

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.setSizePolicy(self, sizePolicy)

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)


    def onclick(self, event):
        if event.button == 1:
            x = event.xdata
            y = event.ydata
            color = 'red'
            self.coordinates.append([x, y, color])

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
    
    def setGroupRed(self, checked):
        if checked:
            self.canvas.group = 'red'
            print("red")

    def setGroupBlue(self, checked):
        if checked:
            self.canvas.group = 'blue'
            print('blue')

        
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
