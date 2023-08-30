# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.is_saved = True                                            # 1

        self.textedit = QTextEdit(self)                                 # 2
        self.textedit.textChanged.connect(self.on_textchanged_func)

        self.button = QPushButton("Save", self)                         # 3
        self.button.clicked.connect(self.on_clicked_func)

        self.v_layout = QVBoxLayout()   
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):                      
        if self.textedit.toPlainText(): 
            self.is_saved = False
        else:
            self.is_saved = True

    def on_clicked_func(self):
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True

    def save_func(self, text):          
        with open("saved.txt", "w") as f:
            f.write(text)

    def closeEvent(self, QCloseEvent):                                  # 4
        if not self.is_saved:
            choice = QMessageBox.question(self, "", "Do you want to save the text?",
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toPlainText())
                QCloseEvent.accept()
            if choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
1. is_saved变量用于记录用户是否已经进行保存；

2. 实例化一个QTextEdit控件用于文本编辑，将其textChanged信号和自定义的槽函数连接起来：在槽函数中我们判断在每次文本内容发生变化时，
    textedit中是否还有文本，若有的话则将is_saved变量设为False，即未保存；
    若无文本，则将其设为True(如果没有文本的话，那可以直接关闭窗口，程序不会询问是否需要保存，因为没必要)。

3. 实例化一个按钮用于保存操作，将clicked信号与自定义的槽函数进行连接：每次点击该按钮就进行保存，不管文本编辑框中是否有文本，
    文本保存通过save_fcun()函数完成,我们将内容保存在当前目录下的saved.txt函数中。
    PyQt5提供一个QFileDialog类可以让我们更好的完成保存操作，后续章节会涉及，这里只是先简单的完成下保存功能。
    
4. 这里我们重新定义了QWidget的窗口关闭函数closeEvent()，如果用户还没有进行保存，则弹出一个QMessageBox窗口询问是否保存，
    若用户点击Yes，则调用save_func()函数进行保存，然后通过accept()方法来接收关闭窗口操作，窗口随之关闭；若点击No，则不进行保存，
    但同样得关闭窗口；若点击cancel，也不进行保存，并通过ignore()方法来忽略这次关闭窗口的操作。
    我们点击Yes后，则窗口关闭，在项目路径下出现一个‘saved.txt’文件，里面的文本正是我们之前所输入的文本
"""
