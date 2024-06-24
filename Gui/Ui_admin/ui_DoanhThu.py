# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DoanhThuvTpYaw.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_DoanhThu_Admin(object):
    def setupUi(self, DoanhThu):
        if not DoanhThu.objectName():
            DoanhThu.setObjectName(u"DoanhThu")
        DoanhThu.resize(1280, 720)
        DoanhThu.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#DoanhThu {\n"
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
"    borde"
                        "r: 1px solid #c4c4c4;\n"
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
"    subcontrol-origin: mar"
                        "gin;\n"
"    subcontrol-position: top left;\n"
"	top: 5px;\n"
"    padding: 0 3px;\n"
"    background-color: #FFD79A;\n"
"    border-radius: 5px;\n"
"    color: #000000;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"}")
        self.groupBox_6 = QGroupBox(DoanhThu)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(230, 10, 1031, 701))
        self.result_table = QTableWidget(self.groupBox_6)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEnabled(True)
        self.result_table.setGeometry(QRect(10, 30, 1011, 661))
        self.groupBox_5 = QGroupBox(DoanhThu)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 180, 211, 351))
        self.btn_doanhthu = QPushButton(self.groupBox_5)
        self.btn_doanhthu.setObjectName(u"btn_doanhthu")
        self.btn_doanhthu.setGeometry(QRect(10, 310, 191, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_doanhthu.setFont(font)
        self.btn_lichsudangki = QPushButton(self.groupBox_5)
        self.btn_lichsudangki.setObjectName(u"btn_lichsudangki")
        self.btn_lichsudangki.setGeometry(QRect(10, 270, 191, 31))
        self.btn_lichsudangki.setFont(font)
        self.btn_tailieu = QPushButton(self.groupBox_5)
        self.btn_tailieu.setObjectName(u"btn_tailieu")
        self.btn_tailieu.setEnabled(True)
        self.btn_tailieu.setGeometry(QRect(10, 110, 191, 31))
        self.btn_tailieu.setFont(font)
        self.btn_hocvien = QPushButton(self.groupBox_5)
        self.btn_hocvien.setObjectName(u"btn_hocvien")
        self.btn_hocvien.setGeometry(QRect(10, 230, 191, 31))
        self.btn_hocvien.setFont(font)
        self.btn_lophoc = QPushButton(self.groupBox_5)
        self.btn_lophoc.setObjectName(u"btn_lophoc")
        self.btn_lophoc.setGeometry(QRect(10, 190, 191, 31))
        self.btn_lophoc.setFont(font)
        self.btn_giangvien = QPushButton(self.groupBox_5)
        self.btn_giangvien.setObjectName(u"btn_giangvien")
        self.btn_giangvien.setEnabled(False)
        self.btn_giangvien.setGeometry(QRect(10, 150, 191, 31))
        self.btn_giangvien.setFont(font)
        self.btn_thongtinchung = QPushButton(self.groupBox_5)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(True)
        self.btn_thongtinchung.setGeometry(QRect(10, 30, 191, 31))
        self.btn_thongtinchung.setFont(font)
        self.btn_khoahoc = QPushButton(self.groupBox_5)
        self.btn_khoahoc.setObjectName(u"btn_khoahoc")
        self.btn_khoahoc.setEnabled(True)
        self.btn_khoahoc.setGeometry(QRect(10, 70, 191, 31))
        self.btn_khoahoc.setFont(font)
        self.groupBox_2 = QGroupBox(DoanhThu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(10, 10, 211, 171))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.groupBox_2.setFont(font1)
        self.btn_dangxuat = QPushButton(self.groupBox_2)
        self.btn_dangxuat.setObjectName(u"btn_dangxuat")
        self.btn_dangxuat.setGeometry(QRect(50, 130, 111, 31))
        self.btn_dangxuat.setFont(font)
        self.btn_dangxuat.setStyleSheet(u"")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 70, 191, 51))
        self.infor_role = QLineEdit(self.groupBox_3)
        self.infor_role.setObjectName(u"infor_role")
        self.infor_role.setEnabled(False)
        self.infor_role.setGeometry(QRect(0, 20, 191, 31))
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 20, 191, 51))
        self.groupBox_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_4.setAutoFillBackground(False)
        self.infor_username = QLineEdit(self.groupBox_4)
        self.infor_username.setObjectName(u"infor_username")
        self.infor_username.setEnabled(False)
        self.infor_username.setGeometry(QRect(0, 20, 191, 31))

        self.retranslateUi(DoanhThu)

        QMetaObject.connectSlotsByName(DoanhThu)
    # setupUi

    def retranslateUi(self, DoanhThu):
        DoanhThu.setWindowTitle(QCoreApplication.translate("DoanhThu", u"Form", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("DoanhThu", u"Th\u00f4ng Tin", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("DoanhThu", u"Ch\u1ee9c N\u0103ng", None))
        self.btn_doanhthu.setText(QCoreApplication.translate("DoanhThu", u"Doanh Thu", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("DoanhThu", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_tailieu.setText(QCoreApplication.translate("DoanhThu", u"T\u00e0i Li\u1ec7u", None))
        self.btn_hocvien.setText(QCoreApplication.translate("DoanhThu", u"H\u1ecdc Vi\u00ean", None))
        self.btn_lophoc.setText(QCoreApplication.translate("DoanhThu", u"L\u1edbp H\u1ecdc", None))
        self.btn_giangvien.setText(QCoreApplication.translate("DoanhThu", u"Gi\u1ea3ng Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("DoanhThu", u"Th\u00f4ng Tin Chung", None))
        self.btn_khoahoc.setText(QCoreApplication.translate("DoanhThu", u"Kh\u00f3a H\u1ecdc", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DoanhThu", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("DoanhThu", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DoanhThu", u"Role", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("DoanhThu", u"Name", None))
    # retranslateUi

