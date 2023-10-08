# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QTableWidget, QTableWidgetItem


class Demo(QTableWidget):                               # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.setRowCount(6)                             # 2
        self.setColumnCount(6)
        # self.table = QTableWidget(6, 6, self)

        print(self.)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())