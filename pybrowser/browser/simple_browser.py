from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLineEdit

from PyQt5.QtWebEngineWidgets import QWebEngineView


HOME_URL = 'https://www.google.com/'


class SimpleBrowser:

    def __init__(self):
        self.__build_ui()
        self.__navigate_home()

    def __build_ui(self):
        # webview
        self.__web_view = QWebEngineView()

        # main window
        self.__window = QMainWindow()
        self.__window.showMaximized()
        self.__window.setCentralWidget(self.__web_view)

        # navbar
        navbar = QToolBar()

        # buttons
        back_btn = QAction('<', self.__window)  # back button
        forward_btn = QAction('>', self.__window)  # forward button
        refresh_btn = QAction('Refresh', self.__window)  # refresh button
        home_btn = QAction('Home', self.__window)  # forward button
        go_btn = QAction('Go', self.__window)  # go to link button
        stop_btn = QAction('X', self.__window)  # stop request button

        # url bar
        self.__url_bar = QLineEdit()

        # add elements to navbar
        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(refresh_btn)
        navbar.addAction(home_btn)
        navbar.addWidget(self.__url_bar)
        navbar.addAction(go_btn)
        navbar.addAction(stop_btn)

        # add navbar to main window
        self.__window.addToolBar(navbar)

        # add events
        # pressing buttons
        back_btn.triggered.connect(self.__web_view.back)
        forward_btn.triggered.connect(self.__web_view.forward)
        refresh_btn.triggered.connect(self.__web_view.reload)
        home_btn.triggered.connect(self.__navigate_home)
        go_btn.triggered.connect(self.__navigate_to_url)
        stop_btn.triggered.connect(self.__web_view.stop)
        # pressing enter in url bar
        self.__url_bar.returnPressed.connect(self.__navigate_to_url)
        # loading page if webview url changes
        self.__web_view.urlChanged.connect(self.__update_url)

    def __navigate_home(self):
        self.__web_view.setUrl(QUrl(HOME_URL))  # setting new webview url

    def __navigate_to_url(self):
        url = self.__url_bar.text()  # getting actual url from url bar
        self.__web_view.setUrl(QUrl(url))  # setting new webview url

    def __update_url(self, q):
        self.__url_bar.setText(q.toString())  # setting url
