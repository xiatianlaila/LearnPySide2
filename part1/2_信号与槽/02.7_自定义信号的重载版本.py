# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    # press_signal = Signal(int)
    # release_signal = Signal(tuple)
    mouse_signal = Signal([int], [tuple])       # 1


    def __init__(self):
        super(Demo, self).__init__()
        # self.press_signal.connect(self.press_slot)
        # self.release_signal.connect(self.release_slot)
        self.mouse_signal[int].connect(self.press_slot)     # 2
        self.mouse_signal[tuple].connect(self.release_slot)


    def press_slot(self, x):
        print(x)

    def release_slot(self, pos):
        print(pos)

    def mousePressEvent(self, event):           # 3
        x = event.pos().x()
        # self.press_signal.emit(x)
        self.mouse_signal[int].emit(x)

    def mouseReleaseEvent(self, event):
        pos_x = event.pos().x()
        pos_y = event.pos().y()
        pos = (pos_x, pos_y)
        # self.release_signal.emit(pos)
        self.mouse_signal[tuple].emit(pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
当鼠标按下时，打印出横坐标；当鼠标释放时，打印出横坐标和纵坐标

1. 实例化一个pyqtSignal对象，并将参数用中括号[]包住，每一个中括号代表了该信号的一种形式，
    也就是说mouse_signal一共有两种形式，既可以携带一个整型值，也可以一个元组
    
2. 将信号与槽函数进行连接，注意这里一定要明确所连接信号的重载类型。

3. 同样，在发射信号时，也要写清楚重载类型。如果在连接和发射时不写清楚重载类型的话，则默认使用第一种。
"""
