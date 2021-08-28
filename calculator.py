import sys
from PyQt5.QtWidgets import QDialog, QApplication
from calculatorEdit import *

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.formula = ""
        
        self.ui.zero.clicked.connect(self.zero)
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.seven)
        self.ui.eight.clicked.connect(self.eight)
        self.ui.nine.clicked.connect(self.nine)
        
        self.ui.clear.clicked.connect(self.clear)
        self.ui.plus_minus.clicked.connect(self.negative)
        self.ui.percentage.clicked.connect(self.percentage)
        self.ui.divide.clicked.connect(self.divide)
        self.ui.multiply.clicked.connect(self.multiply)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.plus.clicked.connect(self.add)
        self.ui.period.clicked.connect(self.period)
        self.ui.equals.clicked.connect(self.calculate)

        self.show()

    def zero(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "0")
        self.formula += "0"

    def one(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "1")
        self.formula += "1"
    
    def two(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "2")
        self.formula += "2"

    def three(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "3")
        self.formula += "3"

    def four(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "4")
        self.formula += "4"

    def five(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "5")
        self.formula += "5"

    def six(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "6")
        self.formula += "6"

    def seven(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "7")
        self.formula += "7"

    def eight(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "8")
        self.formula += "8"

    def nine(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + "9")
        self.formula += "9"

    def clear(self):
        self.ui.screen.setText("")
        self.formula = ""

    def percentage(self):
        text = self.ui.screen.text()
        percentage = int(text) / 100
        self.ui.screen.setText(str(percentage))
        self.formula += str(percentage)

    def divide(self):
        self.ui.screen.setText("")
        self.formula += " / "

    def multiply(self):
        self.ui.screen.setText("")
        self.formula += " * "

    def minus(self):
        self.ui.screen.setText("")
        self.formula += " - "

    def add(self):
        self.ui.screen.setText("")
        self.formula += " + "

    def period(self):
        text = self.ui.screen.text()
        self.ui.screen.setText(text + ".")
        self.formula += "."

    def negative(self):
        text = "-{}".format(self.ui.screen.text())
        self.ui.screen.setText(text)
        self.formula += text

    def calculate(self):
        result = eval(self.formula)
        self.ui.screen.setText(str(result))
        self.formula = result

    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())