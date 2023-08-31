# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)  # 1
        self.pic_label.setPixmap(QPixmap("../../icons/keyboard.png"))
        self.pic_label.setAlignment(Qt.AlignCenter)

        self.key_label = QLabel("No Key Pressed", self)  # 2
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):  # 3
        if QKeyEvent.key() == Qt.Key_Up:
            self.pic_label.setPixmap(QPixmap("../../icons/keyboard_key_a.png"))
            self.key_label.setText("Key Up Pressed")
        elif QKeyEvent.key() == Qt.Key_Down:
            self.pic_label.setPixmap(QPixmap("../../icons/keyboard_key_a.png"))
            self.key_label.setText("Key Down Pressed")
        elif QKeyEvent.key() == Qt.Key_Left:
            self.pic_label.setPixmap(QPixmap("../../icons/keyboard_key_a.png"))
            self.key_label.setText("Key Left Pressed")
        elif QKeyEvent.key() == Qt.Key_Right:
            self.pic_label.setPixmap(QPixmap("../../icons/keyboard_key_a.png"))
            self.key_label.setText("Key Right Pressed")

    def keyReleaseEvent(self, QKeyEvent):  # 4
        self.pic_label.setPixmap(QPixmap("../../icons/keyboard.png"))
        self.key_label.setText("Key Released")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. pic_label用于设置图片，先将初始化的图片设为keyboard.png；

2. key_label用于记录按键状态；

3. keyPressEvent()为键盘某个键被按下时所触发的响应函数，在这个函数中我们判断被按下的键种类，
    并将pic_label设为相应的箭头图片，将key_label设为相应的文本；

4. keyReleasedEvent()在键盘上的任意键被释放时所触发的响应函数，在这个函数中，我们将pic_label设为初始图片keyboard.png，
    并将key_label文本设为‘Key Released'。
"""