# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QApplication, QWidget, QTextBrowser, QLineEdit, QPushButton, QHBoxLayout


class Window1(QTextBrowser):            # 1
    def __init__(self):
        super(Window1, self).__init__()

    def show_msg_slot(self, msg):
        self.append(msg)


class Window2(QWidget):                 # 2
    win2_signal = Signal(str)

    def __init__(self):
        super(Window2, self).__init__()
        self.line = QLineEdit()
        self.send_btn = QPushButton("发送")
        self.send_btn.clicked.connect(self.send_to_win1_slot)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.line)
        h_layout.addWidget(self.send_btn)
        self.setLayout(h_layout)

    def send_to_win1_slot(self):
        msg = self.line.text()
        self.win2_signal.emit(msg)


if __name__ == "__main__":              # 3
    app = QApplication(sys.argv)

    win1 = Window1()
    win1.show()

    win2 = Window2()
    win2.show()
    win2.win2_signal.connect(win1.show_msg_slot)

    sys.exit(app.exec_())

"""
1. 窗口一继承于QTextBrowser，类中有一个槽函数，它会将信号带过来的值添加到窗口上。

2. 窗口2实例化了一个自定义信号，该信号会携带一个字符串。每当用户点击发送按钮后，窗口二会将输入框中的文本随信号一同发射出去。

3. 在程序入口处，我们实例化了窗口一和窗口二，并将窗口二的信号同窗口一的槽函数连接起来。
    也就是说，每当用户在窗口二点击了发送按钮后，窗口一就会将输入框的文本显示到自己的界面上。
"""
