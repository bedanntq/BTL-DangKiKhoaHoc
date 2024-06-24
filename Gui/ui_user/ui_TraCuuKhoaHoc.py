# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KhoaHocFDBbJX.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_TraCuuKhoaHoc_User(object):
    def setupUi(self, TraCuuKhoaHoc):
        if not TraCuuKhoaHoc.objectName():
            TraCuuKhoaHoc.setObjectName(u"TraCuuKhoaHoc")
        TraCuuKhoaHoc.resize(1280, 720)
        TraCuuKhoaHoc.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#TraCuuKhoaHoc {\n"
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
"/* GroupBox Styles */\n"
"QGroupBox {\n"
"    border: 2px solid #FFD79A;\n"
"    border-radius: 10px;\n"
"    margin-top: 20px;\n"
"    background-color: #FEFFDE;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin"
                        ": margin;\n"
"    subcontrol-position: top left;\n"
"	top: 5px;\n"
"    padding: 0 3px;\n"
"    background-color: #FFD79A;\n"
"    border-radius: 5px;\n"
"    color: #000000;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"}")
        self.frame_fucntion = QFrame(TraCuuKhoaHoc)
        self.frame_fucntion.setObjectName(u"frame_fucntion")
        self.frame_fucntion.setGeometry(QRect(260, 120, 981, 41))
        self.frame_fucntion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fucntion.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_fucntion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 0, 701, 37))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_tim = QPushButton(self.layoutWidget)
        self.btn_tim.setObjectName(u"btn_tim")
        icon = QIcon()
        icon.addFile(u"../../icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tim.setIcon(icon)
#if QT_CONFIG(shortcut)
        self.btn_tim.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_tim)

        self.btn_xoathongtin = QPushButton(self.layoutWidget)
        self.btn_xoathongtin.setObjectName(u"btn_xoathongtin")
        icon1 = QIcon()
        icon1.addFile(u"../../icon/clearall.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoathongtin.setIcon(icon1)
#if QT_CONFIG(shortcut)
        self.btn_xoathongtin.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_xoathongtin)

        self.groupBox = QGroupBox(TraCuuKhoaHoc)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 10, 1011, 111))
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 971, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tenkhoahoc = QLineEdit(self.layoutWidget1)
        self.tenkhoahoc.setObjectName(u"tenkhoahoc")

        self.horizontalLayout_2.addWidget(self.tenkhoahoc)

        self.hocphi = QLineEdit(self.layoutWidget1)
        self.hocphi.setObjectName(u"hocphi")

        self.horizontalLayout_2.addWidget(self.hocphi)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 30, 971, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.makhoahoc = QLineEdit(self.layoutWidget2)
        self.makhoahoc.setObjectName(u"makhoahoc")

        self.horizontalLayout.addWidget(self.makhoahoc)

        self.thoiluong = QLineEdit(self.layoutWidget2)
        self.thoiluong.setObjectName(u"thoiluong")

        self.horizontalLayout.addWidget(self.thoiluong)

        self.groupBox_2 = QGroupBox(TraCuuKhoaHoc)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(250, 160, 1011, 541))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.groupBox_2.setFont(font)
        self.result_table = QTableWidget(self.groupBox_2)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEnabled(True)
        self.result_table.setGeometry(QRect(10, 30, 991, 501))
        self.groupBox_3 = QGroupBox(TraCuuKhoaHoc)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QRect(10, 10, 231, 171))
        self.groupBox_3.setFont(font)
        self.btn_dangxuat = QPushButton(self.groupBox_3)
        self.btn_dangxuat.setObjectName(u"btn_dangxuat")
        self.btn_dangxuat.setGeometry(QRect(50, 130, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btn_dangxuat.setFont(font1)
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
        self.groupBox_5 = QGroupBox(TraCuuKhoaHoc)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 190, 231, 281))
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 20, 211, 141))
        self.btn_tracuuhocvien = QPushButton(self.groupBox_4)
        self.btn_tracuuhocvien.setObjectName(u"btn_tracuuhocvien")
        self.btn_tracuuhocvien.setGeometry(QRect(0, 80, 211, 31))
        self.btn_tracuuhocvien.setFont(font1)
        self.btn_thongtinchung = QPushButton(self.groupBox_4)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(True)
        self.btn_thongtinchung.setGeometry(QRect(0, 20, 211, 31))
        self.btn_thongtinchung.setFont(font1)
        self.btn_tracuukhoahoc = QPushButton(self.groupBox_4)
        self.btn_tracuukhoahoc.setObjectName(u"btn_tracuukhoahoc")
        self.btn_tracuukhoahoc.setEnabled(False)
        self.btn_tracuukhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_tracuukhoahoc.setFont(font1)
        self.btn_tracuulophoc = QPushButton(self.groupBox_4)
        self.btn_tracuulophoc.setObjectName(u"btn_tracuulophoc")
        self.btn_tracuulophoc.setGeometry(QRect(0, 110, 211, 31))
        self.btn_tracuulophoc.setFont(font1)
        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 160, 211, 111))
        self.btn_dangkikhoahoc = QPushButton(self.groupBox_8)
        self.btn_dangkikhoahoc.setObjectName(u"btn_dangkikhoahoc")
        self.btn_dangkikhoahoc.setEnabled(True)
        self.btn_dangkikhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_dangkikhoahoc.setFont(font1)
        self.btn_lichsudangki = QPushButton(self.groupBox_8)
        self.btn_lichsudangki.setObjectName(u"btn_lichsudangki")
        self.btn_lichsudangki.setEnabled(True)
        self.btn_lichsudangki.setGeometry(QRect(0, 80, 211, 31))
        self.btn_lichsudangki.setFont(font1)
        self.btn_dangkihocvien = QPushButton(self.groupBox_8)
        self.btn_dangkihocvien.setObjectName(u"btn_dangkihocvien")
        self.btn_dangkihocvien.setEnabled(True)
        self.btn_dangkihocvien.setGeometry(QRect(0, 20, 211, 31))
        self.btn_dangkihocvien.setFont(font1)

        self.retranslateUi(TraCuuKhoaHoc)

        QMetaObject.connectSlotsByName(TraCuuKhoaHoc)
    # setupUi

    def retranslateUi(self, TraCuuKhoaHoc):
        TraCuuKhoaHoc.setWindowTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Tra C\u1ee9u Kh\u00f3a H\u1ecdc", None))
        self.btn_tim.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Search", None))
        self.btn_xoathongtin.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Clear", None))
        self.groupBox.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Nh\u1eadp Th\u00f4ng Tin Kh\u00f3a H\u1ecdc", None))
        self.tenkhoahoc.setPlaceholderText(QCoreApplication.translate("TraCuuKhoaHoc", u"T\u00ean Kh\u00f3a H\u1ecdc", None))
        self.hocphi.setPlaceholderText(QCoreApplication.translate("TraCuuKhoaHoc", u"H\u1ecdc Ph\u00ed", None))
        self.makhoahoc.setPlaceholderText(QCoreApplication.translate("TraCuuKhoaHoc", u"M\u00e3 Kh\u00f3a h\u1ecdc", None))
        self.thoiluong.setPlaceholderText(QCoreApplication.translate("TraCuuKhoaHoc", u"Th\u1eddi L\u01b0\u1ee3ng", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Th\u00f4ng Tin Kh\u00f3a H\u1ecdc", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Role", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Name", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Giao Di\u1ec7n C\u00e1c Ch\u1ee9c N\u0103ng", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Tra C\u1ee9u", None))
        self.btn_tracuuhocvien.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Tra C\u1ee9u H\u1ecdc Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Th\u00f4ng Tin Chung", None))
        self.btn_tracuukhoahoc.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Tra C\u1ee9u Kh\u00f3a H\u1ecdc", None))
        self.btn_tracuulophoc.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"Tra C\u1ee9u L\u1edbp H\u1ecdc", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("TraCuuKhoaHoc", u"Ch\u1ee9c N\u0103ng \u0110\u0103ng K\u00ed", None))
        self.btn_dangkikhoahoc.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"\u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_dangkihocvien.setText(QCoreApplication.translate("TraCuuKhoaHoc", u"\u0110\u0103ng K\u00ed H\u1ecdc Vi\u00ean", None))
    # retranslateUi

