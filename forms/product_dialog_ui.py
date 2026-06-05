# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 385)
        self.label_article = QLabel(Dialog)
        self.label_article.setObjectName(u"label_article")
        self.label_article.setGeometry(QRect(0, 10, 111, 16))
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(0, 40, 111, 16))
        self.label_category = QLabel(Dialog)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(0, 70, 111, 16))
        self.label_manufacturer = QLabel(Dialog)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        self.label_manufacturer.setGeometry(QRect(0, 100, 111, 16))
        self.label_supplier = QLabel(Dialog)
        self.label_supplier.setObjectName(u"label_supplier")
        self.label_supplier.setGeometry(QRect(0, 130, 111, 16))
        self.label_price = QLabel(Dialog)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setGeometry(QRect(0, 160, 111, 16))
        self.label_discount = QLabel(Dialog)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setGeometry(QRect(0, 190, 111, 16))
        self.label_quantity = QLabel(Dialog)
        self.label_quantity.setObjectName(u"label_quantity")
        self.label_quantity.setGeometry(QRect(0, 220, 111, 16))
        self.label_unit = QLabel(Dialog)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setGeometry(QRect(0, 250, 111, 16))
        self.label_description = QLabel(Dialog)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 280, 111, 16))
        self.label_image = QLabel(Dialog)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(0, 310, 111, 16))
        self.button_box = QDialogButtonBox(Dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setGeometry(QRect(60, 350, 156, 24))
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.edit_article = QLineEdit(Dialog)
        self.edit_article.setObjectName(u"edit_article")
        self.edit_article.setGeometry(QRect(120, 10, 113, 22))
        self.edit_name = QLineEdit(Dialog)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setGeometry(QRect(120, 40, 113, 22))
        self.edit_category = QLineEdit(Dialog)
        self.edit_category.setObjectName(u"edit_category")
        self.edit_category.setGeometry(QRect(120, 70, 113, 22))
        self.edit_manufacturer = QLineEdit(Dialog)
        self.edit_manufacturer.setObjectName(u"edit_manufacturer")
        self.edit_manufacturer.setGeometry(QRect(120, 100, 113, 22))
        self.edit_supplier = QLineEdit(Dialog)
        self.edit_supplier.setObjectName(u"edit_supplier")
        self.edit_supplier.setGeometry(QRect(120, 130, 113, 22))
        self.spin_price = QSpinBox(Dialog)
        self.spin_price.setObjectName(u"spin_price")
        self.spin_price.setGeometry(QRect(120, 160, 111, 22))
        self.spin_discount = QSpinBox(Dialog)
        self.spin_discount.setObjectName(u"spin_discount")
        self.spin_discount.setGeometry(QRect(120, 190, 111, 22))
        self.spin_quantity = QSpinBox(Dialog)
        self.spin_quantity.setObjectName(u"spin_quantity")
        self.spin_quantity.setGeometry(QRect(120, 220, 111, 22))
        self.edit_unit = QLineEdit(Dialog)
        self.edit_unit.setObjectName(u"edit_unit")
        self.edit_unit.setGeometry(QRect(120, 250, 161, 22))
        self.edit_description = QLineEdit(Dialog)
        self.edit_description.setObjectName(u"edit_description")
        self.edit_description.setGeometry(QRect(120, 280, 251, 22))
        self.edit_description.setDragEnabled(False)
        self.edit_image = QLineEdit(Dialog)
        self.edit_image.setObjectName(u"edit_image")
        self.edit_image.setGeometry(QRect(120, 310, 113, 22))
        self.edit_image.setDragEnabled(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_article.setText(QCoreApplication.translate("Dialog", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_category.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_manufacturer.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_supplier.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_price.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430 (\u0440\u0443\u0431.)", None))
        self.label_discount.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0438\u0434\u043a\u0430 (%)", None))
        self.label_quantity.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_unit.setText(QCoreApplication.translate("Dialog", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_description.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_image.setText(QCoreApplication.translate("Dialog", u"\u0424\u043e\u0442\u043e (\u0444\u0430\u0439\u043b)", None))
        self.edit_unit.setPlaceholderText(QCoreApplication.translate("Dialog", u"(\u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \"\u0448\u0442\".)", None))
    # retranslateUi

