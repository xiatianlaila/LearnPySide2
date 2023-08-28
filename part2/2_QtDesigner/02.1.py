# -*- coding: utf-8 -*-
"""
去官网查看 https://doc.qt.io/qt-6/qtdesigner-manual.html
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
