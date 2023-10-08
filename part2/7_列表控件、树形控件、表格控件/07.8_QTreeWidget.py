# -*- coding: utf-8 -*-
import os
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 300)
        self.label = QLabel('No Click')                         # 1

        self.tree = QTreeWidget(self)                           # 2
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Install Components', 'Test'])
        self.tree.itemClicked.connect(self.change_func)

        self.preview = QTreeWidgetItem(self.tree)               # 3
        self.preview.setText(0, 'Preview')

        # self.preview = QTreeWidgetItem()
        # self.preview.setText(0, 'Preview')
        # self.tree.addTopLevelItem(self.preview)

        self.qt5112 = QTreeWidgetItem()                         # 4
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.qt5112.setCheckState(0, Qt.Unchecked)
        self.preview.addChild(self.qt5112)

        choice_list = ['macOS', 'Android x86', 'Android ARMv7', 'Sources', 'iOS']
        self.item_list = []
        for i, c in enumerate(choice_list):                     # 5
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)           # 6
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')

        self.tree.expandAll()                                   # 7

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_func(self, item, column):
        self.label.setText(item.text(column))                   # 8

        print(item.text(column))
        print(column)
        if item == self.qt5112:                                 # 9
            if self.qt5112.checkState(0) == Qt.Checked:
                [x.setCheckState(0, Qt.Checked) for x in self.item_list]
            else:
                [x.setCheckState(0, Qt.Unchecked) for x in self.item_list]
        else:                                                   # 10
            check_count = 0
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_count += 1

                if check_count == 5:
                    self.qt5112.setCheckState(0, Qt.Checked)
                elif 0 < check_count < 5:
                    self.qt5112.setCheckState(0, Qt.PartiallyChecked)
                else:
                    self.qt5112.setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. QLabel控件用于显示每个QTreeWidgetItem的文本；

2. 实例化一个QTreeWidget，通过setColumnCount(int)将该树状控件的列数设为2(默认为1列)。
    通过setHeaderLabels(Iterable)设置每列的标题，如果只有一列的话，则应该通过setHeaderLabel(str)方法设置。
    接着我们将itemClicked信号与自定义的槽函数连接起来，每当点击QTreeWidget中的任意一项时，
    都会触发itemClicked信号。QtAssistant中对该信号的说明如下：
    我们发现这是一个带参数的信号，而文档中解释说：每当一项内容被点击时，参数item就是被点击的项，参数column就是被点击项所在的列。
    也就是说当该信号被触发时，参数item保存被点击的项，column保存列数，而这两个参数会自动传给我们的槽函数。
    为与之对应，我们的槽函数也带了两个参数，这样我们就可以知道被点击的项和列数了。
    
3. 实例化一个QTreeWidgetItem，并将其父类设为self.tree，表示self.preview为最外层(最顶层)的项，
    接着通过setText(int, str)方法来设置文本，第一个int类型参数为该文本所在的列，0表示放在第一列。
    当然我们也可以在实例化时不指定父类，并让self.tree调用addTopLevelItem()方法来设置最顶层的项；
    
4. setCheckState(int, CheckState)方法可以让该项以复选框形式呈现出来，addChild(QTreeWidgetItem)方法可以添加子项，
    这里让self.preview添加一个self.qt5112选项；
    
5. 实例化5个子项，将他们添加到self.qt5112中，并以复选框形式显示；

6. 这里的self.test项只是拿来作为对比，好让读者知道将QTreeWidget设为两列时的样子；

7. 调用expandAll()方法可以让QTreeWidget所有的项都是以打开状态显示的。注意必须要在所有项都已经实例化好之后再调用该方法，如果一开始就调用则会没有效果；

8. 在槽函数中，self.label显示对应的项文本，item就是被点击的项，我们调用text(int)传入列数，获得文本(该text()函数用法跟我们之前使用的有所不同)。

9. 如果被点击的项为qt5112，则我们判断是否其被选中，若是的话，将它的所有子项都设为选中状态，若为无选中状态的话，则将其子项全部设为无选中状态；

10. 若被点击是qt5112的子项时，我们判断有多少个子项已经被选中了，若数量为5，则设置qt5112为选中状态，若为0-5之间，则设为半选中状态，若等于0，则设为无选中状态。
"""