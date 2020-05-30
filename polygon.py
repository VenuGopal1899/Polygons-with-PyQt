import sys
import numpy as np

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# New window to plot circles and polygons
class Fourth(QMainWindow):
    def __init__(self):
        super(Fourth,self).__init__()
        self.setGeometry(100,100,1000,700)
        self.setWindowTitle("Circles & Polygons")
        self.setStyleSheet("background-color: azure;")
        self.initUI4()
        self.fs = []

    def initUI4(self):
        extractAction = QAction("&Open",self)
        extractAction.setShortcut("Ctrl+O")

        extractAction1 = QAction("&Save",self)
        extractAction1.setShortcut("Ctrl+S")

        extractAction2 = QAction("&Close",self)
        extractAction2.setShortcut("Ctrl+Q")

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        font = fileMenu.font()
        font.setPointSize(12)
        fileMenu.setFont(font)

        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction1)
        fileMenu.addAction(extractAction2)

        extractAction.triggered.connect(self.open_file)
        extractAction1.triggered.connect(self.save_file)
        extractAction2.triggered.connect(self.close_window)

        btn = QPushButton('Plot', self)
        btn.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn.clicked.connect(self.plot_graph)
        btn.move(580,400)
        btn.resize(150,100)

        btn2 = QPushButton('Clear', self)
        btn2.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn2.clicked.connect(self.clear_plot)
        self.dialogs = list()
        btn2.move(580,140)
        btn2.resize(150,100)

        btn3 = QPushButton('Add a circle', self)
        btn3.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn3.clicked.connect(self.draw_circle)
        self.forms = list()
        btn3.move(230,140)
        btn3.resize(150,100)

        btn4 = QPushButton('Add a polygon', self)
        btn4.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn4.clicked.connect(self.draw_poly)
        self.forms2 = list()
        btn4.move(230,400)
        btn4.resize(150,100)
        self.show()

    def plot_graph(self):
        m = PlotCanvas2(self, width=8, height=7)
        m.move(0,0)

    def clear_plot(self):
        open('polygon.txt', 'w').close()
        open('circle.txt', 'w').close()

    def draw_circle(self):
        self.editor()

    def draw_poly(self):
        self.editor()

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def open_file(self):
        name = QFileDialog().getOpenFileName(self, 'Open File')
        file = open(name[0],'r')
        self.editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def save_file(self):
        name = QFileDialog().getSaveFileName(self, 'Save File')
        file = open(name[0],'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def close_window(self):
        choice = QMessageBox.question(self,'Close',"Wanna Close?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            f = Fourth()
            self.fs.append(f)
            f.show()
            self.close()
        else:
            pass

class PlotCanvas2(FigureCanvas):
    def __init__(self, parent = None, width=8, height=7):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        ax.set_title('Multiple Plots')

        x, y = np.loadtxt('polygon.txt', delimiter=',', unpack = True)
        plt.plot(x, y, color = "black")

        file = open('circle.txt','r')
        Content = file.read()
        Points_List = Content.split("\n")

        for i in Points_List:
            if i:
                point = i.split(",")
                if len(point) != 3:
                    error_dialog = QErrorMessage()
                    error_dialog.showMessage('Missing Circle co-ordinates')
                circle = plt.Circle((float(point[0]),float(point[1])), float(point[2]),  ec = "black",fc = "dimgray", alpha = 0.5)
                ax.add_patch(circle)

        plt.show()


# New window to plot circles
class Third(QMainWindow):
    def __init__(self):
        super(Third,self).__init__()
        self.setGeometry(300,100,700,700)
        self.setWindowTitle("Circle")
        self.setStyleSheet("background-color: azure;")
        self.x = 0
        self.y = 0
        self.r = 0
        self.initUI3()

    def initUI3(self):
        nameLabel1 = QLabel(self)
        nameLabel1.setText('Enter x co-ordinate:')
        nameLabel1.move(100, 40)
        nameLabel1.setFont(QFont('Lucida sans', 14))
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
        nameLabel2.setFont(QFont('Lucida sans', 14))
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
        nameLabel3.setFont(QFont('Lucida sans', 14))
        nameLabel3.resize(400,30)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(100, 380)
        self.textbox3.resize(400,50)
        font = self.textbox3.font()
        font.setPointSize(20)
        self.textbox3.setFont(font)

        self.btn = QPushButton('Click here to plot', self)
        self.btn.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
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
        choice = QMessageBox.question(self,'Close',"Wanna exit?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            sys.exit()
        else:
            pass

# New window - To plot Polygons
class Second(QMainWindow):
    def __init__(self):
        super(Second,self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Polygon - Mouse Click Event")
        self.xpoint = []
        self.ypoint = []
        self.points = QPolygon()
        self.initUI2()

    def initUI2(self):
        extractAction = QAction("&Close",self)
        extractAction.setShortcut("Ctrl+Q")

        extractAction2 = QAction("&Run",self)
        extractAction2.setShortcut("Ctrl+R")

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        font = fileMenu.font()
        font.setPointSize(12)
        fileMenu.setFont(font)

        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction2)

        extractAction.triggered.connect(self.close_window)
        extractAction2.triggered.connect(self.plot_polygon)

    def close_window(self):
        choice = QMessageBox.question(self,'Close',"Wanna Close?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            self.close()
        else:
            pass

    def plot_polygon(self):
        self.xpoint.append(self.xpoint[0])
        self.ypoint.append(self.ypoint[0])
        plt.plot(self.xpoint,self.ypoint)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.title('Polygon')

        plt.show()

    def mouseReleaseEvent(self, QMouseEvent):
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


# Main window or Home Screen
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000,670)
        self.setWindowTitle("Welcome to Polygons with PyQt")
        self.setStyleSheet("background-color: azure;")
        self.initUI()

    def initUI(self):
        m = PlotCanvas(self, width=8, height=7)
        m.move(0,0)

        btn = QPushButton('Quit', self)
        btn.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn.clicked.connect(self.close_window)
        btn.move(825,500)
        btn.resize(150,100)

        btn2 = QPushButton('Draw a polygon', self)
        btn2.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn2.clicked.connect(self.open_window)
        self.dialogs = list()
        btn2.move(825,50)
        btn2.resize(150,100)

        btn3 = QPushButton('Draw a circle', self)
        btn3.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn3.clicked.connect(self.open_form)
        self.forms = list()
        btn3.move(825,200)
        btn3.resize(150,100)

        btn4 = QPushButton('Multiple plots', self)
        btn4.setStyleSheet('QPushButton {background-color: midnightblue; font: 15px; color: gold; border-style: outset;}')
        btn4.clicked.connect(self.open_fourth)
        self.forms = list()
        self.fourth = list()
        btn4.move(825,350)
        btn4.resize(150,100)

        self.show()

    def close_window(self):
        choice = QMessageBox.question(self,'Close',"Wanna exit?",QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing now.....")
            sys.exit()
        else:
            pass

    def open_window(self):
        dialog = Second()
        self.dialogs.append(dialog)
        dialog.show()

    def open_form(self):
        form = Third()
        self.forms.append(form)
        form.show()

    def open_fourth(self):
        four = Fourth()
        self.fourth.append(four)
        four.show()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None, width=8, height=8):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.set_title('Welcome to Polygons with PyQt')
        circle1 = plt.Circle((2.5,7.5), 2.5, color = 'maroon', fill = False )
        circle2 = plt.Circle((7.5, 2.5), 2.5, color = 'maroon', fill = False )
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        p = [0,0,5,5,0,5,5,10,10,5]
        q = [0,5,5,0,0,0,10,10,5,5]

        ax.axes.plot(p,q,color = 'navy')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())