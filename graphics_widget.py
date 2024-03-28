from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QSizePolicy
import matplotlib.pyplot as plt
from PySide6.QtCore import QTimer


class GraphicWidget(FigureCanvas):
    def __init__(self,
                 parent=None,
                 width=6,
                 height=6,
                 dpi=100):
        
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)

        self.ax.grid(True,
                     linestyle='--',
                     color='gray',
                     linewidth=0.5)
        
        self.coordinates = []
        self.group = 'red'
       
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.setSizePolicy(self, sizePolicy)
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)


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


    def draw_learning(self, coordinates, epochs):
        self.draw_epoch(0, coordinates, epochs)
        
        
    def draw_epoch(self, index, coordinates, epochs):
        if index >= len(epochs):
            return

        w1, w2, w3 = epochs[index]
        self.clear_line()
        self.draw_points(coordinates)
        self.plot_discriminant_line(w1, w2, w3)
        self.fig.canvas.draw_idle()

        QTimer.singleShot(1000, lambda: self.draw_epoch(index + 1, coordinates, epochs))

    def clear_line(self):
        self.ax.clear()
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.grid(True,
                     linestyle='--',
                     color='gray',
                     linewidth=0.5)


    def plot_discriminant_line(self, w1, w2, w3):

        x = [-5.00, -4.00, -3.00, -2.00, -1.00, 
             0.00, 1.00, 2.00, 3.00, 4.00, 5.00]
        y = []

        for x1 in x:
            res = -1 * w1 / w2 * x1 - w3 / w2
            if res < -6:
                res = -5.99
            elif res > 6:
                res = 5.99

            y.append(round(res, 2))

     
        plt.plot(x, y, color='green')
        self.fig.canvas.draw_idle()


    def draw_points(self, coordinates):
        self.ax.clear()
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.grid(True, linestyle='--', color='gray', linewidth=0.5)

        for point in coordinates:
            x = point[0]
            y = point[1]
            d = point[2]
            color = ''
            if d == 1:
                color = 'red'
            else:
                color = 'blue'
                            
            self.ax.scatter(x, y, color=color)

        self.draw()
        

    def clear_plot(self):
        self.ax.clear()
        self.coordinates.clear()
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.grid(True,
                     linestyle='--',
                     color='gray',
                     linewidth=0.5)
        
        self.fig.canvas.draw_idle()
