# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.checkbox1 = QCheckBox("Checkbox 1", self)
        self.checkbox2 = QCheckBox("Checkbox 2", self)
        self.checkbox3 = QCheckBox("Checkbox 3", self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        self.checkbox1.setChecked(True)                                                             # 1
        # self.checkbox1.setCheckState(Qt.Checked)                                                  # 2
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))      # 3

        self.checkbox2.setChecked(False)
        # self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        self.checkbox3.setTristate(True)                                                            # 4
        self.checkbox3.setCheckState(Qt.PartiallyChecked)                                           # 5
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))      

    def on_state_change_func(self, checkbox):                                                       # 6
        print("{} was clicked, and its current state is {}".format(checkbox.text(), checkbox.checkState()))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. QPushButton和QToolButton非常相似，不过QToolButton更多是与QToolBar搭配使用，用来显示工具图片；

2. 可以通过setIcon()方法来给按钮设置图标；可以用setPixmap()方法给QLabel控件设置图片；

3. toggled信号在按钮状态发生改变时发出；stateChanged也是，不过该信号用于QCheckBox；

4. QRadioButton单选按钮只能进行多选一操作，即每次只会有一个单选按钮被选中；

5. 如果要让QCheckBox拥有三种状态的话，则需要通过setTristate(True)方法来设置；

6. 若要连接带有参数的自定义槽函数，可以通过lambda表达式来完成。
"""