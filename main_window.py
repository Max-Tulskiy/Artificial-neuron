from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QSizePolicy, QFileDialog, QMessageBox
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

        self.file_attribute = ''

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

        self.corrected_weights = []

        self.ui.saveButton.clicked.connect(self.save_weights)
        self.ui.loadButton.clicked.connect(self.load_weights)


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
                             self.typeActivation
                             )

        epochs = self.neuron.learn_neuron(self.coordinates)
        self.corrected_weights = epochs
        answer = epochs[-1]

        print(answer)
        self.canvas.plot_discriminant_line(answer[0],
                                           answer[1],
                                           answer[2])
        
        print(answer)
        
    def save_weights(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")

        if self.file_attribute:
            self.write_to_file(self.file_attribute)

        elif file_dialog.exec_():

            selected_file = file_dialog.selectedFiles()
            path = selected_file[0]
            self.file_attribute = path
            self.write_to_file(path)

    def write_to_file(self, path):

        if self.corrected_weights:
            with open(str(path), "w") as file:
                line_number = 0

                for epoch in self.corrected_weights:
                    file.write(f'{line_number} epoch\n')
                    file.write(f'w1: {epoch[0]} \nw2: {epoch[1]} \nTHETA: {epoch[2]}\n\n')
                    line_number += 1
                    print(epoch)

                messageBox = QMessageBox()
                messageBox.setIcon(QMessageBox.Information)
                messageBox.setWindowTitle("Инфо")
                messageBox.setText("Веса сохранены")
                messageBox.exec()
                

    def load_weights(self):
        pass


        