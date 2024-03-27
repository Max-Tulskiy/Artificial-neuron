from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QSizePolicy, QFileDialog, QMessageBox
from window import Ui_MainWindow
from neuron import Neuron
from graphics_widget import GraphicWidget
from info_window import InfoWindow


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

        self.ui.radioButton.setChecked(True)                                                                                                                                                                                                                 
        self.ui.radioButton.toggled.connect(self.setGroupRed)
        self.ui.radioButton_2.toggled.connect(self.setGroupBlue)
        
        self.ui.solveButton.clicked.connect(self.solve_button_clicked)
        self.ui.clearButton.clicked.connect(self.canvas.clear_plot)

        self.corrected_weights = []

        self.ui.saveButton.clicked.connect(self.save)
        self.ui.loadButton.clicked.connect(self.load)

        self.ui.saveButton_2.clicked.connect(self.show_info)


    def setGroupRed(self, checked):
        if checked:
            self.canvas.group = 'red'

        
    def setGroupBlue(self, checked):
        if checked:
            self.canvas.group = 'blue'


    def solve_button_clicked(self):
        self.w1 = self.ui.lineEdit_w1.text()
        self.w2 = self.ui.lineEdit_w2.text()
        self.coefficient = self.ui.lineEdit_k.text()
        self.theta = self.ui.lineEdit_theta.text()
        self.typeActivation = self.ui.comboBox.currentText()
        self.coordinates = self.canvas.coordinates

        self.neuron = Neuron(self.w1,
                             self.w2,
                             self.coefficient,
                             self.theta,
                             self.typeActivation
                             )

        epochs = self.neuron.learn_neuron(self.coordinates)

        answer = []
        if epochs:
            self.corrected_weights = epochs
            answer = epochs[-1]
        else:
            answer = [float(self.w1),
                      float(self.w2),
                      float(self.theta)]
      
        self.canvas.plot_discriminant_line(answer[0],
                                           answer[1],
                                           answer[2],
                                           )


    def save(self):
        path1 = self.select_file()
        self.write_weights(path1)

        path2 = self.select_file()
        self.save_coordinates(path2)


    def write_weights(self, path):
        
        if self.corrected_weights:
            try:
                with open(str(path), "w") as file:
                    line_number = 1

                    for epoch in self.corrected_weights:
                        file.write(f'{line_number} epoch\n')
                        file.write(f'w1: {epoch[0]} \nw2: {epoch[1]} \nTHETA: {epoch[2]}\n\n')
                        line_number += 1
                    
                    self.print_messagebox('Веса сохранены')

            except Exception:
                self.print_messagebox('Ошибка записи весов')
        

    def save_coordinates(self, path):
        self.write_coordinates(path)

    
    def write_coordinates(self, path):
        coordinates = self.canvas.coordinates

        try:
            with open(str(path), "w") as file:
                file.write('<x1>   <x2>   <class>\n')

                for point in coordinates:
                    file.write(f'{round(point[0], 2)}, {round(point[1], 2)}, {round(point[2], 2)}\n')

            self.print_messagebox('Координаты сохранены')
        
        except Exception:
            self.print_messagebox('Ошибка записи координат')


    def load(self):
        path1 = self.select_file()
        self.corrected_weights = self.read_file(path1)

        path2 = self.select_file()
        self.coordinates = self.load_coordinates(path2)

        self.canvas.draw_points(self.coordinates)

        
    def read_file(self, path):
        epochs = []

        try:
            with open(str(path), 'r') as file:
                data = file.read()
                lines = data.strip().split('\n')

                for i in range(0, len(lines), 5): 
                    w1 = float(lines[i + 1].split(': ')[1])
                    w2 = float(lines[i + 2].split(': ')[1])
                    theta = float(lines[i + 3].split(': ')[1])
                    epochs.append([w1, w2, theta])

            result = epochs[-1]
    
            self.ui.lineEdit_w1.setText(str(result[0]))
            self.ui.lineEdit_w2.setText(str(result[1]))
            self.ui.lineEdit_theta.setText(str(result[2]))

            self.print_messagebox('Веса загружены')

        except Exception:
            self.print_messagebox('Ошибка загрузки весов')
    
        return epochs
    
    
    def load_coordinates(self, path):
        coordinates = []

        try:
            with open(str(path), 'r') as file:
                next(file)
                for line in file:
                    point = line.strip().split(', ')
                    coordinates.append([float(point[0]),
                                        float(point[1]),
                                        float(point[2])])
            
            self.print_messagebox('Координаты загружены')

        except Exception:
            self.print_messagebox('Ошибка загрузки координат')

        return coordinates
        

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Text Files (*.txt);;All Files (*)")

        file_dialog.exec_()
        selected_file = file_dialog.selectedFiles()
        path = selected_file[0]

        return path

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()

    def print_messagebox(self, text):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setWindowTitle("Инфо")
        messageBox.setText(text)
        messageBox.exec()