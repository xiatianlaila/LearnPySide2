# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton("Start", self)
        self.button.pressed.connect(self.change_text)     # 1
        self.button.released.connect(self.change_text)    # 2

    def change_text(self):
        if self.button.text() == "Start":                 # 3
            self.button.setText("Stop")
        else:
            self.button.setText("Start")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
QPushButton还有两个信号是pressed和released，这两个信号解释如下：

pressed: 当鼠标在button上并点击左键的时候，触发信号 。
released: 当鼠标左键被释放的时候触发信号。

所以其实pressed和released两个连起来就是一个完整的clicked

1-2. 将pressed和released信号连接搭配change_text()槽函数上；

3. 若当前按钮文本为‘Start’，则将文本改为‘Stop’；若为‘Stop’，则改为‘Start’。
"""