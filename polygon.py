import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QAction, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPolygon, QPen, QPainter, QBrush,QFont
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Third(QMainWindow):
    def __init__(self):
        super(Third,self).__init__()
        self.setGeometry(300,100,700,700)
        self.setWindowTitle("Plot given Circle")
        self.x = 0
        self.y = 0
        self.r = 0
        self.initUI3()

    def initUI3(self):
        nameLabel1 = QLabel(self)
        nameLabel1.setText('Enter x co-ordinate:')
        nameLabel1.move(100, 40)
        nameLabel1.setFont(QFont('Arial', 12))
        nameLabel1.resize(400,30)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100, 80)
        self.textbox1.resize(400,50)
        font = self.textbox1.font()
        font.setPointSize(20)
        self.textbox1.setFont(font)

        nameLabel2 = QLabel(self)
        nameLabel2.setText('Enter y co-ordinate:')
        nameLabel2.move(100, 190)
        nameLabel2.setFont(QFont('Arial', 12))
        nameLabel2.resize(400,30)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 230)
        self.textbox2.resize(400,50)
        font = self.textbox2.font()
        font.setPointSize(20)
        self.textbox2.setFont(font)

        nameLabel3 = QLabel(self)
        nameLabel3.setText('Enter radius of circle:')
        nameLabel3.move(100, 340)
        nameLabel3.setFont(QFont('Arial', 12))
        nameLabel3.resize(400,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(100, 380)
        self.textbox3.resize(400,50)
        font = self.textbox3.font()
        font.setPointSize(20)
        self.textbox3.setFont(font)

        self.btn = QPushButton('Click here to plot', self)
        self.btn.setStyleSheet('QPushButton {background-color: #A3C1DA; font: 13px; color: red;}')
        self.btn.move(150,490)
        self.btn.resize(200,40)
        self.btn.clicked.connect(self.plot_circle)

        self.show()

    def plot_circle(self):
        textboxValue = self.textbox1.text()
        self.x = float(textboxValue)

        textboxValue = self.textbox2.text()
        self.y = float(textboxValue)

        textboxValue = self.textbox3.text()
        self.r = float(textboxValue)

        fig, ax = plt.subplots()
        ax.set_xlim((0, 20))
        ax.set_ylim((0, 20))
        circle = plt.Circle((self.x, self.y), self.r, color = 'blue', fill = False )
        ax.add_artist(circle)
        plt.title('Circle')

        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        plt.show()

    def close_window(self):
        choice = QMessageBox.question(self,'Quit',"Wanna exit?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            sys.exit()
        else:
            pass

class Second(QMainWindow):
    def __init__(self):
        super(Second,self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Click on window for plotting polygon")
        self.xpoint = []
        self.ypoint = []
        self.points = QPolygon()
        self.initUI2()

    def initUI2(self):
        extractAction = QAction("&Quit",self)
        extractAction.setShortcut("Ctrl+Q")

        extractAction2 = QAction("&Run",self)
        extractAction2.setShortcut("Ctrl+R")

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction2)

        extractAction.triggered.connect(self.close_window)
        extractAction2.triggered.connect(self.plot_polygon)

    def close_window(self):
        choice = QMessageBox.question(self,'Quit',"Wanna exit?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            sys.exit()
        else:
            pass

    def plot_polygon(self):
        self.xpoint.append(self.xpoint[0])
        self.ypoint.append(self.ypoint[0])
        print(self.xpoint)
        print(self.ypoint)
        plt.plot(self.xpoint,self.ypoint)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.title('Polygon')
        plt.show()

    def mouseReleaseEvent(self, QMouseEvent):
        print(QMouseEvent.x(), ',', QMouseEvent.y())
        self.xpoint.append(QMouseEvent.x())
        self.ypoint.append(QMouseEvent.y())

    def mousePressEvent(self,p):
        self.points << p.pos()
        self.update()

    def paintEvent(self, ev):
        qp = QPainter(self)
        pen = QPen(QtCore.Qt.black, 0.1)
        brush = QBrush(QtCore.Qt.black)
        qp.setPen(pen)
        qp.setBrush(brush)
        for i in range(self.points.count()):
            qp.drawEllipse(self.points.point(i), 3.5, 3.5)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000,620)
        self.setWindowTitle("Welcome to Polygons with PyQt")
        self.initUI()

    def initUI(self):
        m = PlotCanvas(self, width=8, height=6)
        m.move(0,0)

        btn = QPushButton('Quit', self)
        btn.setStyleSheet('QPushButton {background-color: #A3C1DA; font: 13px; color: red;}')
        btn.clicked.connect(self.close_window)
        btn.move(800,400)
        btn.resize(150,100)

        btn2 = QPushButton('Mouse Click Event', self)
        btn2.setStyleSheet('QPushButton {background-color: #A3C1DA; font: 13px; color: red;}')
        btn2.clicked.connect(self.open_window)
        self.dialogs = list()
        btn2.move(800,100)
        btn2.resize(150,100)

        btn3 = QPushButton('Draw a circle', self)
        btn3.setStyleSheet('QPushButton {background-color: #A3C1DA; font: 13px; color: red;}')
        btn3.clicked.connect(self.open_form)
        self.forms = list()
        btn3.move(800,250)
        btn3.resize(150,100)

        self.show()

    def open_window(self):
        dialog = Second()
        self.dialogs.append(dialog)
        dialog.show()

    def open_form(self):
        form = Third()
        self.forms.append(form)
        form.show()

    def close_window(self):
        choice = QMessageBox.question(self,'Close',"Wanna exit?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            sys.exit()
        else:
            pass

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=6):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.set_title('Sample plot')
        '''
        Circle 1 center -  2.5,7.5 Radius = 2.5
        Circle 2 center -  7.5,2.5 Radius = 2.5
        '''
        ax.axes.plot([0,0,5,5,0,5,5,10,10,5], [0,5,5,0,0,0,10,10,5,5])
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())