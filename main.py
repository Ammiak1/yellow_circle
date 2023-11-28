import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.lineEdit.text():
            self.widget.clear()
            ## Получение диапазона построения
            data_x = [i for i in range(self.spinBox_a.value(), self.spinBox_b.value())]
            try:
                ## Получение функции и построение графика
                function = lambda x: eval(self.lineEdit.text())
                self.widget.plot(data_x, [function(i) for i in data_x], pen='r')
            except:
                pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
