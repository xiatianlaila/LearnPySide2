# -*- coding: utf-8 -*-
import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.off_button = QRadioButton("off", self)                 # 1
        self.on_button = QRadioButton("on", self)                   # 2

        self.pic_label = QLabel(self)                               # 3

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.pic_h_layout.addStretch(1)                             # 4
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.off_button.setChecked(True)                            # 5
        self.off_button.toggled.connect(self.on_off_bulb_func)      # 6

    def label_init(self):
        self.pic_label.setPixmap(QPixmap("../../icons/off.svg"))    # 7

    def on_off_bulb_func(self):                                     # 8
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap("../../icons/off.svg"))
        else:
            self.pic_label.setPixmap(QPixmap("../../icons/on.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1-2. 实例化两个单选按钮，一个off，另一个为on；

3. 这里准备用QLabel控件来显示图片；

4. 在管理布局的函数中有一个addStretch(int)方法，该方法就是添加一个占位符，而占位符的大小就是其中填入的数字。
    我们可以看到在示例中先添加了一个大小为1的占位符，然后再添加用于显示图片的QLabel，
    最后再加了一个大小为1的占位符。这样做的目的就是为了让这个QLabel控件居中。
    若将添加的第一个占位符(即左边的占位符)大小设为2，那么QLabel就会偏右，因为左边的占位符大小比QLabel右边的占位符大；

5. 将off单选按钮设为选中状态；

6. 若单选按钮的状态发生改变，则会发出toggled信号。在这里将toggled信号和自定义的槽函数进行连接；

7. 初始状态灯泡是不亮的，所以通过setPixmap()给QLabel设置off.svg，即灯泡不亮的图片。setPixmap()方法接受一个QPixmap()对象；

8. 在该槽函数中，我们判断off按钮是否处于选中状态，若是，则灯泡不亮，否则给QLabel设置灯泡发亮的图片。



在上方radiobutton_init()函数中，我们只给off_button连接了信号和槽，而on_button没有。
正如开始时提到的一点：默认每次只有一个单选按钮会被选中，而这里只有两个按钮，所以一个按钮的状态发生变化，另一个必然也会。
"""