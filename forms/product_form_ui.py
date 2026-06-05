# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QWidget)

class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow):
        if not ProductWindow.objectName():
            ProductWindow.setObjectName(u"ProductWindow")
        ProductWindow.resize(906, 669)
        ProductWindow.setMinimumSize(QSize(900, 600))
        ProductWindow.setStyleSheet(u"background-color: white; color: black;")
        self.centralwidget = QWidget(ProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white;")
        self.user_label = QLabel(self.centralwidget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(460, 25, 320, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.user_label.setFont(font)
        self.logout_button = QPushButton(self.centralwidget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(800, 15, 80, 35))
        self.orders_button = QPushButton(self.centralwidget)
        self.orders_button.setObjectName(u"orders_button")
        self.orders_button.setGeometry(QRect(10, 50, 100, 35))
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(160, 50, 130, 35))
        self.search_label = QLabel(self.centralwidget)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(10, 100, 50, 25))
        self.search_edit = QLineEdit(self.centralwidget)
        self.search_edit.setObjectName(u"search_edit")
        self.search_edit.setGeometry(QRect(65, 100, 200, 25))
        self.sort_label = QLabel(self.centralwidget)
        self.sort_label.setObjectName(u"sort_label")
        self.sort_label.setGeometry(QRect(270, 100, 90, 25))
        self.sort_combo = QComboBox(self.centralwidget)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        self.sort_combo.setGeometry(QRect(375, 100, 150, 25))
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setGeometry(QRect(10, 140, 880, 520))
        self.scroll_area.setWidgetResizable(True)
        self.products_container = QWidget()
        self.products_container.setObjectName(u"products_container")
        self.products_container.setGeometry(QRect(0, 0, 878, 518))
        self.scroll_area.setWidget(self.products_container)
        self.filter_label = QLabel(self.centralwidget)
        self.filter_label.setObjectName(u"filter_label")
        self.filter_label.setGeometry(QRect(550, 100, 90, 25))
        font1 = QFont()
        font1.setPointSize(9)
        self.filter_label.setFont(font1)
        self.filter_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.supplier_combo = QComboBox(self.centralwidget)
        self.supplier_combo.setObjectName(u"supplier_combo")
        self.supplier_combo.setGeometry(QRect(630, 100, 150, 25))
        ProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductWindow)

        QMetaObject.connectSlotsByName(ProductWindow)
    # setupUi

    def retranslateUi(self, ProductWindow):
        ProductWindow.setWindowTitle(QCoreApplication.translate("ProductWindow", u"\u041e\u041e\u041e \"\u041e\u0431\u0443\u0432\u044c\" - \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430\u043c\u0438", None))
        self.user_label.setText(QCoreApplication.translate("ProductWindow", u"\u0424\u0418\u041e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.logout_button.setText(QCoreApplication.translate("ProductWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.orders_button.setText(QCoreApplication.translate("ProductWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.add_button.setText(QCoreApplication.translate("ProductWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.search_label.setText(QCoreApplication.translate("ProductWindow", u"\u041f\u043e\u0438\u0441\u043a:", None))
        self.search_edit.setPlaceholderText(QCoreApplication.translate("ProductWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442...", None))
        self.sort_label.setText(QCoreApplication.translate("ProductWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430:", None))
        self.sort_combo.setItemText(0, QCoreApplication.translate("ProductWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("ProductWindow", u"\u041f\u043e \u0446\u0435\u043d\u0435 (\u0432\u043e\u0437\u0440)", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("ProductWindow", u"\u041f\u043e \u0446\u0435\u043d\u0435 (\u0443\u0431\u044b\u0432)", None))
        self.sort_combo.setItemText(3, QCoreApplication.translate("ProductWindow", u"\u041f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443", None))
        self.sort_combo.setItemText(4, QCoreApplication.translate("ProductWindow", u"\u041f\u043e \u0441\u043a\u0438\u0434\u043a\u0435", None))

        self.filter_label.setText(QCoreApplication.translate("ProductWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
    # retranslateUi

