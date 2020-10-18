#!/usr/bin/env python
# coding: utf-8

# 完全に以下のコード
# https://qiita.com/montblanc18/items/0188ff680acf028d4b63

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5 import QtCore


class MyWidget(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()
        print("fo")

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('sample')

        # buttonの設定
        self.button = QPushButton('Clear!!')
        self.label = QLabel('connected')

        # buttonのclickでラベルをクリア
        self.button.clicked.connect(self.label.clear)

        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.grid.addWidget(self.label, 1, 0, 1, 2)
        self.setLayout(self.grid)

        # 表示
        self.show()


def timerEvent():
    global time
    time = time.addSecs(1)
    print(time.toString("hh:mm:ss"))
    ew.label.setText('Label Example')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ew = MyWidget()

    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(timerEvent)
    timer.start(1000)

    sys.exit(app.exec_())
