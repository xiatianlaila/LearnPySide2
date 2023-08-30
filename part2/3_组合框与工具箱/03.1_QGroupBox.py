# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox("On and Off", self)                       # 1
        self.groupbox_2 = QGroupBox("Change Color", self)

        self.red = QRadioButton("Red", self)                                  # 2
        self.blue = QRadioButton("Blue", self)
        self.green = QRadioButton("Green", self)
        self.yellow = QRadioButton("Yellow", self)
        self.color_list = [self.red, self.blue, self.green, self.yellow]

        self.on = QRadioButton("On", self)                                    # 3
        self.off = QRadioButton("Off", self)

        self.pic_label = QLabel(self)                                         # 4

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        self.groupbox_1.setLayout(self.h1_layout)

        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_v_layout.addWidget(self.pic_label)
        self.all_v_layout.addLayout(self.h3_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):                                              
        self.yellow.setChecked(True)                                         # 5
        for btn in self.color_list:
            btn.clicked.connect(self.change_color_func)

        self.off.setChecked(True)                                            # 6
        self.off.toggled.connect(self.on_and_off_func)

    def label_init(self):                                                    # 7
        self.pic_label.setPixmap(QPixmap("../../icons/off.svg"))
        self.pic_label.setAlignment(Qt.AlignCenter)

    def change_color_func(self):
        """
        在下面这个槽函数中，我们先判断On单选按钮是否是已点击状态(因为如果电源没开的话，灯泡颜色是不会变化的) ，
        如果是的话则获取图片路径path，然后将QLabel设为相应的图片，这里我们详细分析下。
        """
        if self.on.isChecked():
            # 首先以下列表推导式循环判断是哪一个颜色按钮处于点击状态，然后将该按钮的显示文本获取过来。
            path = "../../icons/{}.svg".format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            # 接着将相应的颜色放进字符串中 ，比如Red单选按钮处于点击状态，则path为"../../icons/red.svg"。
            self.pic_label.setPixmap(QPixmap(path))

    def on_and_off_func(self):
        if self.on.isChecked():
            path = "../../icons/{}.svg".format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap("../../icons/off.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化两个QGroupBox组合框，第一个用来放置On和Off单选按钮，第二个用来放置各种颜色按钮；

2. 实例化各个颜色按钮，并将它们放在一个列表中，方便之后使用列表推导式来简化代码；

3. 实例化On和Off单选按钮；

4. 实例化一个QLabel控件，用于显示图片；

5. 在radiobutton_init()函数中，我们先将yellow单选按钮设置为已点击状态，
    然后用各个颜色按钮的clicked信号与自定义的槽函数change_color_func()连接起来。
    
6. 将Off按钮设为点击状态，然后将它的toggled信号与自定义的槽函数连接起来(槽函数原理与5中类似，不再讲解)；

7. 将刚开始显示的QLabel图片设置为Off.png，然后让其居中显示。
"""