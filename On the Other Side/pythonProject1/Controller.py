from PyQt5.QtWidgets import *
from GUI2 import *
from battles import *


# Currently unused because I haven't gotten it to work yet
class Controller(QMainWindow, Battle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_go.clicked.connect(lambda: self.save())

    def save(self):
        selection = 11
        if self.radioButton_attack.isChecked():
            selection = "0"
            self.close()

        elif self.radioButton_waltz.isChecked():
            selection = "1"
            self.close()

        elif self.radioButton_rhapsody.isChecked():
            selection = "2"
            self.close()

        elif self.radioButton_ballad.isChecked():
            selection = "3"
            self.close()
        return selection
