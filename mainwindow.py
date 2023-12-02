# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStyledItemDelegate
from ui_form import Ui_MainWindow
# from PySide6.QtCore import Signal
# from PySide6.QtGui import QPixmap

from PySide6 import QtGui, QtCore

#user-defined-imports
from ui_transitions import transitions, routings


class MainWindow(QMainWindow):
    ui_transition_signals=QtCore.Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('WorkBuddy')

    ##load icons
        calculator_icon=QtGui.QPixmap("assets/icons/calculator_icon.png")
        self.ui.calculatorbtn.setIcon(calculator_icon)

        notes_icon=QtGui.QPixmap("assets/icons/note_icon.png")
        self.ui.notesbtn.setIcon(notes_icon)

        translate_icon=QtGui.QPixmap("assets/icons/translate_icon.png")
        self.ui.translatebtn.setIcon(translate_icon)

        # self.ui.comboBox.lineEdit().setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        

    ##app ui startup
        self.ui.mainStackW.setCurrentIndex(0) #main stack load index 0
        self.ui.functionStack.setCurrentIndex(0)
        self.ui.Introframe.setVisible(True)
        transitions.effect_fade(self,"in",self.ui.Introframe)
        self.ui_transition_signals.connect(lambda identifier:routings.route_from(self,identifier))
        self.animationEffect.finished.connect(lambda: self.ui_transition_signals.emit(0))

    ##main button routing
        self.ui.translatebtn.clicked.connect(lambda:routings.route_to(self,1))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
