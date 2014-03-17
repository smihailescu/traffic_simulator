import sys

from PyQt4.QtCore import Qt, QTime, QTimer
from PyQt4.QtGui import QApplication, QLabel, QPixmap



class Countdown(QLabel):
    def __init__(self, countdown, parent=None):
        QLabel.__init__(self, parent)
        self.countdown = countdown
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter);
        self.setStyleSheet("QLabel {font-size : 200px; color : black; background-image: url('background.bmp');}")
        self.setText(str(self.countdown))
        # setup the countdown timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_time)

    def start(self):
        # update the display every second
        self.timer.start(1000)

    def _update_time(self):
        # this gets called every seconds
        # adjust the remaining time
        #self.countdown = self.countdown.addSecs(-1)
        self.countdown = self.countdown -1
        # if the remaining time reached zero, stop the timer
        if self.countdown <= 0:
            self.timer.stop()
        # update the display
        self.setText(str(self.countdown))
        #self.setPixmap(QPixmap('/tmp/test.png')); #<--- doesn't work


def main():
    app = QApplication(sys.argv)
    widget = Countdown(30)
    widget.start()
    widget.show()
    app.exec_()


if __name__ == '__main__':
    main()


