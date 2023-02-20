from PyQt5.QtWidgets import QWidget,QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np
from matplotlib.figure import Figure
def eje_en_centro(ax,x=0,y=0):
    ax.spines['left'].set_position(('data', x))
    ax.spines['bottom'].set_position(('data', y))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Se dibujan las flechas de los ejes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
  

import numpy as np
from random import random
class MplWidget(QWidget):
    
    def __init__(self, parent = None):
        self.presiones = []
        self.tiempos   = []
        self.xmin      = 0 
        self.xmax      = 5
        self.ymax      = 108
        self.ymin      = 90
        self.nxticks   = self.xmax*5+1
        self.nyticks   = self.xmax*5+1
        self.nplots    = 1
        self.label_plots = [str('Medición '+str(1))]
        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.mpl_connect("button_press_event", self.on_press)
        self.canvas.mpl_connect("button_release_event", self.on_release)
        self.canvas.mpl_connect("motion_notify_event", self.on_move)

        self.canvas.axes.set_xlim(self.xmin,self.xmax)
        self.canvas.axes.set_xticks(np.linspace(self.xmin,self.xmax,self.nxticks).round(decimals=1))
        self.canvas.axes.set_ylim(self.ymin,self.ymax)
        self.canvas.axes.set_yticks(np.linspace(self.ymin,self.ymax,self.nyticks))
        self.canvas.axes.set_ylabel('P [kPa]')
        self.canvas.axes.set_xlabel('t [s]')
        self.canvas.axes.grid(True,linestyle='dashed')
        self.setLayout(vertical_layout)


    def on_press(self, event):
        print("press")
        print("event.xdata", event.xdata)
        print("event.ydata", event.ydata)
        print("event.inaxes", event.inaxes)
        print("x", event.x)
        print("y", event.y)

    def on_release(self, event):
        print("release:")
        print("event.xdata", event.xdata)
        print("event.ydata", event.ydata)
        print("event.inaxes", event.inaxes)
        print("x", event.x)
        print("y", event.y)

    def on_move(self, event):
        print("move")
        print("Tiempo [s]:", event.xdata)
        print("Presión [kPa]", event.ydata)
        #print("event.inaxes", event.inaxes)
        #print("x", event.x)
        #print("y", event.y)
    def plot(self,tiempos,presiones):
        if self.nplots == 1 :
            self.tiempos = [[tiempo/1000 for tiempo in tiempos]]
            self.presiones = [presiones]
            self.canvas.axes.plot(self.tiempos[0],self.presiones[0],label=self.label_plots[0])
            self.ymin = min(min(self.presiones))
            self.ymax = max(max(self.presiones))
        else:
            self.tiempos.append([tiempo/1000 for tiempo in tiempos])
            self.presiones.append(presiones)
            for i in range(0,len(self.label_plots)):
                self.canvas.axes.plot(self.tiempos[i],self.presiones[i],label=self.label_plots[i])
                if self.ymin > min(self.presiones[i]):
                    self.ymin = min(self.presiones[i])
                if self.ymax < max(self.presiones[i]):
                    self.ymax = max(self.presiones[i])
        print(self.ymin,self.ymax)
        
        self.xmin = min(min(self.tiempos))
        self.xmax = max(max(self.tiempos))
        self.canvas.axes.set_xlim(self.xmin,self.xmax)
        self.canvas.axes.set_xticks(np.linspace(self.xmin,self.xmax,self.nxticks).round(decimals=1))
        self.canvas.axes.set_ylim(self.ymin,self.ymax)
        self.canvas.axes.set_yticks(np.linspace(self.ymin,self.ymax,self.nyticks))
        self.canvas.axes.set_ylabel('P [kPa]')
        self.canvas.axes.set_xlabel('t [s]')
        self.canvas.axes.grid(True,linestyle='dashed',alpha=0.5) 
        self.canvas.axes.legend()
        self.canvas.draw()
    def clear(self):
        self.canvas.axes.cla()
    def clearPlots(self):
        self.canvas.axes.cla()
        self.presiones = []
        self.tiempos   = []
        self.xmin      = 0 
        self.xmax      = 5
        self.ymax      = 108
        self.ymin      = 90
        self.nxticks   = self.xmax*5+1
        self.nyticks   = self.xmax*5+1
        self.nplots    = 1
        self.label_plots = [str('Medición '+str(1))]
        self.canvas.axes.set_ylim(self.ymin,self.ymax)
        self.canvas.axes.set_yticks(np.linspace(self.ymin,self.ymax,self.nyticks))
        self.canvas.axes.set_xlim(self.xmin,self.xmax)
        self.canvas.axes.set_xticks(np.linspace(self.xmin,self.xmax,self.nxticks).round(decimals=1))
        self.canvas.axes.set_ylabel('P [kPa]')
        self.canvas.axes.set_xlabel('t [s]')
        self.canvas.axes.grid(True,linestyle='dashed',alpha=0.5) 
        self.canvas.axes.legend()
        self.canvas.draw()
    def updateXaxis(self,xmin,xmax):
        self.xmin = xmin
        self.xmax = xmax
    def addPlot(self,label):
        self.nplots +=1
        if len(label) == 0:
            self.label_plots.append(str('Medición '+str(self.nplots)))
        elif len(label)!=0 and self.nplots == 1: 
            self.label_plots=[label]
        else:
            self.label_plots.append(label)
