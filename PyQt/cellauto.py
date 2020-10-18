#!/usr/bin/env python
# coding: utf-8

windowX, windowY = 700, 700

rule = [0] * 8
rule = [0, 1, 1, 1, 1, 0, 0, 0]

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(windowX, windowY)
        self.move(300, 300)
        self.setWindowTitle('1Dim Cell Auto')
        # 表示
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):
        # 赤ペンを用意
        qp.setPen(Qt.red)
        qp.drawPoint(1,1)
        # ウィンドウサイズをセットする（サイズが変わるとpaintEventが発生）
        size = self.size()
        windowX, windowY = size.width(), size.height()
        centerx = windowX // 2

        datMaster = [0] * windowX
        datMaster[centerx] = 1 # 初期位置
        dat2 = [0] * windowX

        for hh in range(0, windowY):
            h = hh + 1
            for i in range(centerx - h, centerx + h + 1):
                if i == 0 or i == (windowY - 1):
                    return
                ruleind = datMaster[i-1] * 4 + datMaster[i] * 2 + datMaster[i+1] * 1
                dat2[i] = rule[ruleind]
                if dat2[i] == 1:
                    qp.drawPoint(i, hh)
            datMaster, dat2 = dat2, datMaster

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = MyWidget()

    sys.exit(app.exec_())
