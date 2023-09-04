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
    print('click')
action = QAction("Start Session")
action.triggered.connect(start_session)
menu.addAction(action)

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()
