# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DangKiKhoaHocZGxRvo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Dangkikhoahoc_User(object):
    def setupUi(self, Dangkikhoahoc):
        if not Dangkikhoahoc.objectName():
            Dangkikhoahoc.setObjectName(u"Dangkikhoahoc")
        Dangkikhoahoc.resize(1244, 715)
        Dangkikhoahoc.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#Dangkikhoahoc {\n"
"    background-color: #DDFFBC\n"
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
"    "
                        "border: 1px solid #c4c4c4;\n"
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
"/* QDateEdit Styles */\n"
"QDateEdit {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"}\n"
"QDateEdit:focus {\n"
"    border: 2px solid #0078d7"
                        ";\n"
"}\n"
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
"/* TimeEdit Styles */\n"
"QTimeEdit {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FEFFDE;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 2px"
                        " solid #0078d7;\n"
"}\n"
"\n"
"QTimeEdit::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 15px;\n"
"    border-left: 1px solid #FFD79A;\n"
"    border-top-right-radius: 5px;\n"
"    background: #FFD79A;\n"
"}\n"
"\n"
"QTimeEdit::up-button:hover {\n"
"    background: #0078d7;\n"
"    border-left: 1px solid #0078d7;\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed {\n"
"    background: #004494;\n"
"    border-left: 1px solid #004494;\n"
"}\n"
"\n"
"QTimeEdit::up-arrow {\n"
"    image: url(\"E:/BTL python/Dangkikhoahoc/Gui/Ui_admin/icon/chevron-up-outline.png\");\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QTimeEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    height: 15px;\n"
"    border-left: 1px solid #FFD79A;\n"
"    border-bottom-right-radius: 5px;\n"
"    background: #FFD79A;\n"
"}\n"
"\n"
"QTimeEdit::down-button:hover {\n"
"    background: #0078d7"
                        ";\n"
"    border-left: 1px solid #0078d7;\n"
"}\n"
"\n"
"QTimeEdit::down-button:pressed {\n"
"    background: #004494;\n"
"    border-left: 1px solid #004494;\n"
"}\n"
"\n"
"QTimeEdit::down-arrow {\n"
"    image: url(down_arrow.png); /* Thay \u0111\u1ed5i icon m\u0169i t\u00ean n\u1ebfu c\u1ea7n */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
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
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 15px;\n"
"    border-left: 1px solid #FFD79A;\n"
"    border-top-right-radius: 5px;\n"
"    background: #FFD79A;\n"
"}\n"
"\n"
"QDateEdit::up-button:hover {\n"
"    background: #0078d7;\n"
"    border-left: 1px solid #0078d7;\n"
"}\n"
"\n"
"QDateEdit::up-button:pressed "
                        "{\n"
"    background: #004494;\n"
"    border-left: 1px solid #004494;\n"
"}\n"
"\n"
"QDateEdit::up-arrow {\n"
"    image: url(\"E:/BTL python/Dangkikhoahoc/Gui/Ui_admin/icon/chevron-up-outline.png\");\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    height: 15px;\n"
"    border-left: 1px solid #FFD79A;\n"
"    border-bottom-right-radius: 5px;\n"
"    background: #FFD79A;\n"
"}\n"
"\n"
"QDateEdit::down-button:hover {\n"
"    background: #0078d7;\n"
"    border-left: 1px solid #0078d7;\n"
"}\n"
"\n"
"QDateEdit::down-button:pressed {\n"
"    background: #004494;\n"
"    border-left: 1px solid #004494;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(down_arrow.png); /* Thay \u0111\u1ed5i icon m\u0169i t\u00ean n\u1ebfu c\u1ea7n */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"/* GroupBox Styles */\n"
"QGroupBox {\n"
"    border: 2px solid #FFD79A;\n"
"    bo"
                        "rder-radius: 10px;\n"
"    margin-top: 20px;\n"
"    background-color: #FEFFDE;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"	top: 5px;\n"
"    padding: 0 3px;\n"
"    background-color: #FFD79A;\n"
"    border-radius: 5px;\n"
"    color: #000000;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.frame_fucntion = QFrame(Dangkikhoahoc)
        self.frame_fucntion.setObjectName(u"frame_fucntion")
        self.frame_fucntion.setGeometry(QRect(250, 170, 981, 31))
        self.frame_fucntion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fucntion.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_fucntion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 0, 455, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_them = QPushButton(self.layoutWidget)
        self.btn_them.setObjectName(u"btn_them")
        self.btn_them.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../../icon/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_them.setIcon(icon)
        self.btn_them.setIconSize(QSize(20, 16))
