# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("Username:", self)
        self.user_line = QLineEdit(self)                # 1

        self.h_layout = QHBoxLayout()                   # 2
        self.h_layout.addWidget(self.user_label)        # 3
        self.h_layout.addWidget(self.user_line)         # 4

        self.setLayout(self.h_layout)                   # 5


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. QLineEdit控件就是一个用来进行单行文本输入的框；

2. 实例化一个水平布局管理器；

3-4. 将QLabel和QLineEdit控件添加到水平布局管理器中，先添加的出现在左边；

5. 将self.h_layout设为整个窗口的最终布局方式。
"""
