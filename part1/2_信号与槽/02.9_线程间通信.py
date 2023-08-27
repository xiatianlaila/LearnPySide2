# -*- coding: utf-8 -*-
import sys
import random
from PySide2.QtCore import Signal, QThread
from PySide2.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout


class ChildThread(QThread):
    child_signal = Signal(str)                  # 1

    def __init__(self):
        super(ChildThread, self).__init__()

    def run(self):                              # 2
        result = str(random.randint(1, 10000))
        for _ in range(100000000):
            pass

        self.child_signal.emit(result)


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.browser = QTextBrowser()           # 3
        self.btn = QPushButton("开始爬虫")
        self.btn.clicked.connect(self.start_thread_slot)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.browser)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

        self.child_thread = ChildThread()       # 4
        self.child_thread.child_signal.connect(self.child_thread_done_slot)

    def start_thread_slot(self):
        self.browser.clear()
        self.browser.append("爬虫开启")
        self.btn.setText("正在爬取")
        self.btn.setEnabled(False)
        self.child_thread.start()

    def child_thread_done_slot(self, msg):
        self.browser.append(msg)
        self.browser.append("爬取结束")
        self.btn.setText("开始爬取")
        self.btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 在子线程中实例化一个自定义信号对象，该信号会携带一个字符串。

2. 当子线程运行完毕，会将result这个随机值随信号一同发射出去。

3. 在主窗口中实例化一个QTextBrowser控件和一个按钮控件，前者用于显示子线程传递过来的信息，后者用于开启子线程。

4. 实例化子线程，并将子线程的自定义信号与child_thread_done_slot槽函数连接起来。
    每当子线程运行结束，child_signal就会被发射，而child_thread_done_slot槽函数也就会启动。
"""