#if QT_CONFIG(shortcut)
        self.btn_them.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout.addWidget(self.btn_them)

        self.btn_xoathongtin = QPushButton(self.layoutWidget)
        self.btn_xoathongtin.setObjectName(u"btn_xoathongtin")
        icon1 = QIcon()
        icon1.addFile(u"../../icon/clearall.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoathongtin.setIcon(icon1)
#if QT_CONFIG(shortcut)
        self.btn_xoathongtin.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout.addWidget(self.btn_xoathongtin)

        self.btn_tim = QPushButton(self.layoutWidget)
        self.btn_tim.setObjectName(u"btn_tim")
        icon2 = QIcon()
        icon2.addFile(u"../../icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tim.setIcon(icon2)
#if QT_CONFIG(shortcut)
        self.btn_tim.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout.addWidget(self.btn_tim)

        self.btn_lichsudangki_2 = QPushButton(self.layoutWidget)
        self.btn_lichsudangki_2.setObjectName(u"btn_lichsudangki_2")
        self.btn_lichsudangki_2.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_lichsudangki_2.setFont(font)

        self.horizontalLayout.addWidget(self.btn_lichsudangki_2)

        self.groupBox = QGroupBox(Dangkikhoahoc)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(250, 10, 981, 151))
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 941, 33))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.malophoc = QComboBox(self.layoutWidget1)
        self.malophoc.setObjectName(u"malophoc")

        self.horizontalLayout_9.addWidget(self.malophoc)

        self.tenlophoc = QComboBox(self.layoutWidget1)
        self.tenlophoc.setObjectName(u"tenlophoc")

        self.horizontalLayout_9.addWidget(self.tenlophoc)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 30, 941, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mahocvien = QComboBox(self.layoutWidget2)
        self.mahocvien.setObjectName(u"mahocvien")

        self.horizontalLayout_2.addWidget(self.mahocvien)

        self.tenhocvien = QComboBox(self.layoutWidget2)
        self.tenhocvien.setObjectName(u"tenhocvien")

        self.horizontalLayout_2.addWidget(self.tenhocvien)

        self.makhoahoc = QComboBox(self.layoutWidget2)
        self.makhoahoc.setObjectName(u"makhoahoc")

        self.horizontalLayout_2.addWidget(self.makhoahoc)

        self.tenkhoahoc = QComboBox(self.layoutWidget2)
        self.tenkhoahoc.setObjectName(u"tenkhoahoc")

        self.horizontalLayout_2.addWidget(self.tenkhoahoc)

        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(270, 110, 441, 33))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.thoigian = QTimeEdit(self.layoutWidget3)
        self.thoigian.setObjectName(u"thoigian")
        self.thoigian.setCurrentSection(QDateTimeEdit.Section.HourSection)

        self.horizontalLayout_3.addWidget(self.thoigian)

        self.ngaybatdau = QDateEdit(self.layoutWidget3)
        self.ngaybatdau.setObjectName(u"ngaybatdau")
        self.ngaybatdau.setCurrentSection(QDateTimeEdit.Section.YearSection)

        self.horizontalLayout_3.addWidget(self.ngaybatdau)

        self.groupBox_2 = QGroupBox(Dangkikhoahoc)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(250, 200, 981, 501))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.groupBox_2.setFont(font1)
        self.result_table = QTableWidget(self.groupBox_2)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEnabled(True)
        self.result_table.setGeometry(QRect(10, 30, 961, 461))
        self.groupBox_5 = QGroupBox(Dangkikhoahoc)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 190, 231, 281))
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 20, 211, 141))
        self.btn_tracuuhocvien = QPushButton(self.groupBox_4)
        self.btn_tracuuhocvien.setObjectName(u"btn_tracuuhocvien")
        self.btn_tracuuhocvien.setGeometry(QRect(0, 80, 211, 31))
        self.btn_tracuuhocvien.setFont(font)
        self.btn_thongtinchung = QPushButton(self.groupBox_4)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(True)
        self.btn_thongtinchung.setGeometry(QRect(0, 20, 211, 31))
        self.btn_thongtinchung.setFont(font)
        self.btn_tracuukhoahoc = QPushButton(self.groupBox_4)
        self.btn_tracuukhoahoc.setObjectName(u"btn_tracuukhoahoc")
        self.btn_tracuukhoahoc.setEnabled(False)
        self.btn_tracuukhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_tracuukhoahoc.setFont(font)
        self.btn_tracuulophoc = QPushButton(self.groupBox_4)
        self.btn_tracuulophoc.setObjectName(u"btn_tracuulophoc")
        self.btn_tracuulophoc.setGeometry(QRect(0, 110, 211, 31))
        self.btn_tracuulophoc.setFont(font)
        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 160, 211, 111))
        self.btn_dangkikhoahoc = QPushButton(self.groupBox_8)
        self.btn_dangkikhoahoc.setObjectName(u"btn_dangkikhoahoc")
        self.btn_dangkikhoahoc.setEnabled(True)
        self.btn_dangkikhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_dangkikhoahoc.setFont(font)
        self.btn_lichsudangki = QPushButton(self.groupBox_8)
        self.btn_lichsudangki.setObjectName(u"btn_lichsudangki")
        self.btn_lichsudangki.setEnabled(True)
        self.btn_lichsudangki.setGeometry(QRect(0, 80, 211, 31))
        self.btn_lichsudangki.setFont(font)
        self.btn_dangkihocvien = QPushButton(self.groupBox_8)
        self.btn_dangkihocvien.setObjectName(u"btn_dangkihocvien")
        self.btn_dangkihocvien.setEnabled(True)
        self.btn_dangkihocvien.setGeometry(QRect(0, 20, 211, 31))
        self.btn_dangkihocvien.setFont(font)
        self.groupBox_3 = QGroupBox(Dangkikhoahoc)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QRect(10, 10, 231, 171))
        self.groupBox_3.setFont(font1)
        self.btn_dangxuat = QPushButton(self.groupBox_3)
        self.btn_dangxuat.setObjectName(u"btn_dangxuat")
        self.btn_dangxuat.setGeometry(QRect(50, 130, 111, 31))
        self.btn_dangxuat.setFont(font)
        self.btn_dangxuat.setStyleSheet(u"")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 70, 201, 51))
        self.infor_role = QLineEdit(self.groupBox_6)
        self.infor_role.setObjectName(u"infor_role")
        self.infor_role.setEnabled(False)
        self.infor_role.setGeometry(QRect(0, 20, 201, 31))
        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 20, 201, 51))
        self.groupBox_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_7.setAutoFillBackground(False)
        self.infor_username = QLineEdit(self.groupBox_7)
        self.infor_username.setObjectName(u"infor_username")
        self.infor_username.setEnabled(False)
        self.infor_username.setGeometry(QRect(0, 20, 201, 31))

        self.retranslateUi(Dangkikhoahoc)

        QMetaObject.connectSlotsByName(Dangkikhoahoc)
    # setupUi

    def retranslateUi(self, Dangkikhoahoc):
        Dangkikhoahoc.setWindowTitle(QCoreApplication.translate("Dangkikhoahoc", u"\u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.btn_them.setText(QCoreApplication.translate("Dangkikhoahoc", u"\u0110\u0103ng K\u00ed", None))
        self.btn_xoathongtin.setText(QCoreApplication.translate("Dangkikhoahoc", u"Clear", None))
        self.btn_tim.setText(QCoreApplication.translate("Dangkikhoahoc", u"T\u00ecm Ki\u1ebfm", None))
        self.btn_lichsudangki_2.setText(QCoreApplication.translate("Dangkikhoahoc", u"Xu\u1ea5t Th\u00f4ng Tin H\u00f3a \u0110\u01a1n", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Nh\u1eadp Th\u00f4ng Tin \u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.malophoc.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"M\u00e3 L\u1edbp H\u1ecdc", None))
        self.tenlophoc.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"T\u00ean L\u1edbp H\u1ecdc", None))
        self.mahocvien.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"M\u00e3 H\u1ecdc Vi\u00ean", None))
        self.tenhocvien.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"T\u00ean H\u1ecdc Vi\u00ean", None))
        self.makhoahoc.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"M\u00e3 Kh\u00f3a H\u1ecdc", None))
        self.tenkhoahoc.setPlaceholderText(QCoreApplication.translate("Dangkikhoahoc", u"T\u00ean Kh\u00f3a H\u1ecdc", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Th\u00f4ng Tin Kh\u00f3a H\u1ecdc", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Giao Di\u1ec7n C\u00e1c Ch\u1ee9c N\u0103ng", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Tra C\u1ee9u", None))
        self.btn_tracuuhocvien.setText(QCoreApplication.translate("Dangkikhoahoc", u"Tra C\u1ee9u H\u1ecdc Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("Dangkikhoahoc", u"Th\u00f4ng Tin Chung", None))
        self.btn_tracuukhoahoc.setText(QCoreApplication.translate("Dangkikhoahoc", u"Tra C\u1ee9u Kh\u00f3a H\u1ecdc", None))
        self.btn_tracuulophoc.setText(QCoreApplication.translate("Dangkikhoahoc", u"Tra C\u1ee9u L\u1edbp H\u1ecdc", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Ch\u1ee9c N\u0103ng \u0110\u0103ng K\u00ed", None))
        self.btn_dangkikhoahoc.setText(QCoreApplication.translate("Dangkikhoahoc", u"\u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("Dangkikhoahoc", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_dangkihocvien.setText(QCoreApplication.translate("Dangkikhoahoc", u"\u0110\u0103ng K\u00ed H\u1ecdc Vi\u00ean", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("Dangkikhoahoc", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Role", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dangkikhoahoc", u"Name", None))
    # retranslateUi

