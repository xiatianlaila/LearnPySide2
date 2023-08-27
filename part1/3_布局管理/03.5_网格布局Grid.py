# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel("Username:", self)
        self.pwd_label = QLabel("Password:", self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton("Log in", self)
        self.signin_button = QPushButton("Sign in", self)

        self.grid_layout = QGridLayout()                                # 1
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # addWidget(widget, row, column, rowSpan, columnSpan)
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)         # 2
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)                     
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)                       # 3
        self.v_layout.addLayout(self.h_layout)                          # 4

        self.setLayout(self.v_layout)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化一个QGridLayout布局管理器

2. QGridLayout的addWidget()方法遵循如下语法形式：

3-4. 最后，程序用垂直布局管理器将一个网格布局和一个水平布局添加进去。

当使用该布局管理器的时候，你可以把整个窗体想象成带有坐标的，然后只用把各个控件放在相应的坐标就好了
"""