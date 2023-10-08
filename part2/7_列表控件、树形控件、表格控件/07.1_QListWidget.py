import sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)                       # 1
        self.pic_label.setPixmap(QPixmap('arrow.png'))

        self.listwidget_1 = QListWidget(self)               # 2
        self.listwidget_2 = QListWidget(self)
        self.listwidget_1.doubleClicked.connect(lambda: self.change_func(self.listwidget_1))
        self.listwidget_2.doubleClicked.connect(lambda: self.change_func(self.listwidget_2))

        for i in range(6):                                  # 3
            text = 'Item {}'.format(i)
            self.item = QListWidgetItem(text)
            self.listwidget_1.addItem(self.item)

        self.item_6 = QListWidgetItem('Item 6', self.listwidget_1)  # 4

        self.listwidget_1.addItem('Item 7')                         # 5
        str_list = ['Item 9', 'Item 10']
        self.listwidget_1.addItems(str_list)

        self.item_8 = QListWidgetItem('Item 8')                     # 6
        self.listwidget_1.insertItem(8, self.item_8)
        # self.listwidget_1.insertItem(8, 'Item 8')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listwidget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listwidget_2)
        self.setLayout(self.h_layout)

    def change_func(self, listwidget):                              # 7
        if listwidget == self.listwidget_1:
            item = QListWidgetItem(self.listwidget_1.currentItem())
            self.listwidget_2.addItem(item)
            print(self.listwidget_2.count())
        else:
            self.listwidget_2.takeItem(self.listwidget_2.currentRow())
            print(self.listwidget_2.count())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. pic_label用于显示图片；

2. 实例化两个QListWidget，listwidget_1放在左边用于显示可选的内容，listwidget_2放在右边用于显示被双击的项。
    然后将这两个QListWidget控件的doubleClicked信号和自定义的槽函数连接起来，每当双击QListWidget中的某项时，就会触发该槽函数。

3. 循环创建六个QListWidgetItem，并通过调用addItem(QListWidgetItem)将其添加到listwidget_1中；

4. 当然也可以通过实例化时直接指定父类的方式进行添加；

5. 也可以不用QListWidgetItem，直接调用addItem(str)方法来添加一项内容。
    也可以使用addItem(Iterable)来添加一组项内容(不过若要让项呈现更多功能的话，还是应该选择QListWidgetItem)；

6. 通过insertItem(row, QListWidgetItem)方法可以在指定行中加入一项内容；
"""