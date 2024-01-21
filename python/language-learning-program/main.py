'''Run program dari sini
Karya:  1. Rizky Maulana Hadi
        2. M. Alif Rahman
        3. Abid Yafi Abiyyu'''
import frontend
import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = frontend.Login()
    login_window.show()
    sys.exit(app.exec_())