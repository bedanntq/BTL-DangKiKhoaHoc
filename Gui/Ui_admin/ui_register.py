# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerBrghBT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DangKi(object):
    def setupUi(self, DangKi):
        if not DangKi.objectName():
            DangKi.setObjectName(u"DangKi")
        DangKi.resize(640, 480)
        DangKi.setStyleSheet(u"\n"
"/* Main Widget Background */\n"
"QWidget#DangKi {\n"
"    background-color: #DDFFBC;\n"
"}\n"
"\n"
"/* LineEdit Styles */\n"
"QLineEdit {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"}\n"
"\n"
"/* PushButton Styles */\n"
"QPushButton {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px 15px;\n"
"    background-color: #FEFFDE;\n"
"    color: #000000;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FFD79A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004494;\n"
"}\n"
"\n"
"/* TableWidget Styles */\n"
"QTableWidget {\n"
"    border: 2px solid #c4c4c4;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #FFFAC0;\n"
"    color: #9DE6E8;\n"
"    padding: 5px;\n"
"    border: 1px solid #c4c"
                        "4c4;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #FFD79A;\n"
"    color: #FFFAC0;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #FFD79A;\n"
"}\n"
"\n"
"/* ScrollBar Styles */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 15px 0 15px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c4c4c4;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* QDateEdit Styles */\n"
"QDateEdit {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"}\n"
""
                        "\n"
"/* ComboBox Styles */\n"
"QComboBox {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #0078d7;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png); /* Thay \u0111\u1ed5i icon m\u0169i t\u00ean n\u1ebfu c\u1ea7n */\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"    selection-background-color: #FFD79A;\n"
"}\n"
"\n"
"/* TabWidget Styles */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    background-color: #FEFFDE;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #FFD79A;\n"
"    bor"
                        "der: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #9DE6E8;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: #FEFFDE;\n"
"    color: #9DE6E8;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #9DE6E8;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-left-color: none;\n"
"}\n"
"/* PlainTextEdit Styles */\n"
"QPlainTextEdit {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 13pt; /* T\u0103ng c\u1ee1 ch\u1eef l\u00ean 16pt */\n"
"    color: #000000; /* M\u00e0u ch\u1eef \u0111en */\n"
"}\n"
""
                        "\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"}")
        self.groupBox = QGroupBox(DangKi)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 621, 461))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.hovaten = QLineEdit(self.groupBox)
        self.hovaten.setObjectName(u"hovaten")
        self.hovaten.setGeometry(QRect(100, 110, 411, 31))
        self.Taikhoan = QLineEdit(self.groupBox)
        self.Taikhoan.setObjectName(u"Taikhoan")
        self.Taikhoan.setGeometry(QRect(100, 190, 411, 31))
        self.btn_dk_to_dn = QPushButton(self.groupBox)
        self.btn_dk_to_dn.setObjectName(u"btn_dk_to_dn")
        self.btn_dk_to_dn.setGeometry(QRect(340, 350, 121, 31))
        self.matkhau = QLineEdit(self.groupBox)
        self.matkhau.setObjectName(u"matkhau")
        self.matkhau.setGeometry(QRect(100, 230, 411, 31))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 360, 181, 16))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.nhaplaimatkhau = QLineEdit(self.groupBox)
        self.nhaplaimatkhau.setObjectName(u"nhaplaimatkhau")
        self.nhaplaimatkhau.setGeometry(QRect(100, 270, 411, 31))
        self.btn_dk = QPushButton(self.groupBox)
        self.btn_dk.setObjectName(u"btn_dk")
        self.btn_dk.setGeometry(QRect(250, 310, 111, 31))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 60, 161, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(28)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.email = QLineEdit(self.groupBox)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(100, 150, 411, 31))

        self.retranslateUi(DangKi)

        QMetaObject.connectSlotsByName(DangKi)
    # setupUi

    def retranslateUi(self, DangKi):
        DangKi.setWindowTitle(QCoreApplication.translate("DangKi", u"\u0110\u0103ng K\u00ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("DangKi", u"\u0110\u0102NG K\u00cd", None))
        self.hovaten.setPlaceholderText(QCoreApplication.translate("DangKi", u"H\u1ecd V\u00e0 T\u00ean", None))
        self.Taikhoan.setPlaceholderText(QCoreApplication.translate("DangKi", u"T\u00e0i Kho\u1ea3n", None))
        self.btn_dk_to_dn.setText(QCoreApplication.translate("DangKi", u"\u0110\u0103ng Nh\u1eadp", None))
        self.matkhau.setPlaceholderText(QCoreApplication.translate("DangKi", u"M\u1eadt Kh\u1ea9u", None))
        self.label.setText(QCoreApplication.translate("DangKi", u"B\u1ea1n \u0110\u00e3 c\u00f3 T\u00e0i Kho\u1ea3n !?", None))
        self.nhaplaimatkhau.setPlaceholderText(QCoreApplication.translate("DangKi", u"Nh\u1eadp L\u1ea1i M\u1eadt Kh\u1ea9u", None))
        self.btn_dk.setText(QCoreApplication.translate("DangKi", u"\u0110\u0102NG K\u00ed", None))
        self.label_2.setText(QCoreApplication.translate("DangKi", u"\u0110\u0102NG K\u00cd", None))
        self.email.setPlaceholderText(QCoreApplication.translate("DangKi", u"Email", None))
    # retranslateUi

