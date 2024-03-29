# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.lcd_1 = QLCDNumber(self)                                   # 1
        self.lcd_1.setDigitCount(10)
        self.lcd_1.display(1234567890)

        self.lcd_2 = QLCDNumber(self)                                   # 2
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        # self.lcd_2.setSmallDecimalPoint(True)
        self.lcd_2.setDigitCount(10)
        self.lcd_2.display(0.123456789)

        self.lcd_3 = QLCDNumber(self)                                   # 3
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display("HELLO")

        self.lcd_4 = QLCDNumber(self)                                   # 4
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd_4.setMode(QLCDNumber.Hex)
        self.lcd_4.setDigitCount(6)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)

        self.setLayout(self.v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化一个QLCDNumber控件，然后通过setDiditCount()方法来设置一共可以显示多少为数字；

2. lcd_2显示浮点型数字。通过setSegmentStyle()可以设置显示屏数字样式，可传入的参数有：
    QLCDNumber.Outline  QLCDNumber.Filled   QLCDNumber.Flat
    setSmallDecimalPoint(bool)方法可以设置小数点的显示方式：若为True，那么小数点就会在两个数字之间显示出来，而不会单独占一个位置。
    如果为False，那就会单独占位(默认为False)。

3. lcd_3显示的为字符串，可以显示的字母种类有限：A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, O/0, S/5, g/9；

4. 可以通过setMode()方法来更改数字显示方式，这里用传入QLCDNumber.Hex让数字以16进制方式显示，总共可以传入以下参数：
    QLCDNumber.Hex  QLCDNumber.Dec  QLCDNumber.Oct  QLCDNumber.Bin
    
setDigitCount(int)用于设置可显示位数；setSegmentStyle()用于设置样式；setMode()用于设置数字显示方式；display()用于显示
"""
