from PyQt5 import QtCore, QtWidgets, QtGui
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('Qt5Agg')


class My_Main_window(QtWidgets.QDialog):
    def __init__(self, parent=None):
      
        super(My_Main_window, self).__init__(parent)

      
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button_plot = QtWidgets.QPushButton("单位脉冲序列")
        self.button_plot1 = QtWidgets.QPushButton("阶跃序列")
        self.button_plot2 = QtWidgets.QPushButton("矩形序列")
        self.button_plot3 = QtWidgets.QPushButton("单位斜坡序列")

       
        self.button_plot.clicked.connect(self.plot_)
        self.button_plot1.clicked.connect(self.plot_1)
        self.button_plot2.clicked.connect(self.plot_2)
        self.button_plot3.clicked.connect(self.plot_3)

       
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button_plot)
        layout.addWidget(self.button_plot1)
        layout.addWidget(self.button_plot2)
        layout.addWidget(self.button_plot3)
        self.setLayout(layout)

    
    def plot_(self):
        def pulse(t):
            r = np.where(t == 0.0, 1.0, 0.0)  
            return r
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear() 
        n = np.arange(-4, 5)
        plt.ylim(0, 2)
        plt.stem(n, pulse(n))
        self.canvas.draw()
        
    def plot_1(self):
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear() 
        def step(t):
            r = np.where(t >= 0.0, 1.0, 0.0)
            return r
        n = np.arange(-4, 5)
        plt.ylim(0, 2)
        plt.stem(n, step(n))
        self.canvas.draw() 

    def plot_2(self):
        def rect(x, c, c0): 
            if x >= (c+c0):
                r = 0.0
            elif x < c0:
                r = 0.0
            else:
                r = 1
            return r
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear()  
        n = np.arange(-4, 5)
        y = np.array([rect(t, 3, 0) for t in n])
        plt.ylim(0, 2)
        plt.stem(n, y)
        self.canvas.draw()
        
    def plot_3(self):
        def Ramp(t):
            r = np.where(t >=0, t, 0.0)  
            return r
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.clear()  
        n = np.arange(-4, 5)
        plt.ylim(0, 5)
        plt.stem(n, Ramp(n))
        self.canvas.draw() 



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()
