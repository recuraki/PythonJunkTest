# coding: utf-8

gridSize = 2
gridX = 200
gridY = 200
windowX, windowY = gridX*gridSize+1, gridSize*gridY+1
import sys, random
from PyQt5.QtGui import QPainter, QColor, QPen, QImage
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5 import QtCore

bgColor = Qt.black
cellLine = Qt.white
cycleSpeed = 100
dx = [0 , 1, 0, -1]
dy = [-1, 0, 1, 0]

class Ant():
    def __init__(self):
        self.x = int(0)
        self.y = int(0)
        self.dir = 0
        self.color = Qt.red

    def rotateLeft(self):
        self.dir = (self.dir - 1) % len(dx)

    def rotateRight(self):
        self.dir = (self.dir + 1) % len(dx)

    def move(self):
        if maze[self.y][self.x] == 0: # 今の自分の場所が塗られていない場合は塗って右を向く
            maze[self.y][self.x] = 1
            self.rotateRight()
        else: # 塗られている場合は消して左へ
            maze[self.y][self.x] = 0
            self.rotateLeft()

        self.x += dx[self.dir]
        self.y += dy[self.dir]
        # 上下左右をつなげる
        if self.x < 0: self.x = gridX - 1
        if self.y < 0: self.y = gridY - 1
        if self.x > gridX - 1: self.x = 0
        if self.y > gridY - 1: self.y = 0

    def getPos(self):
        return (self.x, self.y)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(windowX, windowY)
        self.move(300, 300)
        self.setWindowTitle('1Dim Cell Auto')
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(bgColor)
        self.show()

    # updateで呼ばれる
    def paintEvent(self, event):
        # 画面全域にimageを張るだけ
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def do(self):
        # image というオブジェクトに描画を開始
        qp = QPainter(self.image)
        qp.begin(self)
        for ant in ants:
            for loop in range(cycleSpeed):
                x, y = ant.getPos()
                ant.move()
                #qp.setPen(bgColor if maze[y][x] == 0 else cellLine) # 枠をcellcolot
                qp.setPen(bgColor if maze[y][x] == 0 else ant.color)  # 枠はセルの色
                qp.setBrush(bgColor if maze[y][x] == 0 else ant.color)
                qp.drawRect(x*gridSize, y*gridSize, gridSize-1, gridSize-1)
                # 1ピクセル書きたいときはこうする
                #qp.drawPoint(x, y)
        qp.end() # これで、imageに編集を書き込み
        self.update() # paintEventを呼んでimageを画面に描く

maze = [[0] * windowX for _ in range(windowY)]
countAnt = 3
ants = [Ant() for _ in range(countAnt)]
antsColorDefined = [Qt.red, Qt.blue, Qt.yellow, Qt.green]

ants[0].x = windowX // 2
ants[0].y = windowY // 2

for i in range(countAnt):
    ants.append(Ant())
    ants[i].color = antsColorDefined[i % len(antsColorDefined)]
    ants[i].dir = i % 4
    ants[i].x = ants[0].x + i*2 # サイズによっていはoverflowします
    ants[i].y = ants[0].y + i*2

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = MyWidget()

    timer = QtCore.QTimer()
    timer.timeout.connect(ew.do) # timerが発火した時のイベント
    timer.start(10) # interval(ms)

    sys.exit(app.exec_())

