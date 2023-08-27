# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QFormLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel("Username:", self)
        self.pwd_label = QLabel("Password:", self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton("Log in", self)
        self.signin_button = QPushButton("Sign in", self)

        self.f_layout = QFormLayout()                           # 1
        self.button_h_layout = QHBoxLayout()                     
        self.all_v_layout = QVBoxLayout()                        

        self.f_layout.addRow(self.user_label, self.user_line)   # 2
        self.f_layout.addRow(self.pwd_label, self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)
        self.all_v_layout.addLayout(self.f_layout)              # 3
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化一个QFormLayout控件；

2. 调用addRow()方法传入QLabel和QLineEdit控件；

3. 将表单布局添加到总布局中。

表单布局可以将控件以两列的形式进行排布，左列控件为文本标签，右列为输入型的控件，如QLineEdit。

可以发现代码比之前的更加简洁了。
"""