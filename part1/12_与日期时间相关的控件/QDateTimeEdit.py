# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import QDate, QTime, QDateTime
from PySide2.QtWidgets import QApplication, QWidget, QDateTimeEdit, QDateEdit, QTimeEdit, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()    
        self.datetime_1 = QDateTimeEdit(self)                                           # 1
        self.datetime_1.dateChanged.connect(lambda: print("Date Changed!"))

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)              # 2
        self.datetime_2.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.datetime_2.timeChanged.connect(lambda: print("Time Changed!"))
        print(self.datetime_2.date())
        print(self.datetime_2.time())
        print(self.datetime_2.dateTime())

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)              # 3
        self.datetime_3.dateTimeChanged.connect(lambda: print("DateTime Changed!"))
        self.datetime_3.setCalendarPopup(True)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)                      # 4
        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)

        self.date = QDateEdit(QDate.currentDate(), self)                                # 5
        self.date.setDisplayFormat("yyyy/MM/dd")
        print(self.date.date())

        self.time = QTimeEdit(QTime.currentTime(), self)                                # 6
        self.time.setDisplayFormat("HH:mm:ss")
        print(self.time.time())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)
        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. 实例化一个QDateTimeEdit控件，并将其dateChanged信号与print('Date Changed!')打印函数连接起来，
    也就是说每当用户改变该控件上的日期(不是时间)时，就会触发dateChanged信号，而控制台就会打印'Date Changed!'；

2. 实例化一个QDateTimeEdit控件并将日期时间设置为当前的日期和时间，如果没有设置(像1中的QdateTimeEdit一样)，
    那么就会显示默认日期时间2000/1/1 12:00 AM。通过setDisplayFormat()方法可以设置日期时间的显示格式。
    这里还将timeChanged信号和打印函数进行了连接，也就是说每当用户改变时间(不是日期)时，就会触发timeChanged信号，
    而控制台就会打印'Time Changed!'，通过调用date()、time()和dateTime()可以分别获取到日期、时间以及合并的日期时间；

3. 该QDateTimeEdit控件的dateTimeChanged信号和打印函数连接了起来，也就是说用户不管是改了日期还是时间，都会触发该信号，
    从而打印'DateTime Changed!'，setCalendarPopup(True)方法可以设置日历弹窗；

4. self.datetime_4只传入了日期参数，没有时间；而self.datetime_5只传入了时间参数，没有日期；

5-6. 分别实例化了一个QDateEdit和QTimeEdit控件，用法和QDateTimeEdit控件极为类似。

QCalendarWidget为日历控件，用户可以设置日期范围，可以设置日历初始化时显示的日期(如果没有设置的话，默认为当天日期)；

QDateTimeEdit、QDateEdit以及QTimeEdit这三个控件用法差不多，掌握QDateTimeEdit的话其他两种其实也就明白怎么使用了；

通过setCalendarPopup(True)方法可以让QDateTimeEdit和QDateEdit显示日历。
"""