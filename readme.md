# PyBrowser

PyBrowser is a lightweight web browser application built with Python and PyQt5. It features a tabbed interface, basic navigation controls, and a URL bar for convenient web browsing. This project demonstrates how to use PyQt5's WebEngine to create a simple, functional browser with essential features.

# Features
Tabbed Browsing: Open multiple tabs and close them individually.
Navigation Controls: Includes Back, Forward, Reload, and Home buttons for easy browsing.
URL Bar: Type URLs directly and navigate with ease. The URL bar updates automatically when the page changes.
Home Page: Quickly return to the home page (Google) with the Home button.
Automatic Tab Titles: Each tab displays the page title as the tab label, which updates as you navigate.

# Installation
To use PyBrowser, you need to have Python installed along with PyQt5 and PyQtWebEngine. You can install the required libraries with the following command:


- pip install PyQt5 PyQtWebEngine

Run the application:

- python pybrowser.py

- The browser opens with a single tab set to Google.
- Use the navigation toolbar to browse, open new tabs, or close them as needed.

# Customization
Home Page: Modify the default URL for the home page by changing the URL in self.navigate_home() and self.add_tab() methods.

Icon: Replace icon.webp with your own icon file to customize the browser window icon.

# License
This project is open-source and available under the MIT License.