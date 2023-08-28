# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import QDate, Qt
from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout

EMOTION = {  # 1 
    "周一": "(╯°Д°)╯︵ ┻━┻",
    "周二": "(╯￣Д￣)╯╘═╛",
    "周三": "╭(￣▽￣)╯╧═╧",
    "周四": "_(:з」∠)_",
    "周五": "(๑•̀ㅂ•́) ✧",
    "周六": "( ˘ 3˘)♥",
    "周日": "(;′༎ຶД༎ຶ`)"
}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946, 2, 14))  # 2
        self.calendar.setMaximumDate(QDate(6666, 6, 6))  # 3
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
        # self.calendar.setFirstDayOfWeek(Qt.Monday)                            # 4
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))                     # 5
        self.calendar.setGridVisible(True)  # 6
        self.calendar.clicked.connect(self.show_emotion_func)  # 6

        print(self.calendar.minimumDate())  # 7
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel(self)  # 8
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString("ddd")  # 9
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle("QCalendarWidget")

    def show_emotion_func(self):  # 10
        weekday = self.calendar.selectedDate().toString("ddd")
        self.label.setText(EMOTION[weekday])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 设置一个字典，并将各个星期及对应的颜文字分别作为键值输入；

2. 通过setMinimumDate()和setMaximumDate()可以设置日历的最小和最大日期(可用setDateRange()替代)，传入的参数为QDate。

3. setFirstDayOfWeek()方法可以设置一个星期的第一天，默认第一天为星期天，可传入的参数有：
    Qt.Monday
    Qt.Tuesday
    Qt.Wednesday
    Qt.Thursday
    Qt.Friday
    Qt.Saturday
    Qt.Sunday

4. setSelectedDate()方法可以设置日历初始化时所显示的日期，如果不设置，则默认是当天日期；

5. setGridVisible(bool)方法可以设置是否在日历上显示网格；

6. 当点击到日历上的某个日期时，clicked信号就会被触发。

7. minimumDate()、maximumDate()和selectedDate()分别获取日历的最早日期，最后日期和当前所选日期，类型为QDate；

8. 实例化一个QLabel控件用于显示颜文字；

9. 首先通过selectedDate()方法获取到当前所选日期，接着通过toString(‘ddd‘)方法获取星期的缩写，
    然后作为字典的键获取对应的值(注：笔者系统语言为英语，读者的系统语言为中文的话，则会获取到中文的星期名，那么此时应该将开头字典的键换成中文)；

10. 在槽函数中同理，获取到对应的值后，让QLabel控件进行显示。
"""
