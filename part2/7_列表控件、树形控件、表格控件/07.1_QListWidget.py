# -*- coding: utf-8 -*-
"""
列表控件可以让我们以列表形式呈现内容，使界面更加有序美观。QListWidget列表控件应当与QListWidgetItem一起使用，后者作为项被添加入列表控件中，
也就是说列表控件中的每一项都是一个QListWidgetItem。这也是为什么我们说QListWidget是一个基于项(Item-based)的控件了。

同样基于项的控件还有QTreeWidget树形控件和QTableWidget表格控件，前者以树状方式呈现内容，并与QTreeWidgetItem搭配使用；
后者以表格形式呈现内容，并与QTableWidgetItem一起使用。
"""
import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Demo(QWidget):
    def __int__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)                       # 1
        self.pic_label.setPixmap(QPixmap('arrow.png'))

        self.listwidget_1 = QListWidget(self)               # 2
        self.listwidget_2 = QListWidget(self)














if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())