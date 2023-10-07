# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QPushButton, QGridLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.clipboard = QApplication.clipboard()                               # 1
        self.clipboard.dataChanged.connect(lambda: print('Data Changed'))

        self.copy_btn = QPushButton('Copy', self)                               # 2
        self.copy_btn.clicked.connect(self.copy_func)

        self.paste_btn = QPushButton('Paste', self)                             # 3
        self.paste_btn.clicked.connect(self.paste_func)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.text_edit, 0, 0, 1, 1)
        self.g_layout.addWidget(self.text_browser, 0, 1, 1, 1)
        self.g_layout.addWidget(self.copy_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.paste_btn, 1, 1, 1, 1)
        self.setLayout(self.g_layout)

    def copy_func(self):
        self.clipboard.setText(self.text_edit.toPlainText())

    def paste_func(self):
        self.text_browser.setText(self.clipboard.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化一个剪贴板，并将其dataChanged信号和打印函数连接起来。每当剪贴板内容发生变化的时候，都会触发dataChanged信号。
    在这里也就是说每当发生变化，控制台都会打印出Data Changed；
    
2. 当点击copy_btn后，槽函数copy_func()就会启动：在槽函数中，我们将text_edit中的文本获取过来并通过setText()方法将其设置为剪贴板的文本；

3. 当点击paste_btn后，槽函数paste_func()启动：在槽函数中，我们将text_browser的文本设为剪贴板的文本。当然该槽函数还有另一种实现方法：
"""

"""
1. 使用QMimeData类来处理MIME类型数据；

. 拖放事件一共有四种，分别在拖动目标进入窗口或部件时、目标进入后继续被拖动时、目标离开窗口或控件时以及目标被放下时；

2. 剪贴板的内容发生变化的话，则会触发dataChanged信号。剪贴板针对不同数据类型有相应获取和设置的方法。
"""