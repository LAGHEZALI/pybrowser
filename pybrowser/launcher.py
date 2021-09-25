import sys

from PyQt5.QtWidgets import QApplication

from pybrowser.browser.simple_browser import SimpleBrowser


def launch_simple_browser():
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Simple Browser')
    _ = SimpleBrowser()
    return app.exec_()


if __name__ == "__main__":
    launch_simple_browser()
