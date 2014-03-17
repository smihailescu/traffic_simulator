import sys

from PyQt4.QtCore import Qt, QTime, QTimer
from PyQt4.QtGui import QApplication, QLabel, QPixmap



class Principal(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter);
        self.setStyleSheet("QLabel {font-size : 200px; color : black; background-image: url('background.bmp');}")
        self.setText(str(self.countdown))
        
def main():
    app = QApplication(sys.argv)
    widget = Principal()
    widget.show()
    app.exec_()


if __name__ == '__main__':
    main()


