# -*- coding: utf-8 -*-
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QToolBox, QGroupBox, QToolButton, QVBoxLayout


class Demo(QToolBox):                                           # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox(self)                       # 2
        self.groupbox_2 = QGroupBox(self)
        self.groupbox_3 = QGroupBox(self)

        self.toolbtn_f1 = QToolButton(self)                     # 3
        self.toolbtn_f2 = QToolButton(self)
        self.toolbtn_f3 = QToolButton(self)
        self.toolbtn_m1 = QToolButton(self)
        self.toolbtn_m2 = QToolButton(self)
        self.toolbtn_m3 = QToolButton(self)

        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.v3_layout = QVBoxLayout()

        self.addItem(self.groupbox_1, "Couple One")             # 4
        self.addItem(self.groupbox_2, "Couple Two")
        self.addItem(self.groupbox_3, "Couple Three")
        self.currentChanged.connect(self.print_index_func)      # 5

        self.layout_init()
        self.groupbox_init()
        self.toolbtn_init()

    def layout_init(self):
        self.v1_layout.addWidget(self.toolbtn_f1)
        self.v1_layout.addWidget(self.toolbtn_m1)
        self.v2_layout.addWidget(self.toolbtn_f2)
        self.v2_layout.addWidget(self.toolbtn_m2)
        self.v3_layout.addWidget(self.toolbtn_f3)
        self.v3_layout.addWidget(self.toolbtn_m3)

    def groupbox_init(self):                                    # 6
        self.groupbox_1.setFlat(True)
        self.groupbox_2.setFlat(True)
        self.groupbox_3.setFlat(True)
        self.groupbox_1.setLayout(self.v1_layout)
        self.groupbox_2.setLayout(self.v2_layout)
        self.groupbox_3.setLayout(self.v3_layout)

    def toolbtn_init(self):                                     # 7
        self.toolbtn_f1.setIcon(QIcon("../../icons/apple.svg"))
        self.toolbtn_f2.setIcon(QIcon("../../icons/apple.svg"))
        self.toolbtn_f3.setIcon(QIcon("../../icons/apple.svg"))
        self.toolbtn_m1.setIcon(QIcon("../../icons/apple.svg"))
        self.toolbtn_m2.setIcon(QIcon("../../icons/apple.svg"))
        self.toolbtn_m3.setIcon(QIcon("../../icons/apple.svg"))

    def print_index_func(self):
        couple_dict = {
            0: "Couple One",
            1: "Couple Two",
            2: "Couple Three"
        }
        sentence = "You are looking at {}.".format(couple_dict.get(self.currentIndex()))
        print(sentence)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 因为要显示的最终控件也就是QToolBox，所以这里就直接继承QToolBox；

2. 实例化三个QGroupBox控件，目的是将6个头像分别放入这三个QGroupBox中；

3. QToolButton用于显示头像；

4. 通过addItem(QWidget, Str)方法将QGroupBox添加到QToolBox中，第一个参数为要添加的控件，第二个参数是给每个QToolBox抽屉设定的名称；

5. 每当用户点击不同抽屉时，都会触发currentChanged信号，我们将该信号连接到自定义的槽函数上：
通过currentIndex()方法可以获取到当前所点击的抽屉序号，序号从0开始。这里通过字典来获取相应的抽屉名称，然后将其打印出来；

6. setFlat(True)方法可以让QGroupBox的边框消失；

7. 通过setIcon(QIcon)方法来设置QToolButton的图标；

小结:
QGroupBox组合框和QToolBox工具箱可以很好的用来将界面各部分控件进行归类，让界面更加友好，从而提高用户体验度；

不同QGroupBox中的单选按钮QRadioButton互不影响；

 QToolBox可以用addItem(QWidget, Str)方法来添加抽屉，每一个抽屉都是一个控件。当用户点击不同抽屉时，会触发currentChanged信号。
"""