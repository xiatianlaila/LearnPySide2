# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Signal, QPoint
from PySide2.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    # my_signal = Signal(int)             # 1
    # my_signal = Signal(int, int)
    my_signal = Signal(QPoint)

    def __init__(self):
        super(Demo, self).__init__()
        self.my_signal.connect(self.signal_slot)

    def signal_slot(self, pos):           # 2
        print("信号发射成功")
        # print(x)
        # print(y)
        print(pos)

    def mouseDoubleClickEvent(self, event):
        # pos_x = event.pos().x()         # 3
        # pos_y = event.pos().y()
        # self.my_signal.emit(pos_x, pos_y)
        pos = event.pos()
        self.my_signal.emit(pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
发送鼠标双击点的横坐标

1. 首先在实例化Signal对象时传入一个int参数，表明我们这个信号会携带一个整型值，而这个值将会被槽函数接收。

2. 给槽函数添加一个接收参数x，并在函数内部打印该值。

3. 在获取到横坐标后，通过emit方法发射出去就行了。

除了int类型，我们还可以让自定义信号携带其他类型的值，包括python语言所支持的值类型和PyQt5自定义的数据类型。
"""
