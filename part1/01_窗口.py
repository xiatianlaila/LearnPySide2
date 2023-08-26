# -*- coding: UTF-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)     # 1
    label = QLabel("Hello Pyside2")  # 2
    # label.setText(”Hello World“)
    # label = QLabel('<font color="red">Hello</font> <h1>World</h1>')
    label.show()                     # 3
    sys.exit(app.exec_())            # 4

"""
1. 想要创建应用必须先实例化一个QApplication，并将sys.argv作为参数传入；
2. 实例化一个QLabel控件，该控件用来展示文字或图片(可以想象下衣服标签，上面既有文字也有图片)，这里用于展示文本。
可以像上方代码一样直接传入"Hello Pyside2"进行实例化，也可以先实例化，再调用setText()方法来设置文本：
3. 通过调用show()方法使控件可见(默认是隐藏)；
4. app.exec_()是执行应用，让应用开始运转循环，直到窗口关闭返回0给sys.exit()，退出整个程序。 有些小伙伴可能发现还有exec()，
在Python2中exec是关键字，所以PySide2就使用exec_()而不是exec() 。
不过exec在Python3中已经不再是关键字了，所以如果读者使用的是Python3的话那在上述代码中用exec()也完全没关系。
"""

"""
小结：
1. QLabel是文本控件，但是也可以用来展示图片(在之后章节讲解)；

2. 可以直接在字符串中添加html代码；

3. app.exec_()用来执行应用，sys.exit()退出程序(exec就是英文当中的execute【执行】的缩写，这样记就容易了)。
"""