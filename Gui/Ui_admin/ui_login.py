# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginTuDzTb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pymysql
from PySide6.QtGui import *


class Ui_DangNhap(object):
    def setupUi(self, Tailieu):
        if not Tailieu.objectName():
            Tailieu.setObjectName(u"Tailieu")
        Tailieu.resize(640, 480)
        Tailieu.setStyleSheet(u"\n"
"/* Main Widget Background */\n"
"QWidget#Tailieu {\n"
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
"    border: 1px solid #c4"
                        "c4c4;\n"
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
        self.groupBox = QGroupBox(Tailieu)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 621, 461))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.Taikhoan = QLineEdit(self.groupBox)
        self.Taikhoan.setObjectName(u"Taikhoan")
        self.Taikhoan.setGeometry(QRect(80, 170, 451, 31))
        self.btn_dn = QPushButton(self.groupBox)
        self.btn_dn.setObjectName(u"btn_dn")
        self.btn_dn.setGeometry(QRect(240, 290, 111, 31))
        self.matkhau = QLineEdit(self.groupBox)
        self.matkhau.setObjectName(u"matkhau")
        self.matkhau.setGeometry(QRect(80, 230, 451, 31))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 360, 181, 16))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.btn_dn_to_dk = QPushButton(self.groupBox)
        self.btn_dn_to_dk.setObjectName(u"btn_dn_to_dk")
        self.btn_dn_to_dk.setGeometry(QRect(320, 350, 111, 31))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 100, 201, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.retranslateUi(Tailieu)

        QMetaObject.connectSlotsByName(Tailieu)
    # setupUi

    def retranslateUi(self, Tailieu):
        Tailieu.setWindowTitle(QCoreApplication.translate("Tailieu", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Tailieu", u"\u0110\u0102NG NH\u1eacP", None))
        self.Taikhoan.setPlaceholderText(QCoreApplication.translate("Tailieu", u"T\u00e0i Kho\u1ea3n", None))
        self.btn_dn.setText(QCoreApplication.translate("Tailieu", u"\u0110\u0103ng Nh\u1eadp", None))
        self.matkhau.setPlaceholderText(QCoreApplication.translate("Tailieu", u"M\u1eadt Kh\u1ea9u", None))
        self.label.setText(QCoreApplication.translate("Tailieu", u"B\u1ea1n ch\u01b0a c\u00f3 T\u00e0i Kho\u1ea3n !?", None))
        self.btn_dn_to_dk.setText(QCoreApplication.translate("Tailieu", u"\u0110\u0102NG K\u00ed", None))
        self.label_2.setText(QCoreApplication.translate("Tailieu", u"\u0110\u0102NG NH\u1eacP", None))
    # retranslateUi





# Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        # Mở cửa sổ đăng nhập
        self.logout = LoginWindow()
        self.logout.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_main_admin_window(self):
        self.main_admin = GuiMainAdminWindow()
        self.main_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_khoahoc_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.khoahoc_admin = KhoaHocAdminWindow()
        self.khoahoc_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_tailieu_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.tailieu_admin = TailieuAdminWindow()
        self.tailieu_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_giangvien_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.giangvien_admin = GiangVienAdminWindow()
        self.giangvien_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_lophoc_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.lophoc_admin = LopHocAdminWindow()
        self.lophoc_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_hocvien_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.hocvien_admin = HocVienAdminWindow()
        self.hocvien_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_lichsudangki_admin_window(self):
        # Mở cửa sổ đăng nhập
        self.lichsudangki_admin = LichSuDangKiAdminWindow()
        self.lichsudangki_admin.show()
        #Ẩn cửa sổ
        self.hide()
    # Thực hiện hành động chuyển trang
    def open_doanhthu_admin_window(self):
        # Mở cửa sổ 
        self.doanhthu_admin = DoanhThuAdminWindow()
        self.doanhthu_admin.show()
        #Ẩn cửa sổ
        self.hide()