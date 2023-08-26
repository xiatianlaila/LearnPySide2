# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 1
        self.setWindowTitle("demo")                             # 2
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)    # 3
        self.button.clicked.connect(self.change_window_title)   # 4

    def change_text(self):
        print("change text")
        self.button.setText("Stop")
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):                               # 5
        print("change window size")
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):                              # 6
        print("change window title")
        self.setWindowTitle("window title changed")
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 首先在初始化函数中将窗口大小设置为宽300，长300；

2. 其次将窗口名称设置为‘demo’；

3-4. 信号和槽连接，可以看到信号还是clicked，而槽函数多了两个；

5. 修改窗口大小的槽函数；

6. 修改窗口名称的槽函数；

现在运行点击按钮后，按钮文本会由‘Start’变为‘Stop’，窗口大小从(300, 300)变为(500, 500)，窗口标题由‘demo’变为‘window title changed’
"""