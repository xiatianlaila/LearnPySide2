# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QTextBrowser

class Demo(QTextBrowser):                                           # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)                                   # 2

    def dragEnterEvent(self, QDragEnterEvent):                      # 3
        print('Drag Enter')
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()

    def dragMoveEvent(self, QDragMoveEvent):                        # 4
        print('Drag Move')

    def dragLeaveEvent(self, QDragLeaveEvent):                      # 5
        print('Drag Leave')


    def dropEvent(self, QDropEvent):
        print('Drag Leave')
        # MacOS
        txt_path = QDropEvent.mimeData().text().replace('file:///', '/')

        # Linux
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/').strip()

        # Windows
        txt_path = QDropEvent.mimeData().text().replace('file:///', '')

        with open(txt_path, 'r') as f:
            self.setText(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 继承QTextBrowser，也就是说下面来实现该控件的拖放事件响应函数；

2. setAcceptDrops(True)方法可以让该控件接收放下(Drop)事件

3. 当拖动目标进入QTextBrowser的那一刹那，触发dragEnterEvent事件，
    在该响应函数中，我们先判断所拖动目标的MIME类型是否为text/plain，
    若是的话则调用acceptProposedAction()方法来表明可以在QTextBrowser上进行拖放动作；
    
4. 当目标进入窗体后，如果不放下而是继续移动的话，则会触发dragMoveEvent事件；

5. 将进入控件后的目标再次拖动到控件之外时，就会触发dragLeaveEvent()事件；

6. 将目标在QTextBrowser中放下后，我们先通过QDropEvent.mimeData().text()方法获取到该文件的URI路径，
    replace()方法将其中的file:///替换为/，这样得到的值才是我们想要的本地文件路径。
    最后打开my.txt文件进行读取，并用setText()方法将QTextBrowser的文本设为该my.txt的内容。
"""