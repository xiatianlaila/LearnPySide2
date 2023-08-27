# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton("Click Me!", self)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        choice = QMessageBox.question(self, "Change Text?", "Would you like to change the button text?",  
                             QMessageBox.Yes | QMessageBox.No)  # 1

        if choice == QMessageBox.Yes:                           # 2
            self.button.setText("Changed!")
        elif choice == QMessageBox.No:                          # 4
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
