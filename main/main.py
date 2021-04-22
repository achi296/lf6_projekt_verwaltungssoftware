import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from database_connection.load_from_mysql import LoadFromMySQL


class MainWindow(QMainWindow):
    """
    This is the root class of the whole project.
    The class inherits the attributes and functions from the QMainWindow class which is part of the module PyQt5.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the MainWindow class.
        :param args:
        :param kwargs:
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Verwaltungsprogramm")
        self.setFixedSize(350, 350)
        self.db = None
        self.initialise_database()

    def initialise_database(self):
        self.db = LoadFromMySQL()
        self.db.load_settings_from_json("../settings/settings.json")
        self.db.establish_connection()
        self.db.close_connection()


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
