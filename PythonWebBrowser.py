import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

# Main Window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Browser
        self.browser = QWebEngineView()

        # Search Engine URL for Browser
        self.browser.setUrl(QUrl('https://google.com'))

        # Google Search Engine
        self.setCentralWidget(self.browser)

        # Screen Maximize
        self.showMaximized()

        # Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Go Back Button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Go Forward Button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Reload Button
        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # HomePage Button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.home)
        navbar.addAction(home_button)

        # Search Bar
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)

        # Update Url
        self.browser.urlChanged.connect(self.updateUrl)

    # back to HomePage
    def home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    # load URL 
    def loadUrl(self):
        url = self.searchBar.text()     # fetching URL
        self.browser.setUrl(QUrl(url))  # loading URL

    # update URL
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())      # Updating SearchBar

MyApp = QApplication(sys.argv)

QApplication.setApplicationName('Python Web Browser')

window = Window()

MyApp.exec_()
