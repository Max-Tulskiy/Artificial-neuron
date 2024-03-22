from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QSizePolicy
import matplotlib.pyplot as plt


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
        self.group = None # надо добавить проверку на установление группы

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
       
    def plot_discriminant_line(self, w1, w2, w3):

        x = [-5.00, -4.00, -3.00, -2.00, -1.00, 
             0.00, 1.00, 2.00, 3.00, 4.00, 5.00]
        y = []

        for x1 in x:
            res = -1 * w1/w2 * x1 - w3/w2
            if res < -6:
                res = -5.99
            elif res > 6:
                res = 5.99

            y.append(round(res, 2))

        print('x:' + str(x))
        print('y' + str(y))

        plt.plot(x, y, color='green')
        self.fig.canvas.draw_idle()

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
