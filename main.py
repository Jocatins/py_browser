import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set window properties
        self.setWindowTitle('PyBrowser')
        self.setWindowIcon(QIcon('icon.webp'))  # Optional icon

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Create toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add back button
        back_btn = QAction('⮜', self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        toolbar.addAction(back_btn)

        # Add forward button
        forward_btn = QAction('⮞', self)
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        toolbar.addAction(forward_btn)

        # Add reload button
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        toolbar.addAction(reload_btn)

        # Add home button
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)

        # Add new tab button
        add_tab_btn = QAction('+', self)
        add_tab_btn.triggered.connect(self.add_tab)
        toolbar.addAction(add_tab_btn)

        # Add URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        # Add first tab
        self.add_tab()

    def current_browser(self):
        # Return the currently active tab (browser)
        return self.tabs.currentWidget()

    def add_tab(self):
        # Create a new browser tab
        browser = QWebEngineView()
        browser.setUrl(QUrl('https://www.google.com'))
        self.tabs.addTab(browser, 'New Tab')
        self.tabs.setCurrentWidget(browser)
        self.tabs.setTabText(self.tabs.currentIndex(), 'Loading...')

        # Update tab title when the page loads
        browser.titleChanged.connect(
            lambda title, browser=browser: self.tabs.setTabText(self.tabs.indexOf(browser), title)
        )

        # Update URL bar when the page changes
        browser.urlChanged.connect(
            lambda url, browser=browser: self.update_url(url) if self.tabs.currentWidget() == browser else None
        )

    def close_tab(self, index):
        # Close the tab and stop any video if it's from YouTube
        browser_widget = self.tabs.widget(index)
        if browser_widget.url().host() == "www.youtube.com":
            browser_widget.page().runJavaScript("document.getElementsByTagName('video')[0].pause();")
        if self.tabs.count() < 2:
            self.close()
        else:
            self.tabs.removeTab(index)
            browser_widget.deleteLater()

    def navigate_home(self):
        # Navigate to the homepage
        self.current_browser().setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        # Navigate to the entered URL
        url = self.url_bar.text()
        if 'http' not in url:
            url = 'https://' + url
        self.current_browser().setUrl(QUrl(url))

    def update_url(self, q):
        # Update the URL bar with the current URL
        if self.sender() == self.current_browser():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('PyBrowser')
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
