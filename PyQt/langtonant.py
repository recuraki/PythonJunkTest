#!/usr/bin/env python
# coding: utf-8

windowX, windowY = 300,300

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QImage
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5 import QtCore

dx = [0 , 1, 0, -1]
dy = [-1, 0, 1, 0]


class Ant():
    def __init__(self):
        self.x = int(0)
        self.y = int(0)
        self.dir = 0

    def rotateLeft(self):
        self.dir = (self.dir - 1) % len(dx)

    def rotateRight(self):
        self.dir = (self.dir + 1) % len(dx)

    def move(self):
        #print(self.y, self.x, self.dir)
        if maze[self.y][self.x] == 0:
            maze[self.y][self.x] = 1
            self.rotateRight()
        else:
            maze[self.y][self.x] = 0
            self.rotateLeft()

        self.x += dx[self.dir]
        self.y += dy[self.dir]

        #print(",", self.y, self.x, self.dir)
        if self.x < 0:
            self.x = windowX - 1
        if self.y < 0:
            self.y = windowY - 1
        if self.x > windowX - 1:
            self.x = 0
        if self.y > windowY - 1:
            self.y = 0

    def getPos(self):
        return (self.x, self.y)



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(windowX, windowY)
        self.move(300, 300)
        self.setWindowTitle('1Dim Cell Auto')
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        # 表示
        self.show()

    # paint event
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def do(self):
        qp = QPainter(self.image)
        qp.begin(self)
        for ant in ants:
            for loop in range(300):
                x, y = ant.getPos()
                ant.move()
                qp.setPen(Qt.white if maze[y][x] == 0 else Qt.red)
                qp.drawPoint(x, y)

        qp.end()
        self.update()

maze = []
for i in range(windowY):
    maze.append([0] * windowX)
countAnt = 1
ants = []
for i in range(countAnt):
    ants.append(Ant())
ants[0].x = windowX // 2
ants[0].y = windowY // 2
ants[0].dir = 0


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = MyWidget()

    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(ew.do)
    timer.start(10)

    sys.exit(app.exec_())

