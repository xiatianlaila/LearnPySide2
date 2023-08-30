# -*- coding: utf-8 -*-
"""
https://zhuanlan.zhihu.com/p/86963699   重点看
"""
import sys
from PySide2.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(200, 200)                    # 1
    widget.move(100, 100)                      # 2
    # widget.setGeometry(100, 100, 200, 200)   # 3
    widget.show()

    print("-----------------x(), y(), pos()-----------------")
    print(widget.x())
    print(widget.y())
    print(widget.pos())

    print("-----------------width(), height()-----------------")
    print(widget.width())
    print(widget.height())

    print("-----------------geometry().x(), geometry.y(), geometry()-----------------")
    print(widget.geometry().x())
    print(widget.geometry().y())
    print(widget.geometry())

    print("-----------------geometry.width(), geometry().height()-----------------")
    print(widget.geometry().width())
    print(widget.geometry().height())

    print("-----------------frameGeometry().x(), frameGeometry().y(), frameGeometry(), "
          "frameGeometry().width(), frameGeometry().height()-----------------")
    print(widget.frameGeometry().x())
    print(widget.frameGeometry().y())
    print(widget.frameGeometry())
    print(widget.frameGeometry().width())
    print(widget.frameGeometry().height())

    sys.exit(app.exec_())

"""
x()——得到窗口左上角在显示屏屏幕上的x坐标；
y()——得到窗口左上角在显示屏屏幕上的y坐标；
pos()——得到窗口左上角在显示屏屏幕上的x和y坐标，类型为QPoint()；
geometry().x()——的到客户区左上角在显示屏屏幕上的x坐标；
geometry().y()——的到客户区左上角在显示屏屏幕上的y坐标；
geometry()——的到客户区左上角在显示屏屏幕上的x和y坐标，以及客户区的宽度和长度，类型为QRect()；
width()——得到客户区的宽度；
height()——得到客户区的长度；
geometry().width()——得到客户区的宽度；
geometry().height()——得到客户区的长度；
frameGeometry().width()——得到窗口的宽度；
frameGeometry().height()——得到窗口的长度；
frameGeometry().x()——即x()，得到窗口左上角在显示屏屏幕上的x坐标；
frameGeometry().y()——即y()，得到窗口左上角在显示屏屏幕上的y坐标；
frameGeometry()——即pos()，得到窗口左上角在显示屏屏幕上的x和y坐标，以及窗口的宽度和长度，类型为QRect()；
"""

"""
1. 窗口可分为标题栏、边框和客户区三个部分。但是从Linux系统上的输出结果来看，
    在Linux上的窗口并没有将窗口划分为是那个部分，而是始终保持一个整体。Mac上的窗口也没有边框这一部分；

2. move(x, y)和resize(width, height)方法的功能可以单单通过setGeometry(x, y, width, height)方法来实现
    (我们也可以用该方法实现窗口中各控件的布局)。
"""