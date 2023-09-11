from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication, QSystemTrayIcon, QMenu, QAction
)



app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("assets/icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

def start_session():
    print('start_session')
action_start_session = QAction("Start Session")
action_start_session.triggered.connect(start_session)
menu.addAction(action_start_session)

menu.addSeparator()

def open_dashboard():
    print('open_dashboard')
action_open_dashboard = QAction("Dashboard")
action_open_dashboard.triggered.connect(open_dashboard)
menu.addAction(action_open_dashboard)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()
