# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel("QTextEdit", self)
        self.browser_label = QLabel("QTextBrowser", self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)  # 1

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())  # 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 将self.text_edit的textChanged信号连接到自定义的槽函数上。也就是说当self.text_edit中的文本发生改变的时候，
    就会发出textChanged信号，然后调用show_text_func()槽函数。

2. 在槽函数中我们通过setText()方法将self.text_browser的文本设为self.text_edit的文本，
    而self.text_edit的文本通过toPlainText()获取，而不是text().
    
3. 顾名思义，QTextEdit为用来编辑文本，而QTextBrowser用来显示文本；

4. setText()用来设置文本，toPlainText()用来获取文本，这两个控件都有这些方法；

5. 浏览框会执行Html代码。
"""
