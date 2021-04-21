import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    """
    This is the root class of the whole project.
    The class inherits the attributes and functions form the QMainWindow class which is part of the module PyQt5.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the MainWindow class.
        :param args:
        :param kwargs:
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Verwaltungsprogramm")


def main():
    """
    This is the main function of this Python module
    :return: None
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
