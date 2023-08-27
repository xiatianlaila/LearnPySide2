# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Signal                               # 1
from PySide2.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    my_signal = Signal()                                        # 2

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel("Hello World", self)
        self.my_signal.connect(self.change_text)                # 3

    def change_text(self):
        if self.label.text() == "Hello World":
            self.label.setText("Hello Pyside2")
        else:
            self.label.setText("Hello World")

    def mousePressEvent(self, QMouseEvent):                     # 4
        self.my_signal.emit()                                   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 需要先导入Signal；

2. 实例化一个自定义的信号；

3. 将自定义的信号连接到自定义的槽函数上；

4. mousePressEvent()方法是许多控件自带的，这里来自于QWidget。该方法用来监测鼠标是否有按下。现在鼠标若被按下，则会发出自定义的信号。

详细用法：https://pyqt5.blog.csdn.net/article/details/107573344?ydreferer=aHR0cHM6Ly9saW5rLnpoaWh1LmNvbS8%2FdGFyZ2V0PWh0dHBzJTNBLy9weXF0NS5ibG9nLmNzZG4ubmV0L2FydGljbGUvZGV0YWlscy8xMDc1NzMzNDQ%3D
"""