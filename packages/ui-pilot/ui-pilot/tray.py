import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication, QSystemTrayIcon, QMenu, QAction
)



basedir = os.path.dirname(__file__)


def start_session():
    print('start_session')

def open_dashboard():
    print('open_dashboard')


class TrayApp:
    def __init__(self):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)
        self.initUI()

    def initUI(self):
        # self.icon = QIcon("assets/icon.png")
        self.icon = QIcon(os.path.join(basedir, 'assets', 'icon.png'))
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        self.renderMenu()

    def renderMenu(self):
        self.menu = QMenu()

        self.action_start_session = QAction("Start Session")
        self.action_start_session.triggered.connect(start_session)
        self.menu.addAction(self.action_start_session)

        self.menu.addSeparator()

        self.action_open_dashboard = QAction("Dashboard")
        self.action_open_dashboard.triggered.connect(open_dashboard)
        self.menu.addAction(self.action_open_dashboard)

        self.menu.addSeparator()

        self.action_quit = QAction("Quit")
        self.action_quit.triggered.connect(self.app.quit)
        self.menu.addAction(self.action_quit)

        self.tray.setContextMenu(self.menu)

    def run(self):
        self.app.exec_()


def main():
    app = TrayApp()
    app.run()

if __name__ == '__main__':
    main()
