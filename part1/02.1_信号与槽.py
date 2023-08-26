# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):

    def __init__(self):                                      # 1
        super(Demo, self).__init__()
        self.button = QPushButton("Start", self)             # 2
        self.button.clicked.connect(self.change_text)        # 3

    def change_text(self):
        print("change text")
        self.button.setText("Stop")                         # 4
        self.button.clicked.disconnect(self.change_text)    # 5


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()                                           # 6
    demo.show()                                             # 7
    sys.exit(app.exec_())

"""
1. 该类继承QWidget，可以将QWidget看作是一种毛坯房，还没有装修，而我们往其中放入QPushButton、QLabel等控件就相当于在装修这间毛坯房。
    类似的毛坯房还有QMainWindow和QDialog，之后章节再讲述；

2. 实例化一个QPushButton，因为继承于QWidget，所以self不能忘了(相当于告诉程序这个QPushButton是放在QWidget这个房子中的)；

3. 连接信号与槽函数。self.button就是一个控件，clicked(按钮被点击)是该控件的一个信号，connect()即连接，
    self.change_text即下方定义的函数(我们称之为槽函数)。所以通用的公式可以是：widget.signal.connect(slot)；

4. 将按钮文本从‘Start’改成‘Stop’；

5. 信号和槽解绑，解绑后再按按钮你会发现控制台不会再输出‘change text’，如果把这行解绑的代码注释掉，
    你会发现每按一次按钮，控制台都会输出一次‘change text’；

6. 实例化Demo类；

7. 使demo可见，其中的控件自然都可见(除非某控件刚开始设定隐藏)
"""