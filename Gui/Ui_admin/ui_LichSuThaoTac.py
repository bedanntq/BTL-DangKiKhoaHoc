# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HocPhinZZgRS.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_LichSuThaoTac_Admin(object):
    def setupUi(self, LichSuThaoTac):
        if not LichSuThaoTac.objectName():
            LichSuThaoTac.setObjectName(u"LichSuThaoTac")
        LichSuThaoTac.resize(1247, 720)
        LichSuThaoTac.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#LichSuThaoTac {\n"
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
        self.groupBox_2 = QGroupBox(LichSuThaoTac)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(10, 10, 231, 151))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.groupBox_2.setFont(font)
        self.btn_dangxuat = QPushButton(self.groupBox_2)
        self.btn_dangxuat.setObjectName(u"btn_dangxuat")
        self.btn_dangxuat.setGeometry(QRect(60, 110, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btn_dangxuat.setFont(font1)
        self.btn_dangxuat.setStyleSheet(u"")
        self.layoutWidget_4 = QWidget(self.groupBox_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 30, 211, 37))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.Tentaikhoan = QLineEdit(self.layoutWidget_4)
        self.Tentaikhoan.setObjectName(u"Tentaikhoan")
        self.Tentaikhoan.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.Tentaikhoan)

        self.layoutWidget_5 = QWidget(self.groupBox_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 70, 211, 37))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lop = QLineEdit(self.layoutWidget_5)
        self.lop.setObjectName(u"lop")
        self.lop.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.lop)

        self.frame_btn = QFrame(LichSuThaoTac)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setGeometry(QRect(20, 170, 211, 331))
        self.frame_btn.setStyleSheet(u"")
        self.frame_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_thongtinchung = QPushButton(self.frame_btn)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(False)
        self.btn_thongtinchung.setGeometry(QRect(10, 10, 191, 31))
        self.btn_thongtinchung.setFont(font1)
        self.btn_giangvien = QPushButton(self.frame_btn)
        self.btn_giangvien.setObjectName(u"btn_giangvien")
        self.btn_giangvien.setGeometry(QRect(10, 130, 191, 31))
        self.btn_giangvien.setFont(font1)
        self.btn_tailieu = QPushButton(self.frame_btn)
        self.btn_tailieu.setObjectName(u"btn_tailieu")
        self.btn_tailieu.setEnabled(True)
        self.btn_tailieu.setGeometry(QRect(10, 90, 191, 31))
        self.btn_tailieu.setFont(font1)
        self.btn_lichsudangki = QPushButton(self.frame_btn)
        self.btn_lichsudangki.setObjectName(u"btn_lichsudangki")
        self.btn_lichsudangki.setGeometry(QRect(10, 250, 191, 31))
        self.btn_lichsudangki.setFont(font1)
        self.btn_lophoc = QPushButton(self.frame_btn)
        self.btn_lophoc.setObjectName(u"btn_lophoc")
        self.btn_lophoc.setGeometry(QRect(10, 170, 191, 31))
        self.btn_lophoc.setFont(font1)
        self.btn_doanhthu = QPushButton(self.frame_btn)
        self.btn_doanhthu.setObjectName(u"btn_doanhthu")
        self.btn_doanhthu.setGeometry(QRect(10, 290, 191, 31))
        self.btn_doanhthu.setFont(font1)
        self.btn_hocvien = QPushButton(self.frame_btn)
        self.btn_hocvien.setObjectName(u"btn_hocvien")
        self.btn_hocvien.setGeometry(QRect(10, 210, 191, 31))
        self.btn_hocvien.setFont(font1)
        self.btn_khoahoc = QPushButton(self.frame_btn)
        self.btn_khoahoc.setObjectName(u"btn_khoahoc")
        self.btn_khoahoc.setEnabled(True)
        self.btn_khoahoc.setGeometry(QRect(10, 50, 191, 31))
        self.btn_khoahoc.setFont(font1)
        self.result_table = QTableWidget(LichSuThaoTac)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setGeometry(QRect(250, 10, 981, 691))

        self.retranslateUi(LichSuThaoTac)

        QMetaObject.connectSlotsByName(LichSuThaoTac)
    # setupUi

    def retranslateUi(self, LichSuThaoTac):
        LichSuThaoTac.setWindowTitle(QCoreApplication.translate("LichSuThaoTac", u"L\u1ecbch S\u1eed Thao T\u00e1c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("LichSuThaoTac", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("LichSuThaoTac", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.label_3.setText(QCoreApplication.translate("LichSuThaoTac", u"T\u00ean", None))
        self.label_4.setText(QCoreApplication.translate("LichSuThaoTac", u"M\u00e3", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("LichSuThaoTac", u"Th\u00f4ng Tin Chung", None))
        self.btn_giangvien.setText(QCoreApplication.translate("LichSuThaoTac", u"Gi\u1ea3ng Vi\u00ean", None))
        self.btn_tailieu.setText(QCoreApplication.translate("LichSuThaoTac", u"T\u00e0i Li\u1ec7u", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("LichSuThaoTac", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_lophoc.setText(QCoreApplication.translate("LichSuThaoTac", u"L\u1edbp H\u1ecdc", None))
        self.btn_doanhthu.setText(QCoreApplication.translate("LichSuThaoTac", u"Doanh Thu", None))
        self.btn_hocvien.setText(QCoreApplication.translate("LichSuThaoTac", u"H\u1ecdc Vi\u00ean", None))
        self.btn_khoahoc.setText(QCoreApplication.translate("LichSuThaoTac", u"Kh\u00f3a H\u1ecdc", None))
    # retranslateUi

