from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 100, 30))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 50, 320, 200))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        self.buttons = {}
        for text, row, col in buttons:
            button = QtWidgets.QPushButton(text)
            button.setObjectName(f"pushButton_{text}")
            self.gridLayout.addWidget(button, row, col, 1, 1)
            self.buttons[text] = button
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.add_functions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.label.setText(_translate("Form", "Calculator"))
        self.lineEdit.setText(_translate("Form", "0"))

    def add_functions(self):
        for text, button in self.buttons.items():
            if text not in {'=', 'C'}:
                button.clicked.connect(lambda _, t=text: self.on_button_click(t))
        self.buttons['='].clicked.connect(self.calculate_result)

    def on_button_click(self, char):
        current_text = self.lineEdit.text()
        if current_text == '0':
            self.lineEdit.setText(char)
        else:
            self.lineEdit.setText(current_text + char)

    def calculate_result(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except Exception as e:
            self.lineEdit.setText("Error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
