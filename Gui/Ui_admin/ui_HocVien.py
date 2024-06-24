# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HocViendRVRai.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_HocVien_Admin(object):
    def setupUi(self, HocVien):
        if not HocVien.objectName():
            HocVien.setObjectName(u"HocVien")
        HocVien.resize(1264, 715)
        HocVien.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#HocVien {\n"
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
"    border"
                        ": 1px solid #c4c4c4;\n"
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
"    border: 2px solid #0078d7;\n"
""
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
"    subcontrol-or"
                        "igin: margin;\n"
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
        self.frame_chucnang = QFrame(HocVien)
        self.frame_chucnang.setObjectName(u"frame_chucnang")
        self.frame_chucnang.setGeometry(QRect(250, 170, 981, 41))
        self.frame_chucnang.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_chucnang.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget_6 = QWidget(self.frame_chucnang)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(170, 0, 661, 32))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_them = QPushButton(self.layoutWidget_6)
        self.btn_them.setObjectName(u"btn_them")
        self.btn_them.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../../icon/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_them.setIcon(icon)
        self.btn_them.setIconSize(QSize(20, 16))
#if QT_CONFIG(shortcut)
        self.btn_them.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_6.addWidget(self.btn_them)

        self.btn_xoa = QPushButton(self.layoutWidget_6)
        self.btn_xoa.setObjectName(u"btn_xoa")
        icon1 = QIcon()
        icon1.addFile(u"../../icon/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoa.setIcon(icon1)
#if QT_CONFIG(shortcut)
        self.btn_xoa.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_6.addWidget(self.btn_xoa)

        self.btn_capnhat = QPushButton(self.layoutWidget_6)
        self.btn_capnhat.setObjectName(u"btn_capnhat")
        icon2 = QIcon()
        icon2.addFile(u"../../icon/update.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_capnhat.setIcon(icon2)
#if QT_CONFIG(shortcut)
        self.btn_capnhat.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_6.addWidget(self.btn_capnhat)

        self.btn_xoathongtin = QPushButton(self.layoutWidget_6)
        self.btn_xoathongtin.setObjectName(u"btn_xoathongtin")
        icon3 = QIcon()
        icon3.addFile(u"../../icon/clearall.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoathongtin.setIcon(icon3)
#if QT_CONFIG(shortcut)
        self.btn_xoathongtin.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_6.addWidget(self.btn_xoathongtin)

        self.btn_tim = QPushButton(self.layoutWidget_6)
        self.btn_tim.setObjectName(u"btn_tim")
        icon4 = QIcon()
        icon4.addFile(u"../../icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tim.setIcon(icon4)
#if QT_CONFIG(shortcut)
        self.btn_tim.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_6.addWidget(self.btn_tim)

        self.groupBox = QGroupBox(HocVien)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(250, 10, 981, 151))
        self.diachi = QLineEdit(self.groupBox)
        self.diachi.setObjectName(u"diachi")
        self.diachi.setGeometry(QRect(80, 110, 831, 31))
        self.mahocvien = QLineEdit(self.groupBox)
        self.mahocvien.setObjectName(u"mahocvien")
        self.mahocvien.setGeometry(QRect(80, 30, 131, 31))
        self.ten = QLineEdit(self.groupBox)
        self.ten.setObjectName(u"ten")
        self.ten.setGeometry(QRect(220, 30, 401, 31))
        self.Gioitinh = QComboBox(self.groupBox)
        self.Gioitinh.addItem("")
        self.Gioitinh.addItem("")
        self.Gioitinh.addItem("")
        self.Gioitinh.addItem("")
        self.Gioitinh.setObjectName(u"Gioitinh")
        self.Gioitinh.setGeometry(QRect(630, 30, 122, 31))
        self.socccd = QLineEdit(self.groupBox)
        self.socccd.setObjectName(u"socccd")
        self.socccd.setGeometry(QRect(250, 70, 241, 31))
        self.sodienthoai = QLineEdit(self.groupBox)
        self.sodienthoai.setObjectName(u"sodienthoai")
        self.sodienthoai.setGeometry(QRect(80, 70, 161, 31))
        self.email = QLineEdit(self.groupBox)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(500, 70, 411, 31))
        self.ngaysinh = QDateEdit(self.groupBox)
        self.ngaysinh.setObjectName(u"ngaysinh")
        self.ngaysinh.setGeometry(QRect(760, 30, 151, 31))
        self.groupBox_5 = QGroupBox(HocVien)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 190, 211, 351))
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
        self.btn_hocvien.setEnabled(False)
        self.btn_hocvien.setGeometry(QRect(10, 230, 191, 31))
        self.btn_hocvien.setFont(font)
        self.btn_lophoc = QPushButton(self.groupBox_5)
        self.btn_lophoc.setObjectName(u"btn_lophoc")
        self.btn_lophoc.setGeometry(QRect(10, 190, 191, 31))
        self.btn_lophoc.setFont(font)
        self.btn_giangvien = QPushButton(self.groupBox_5)
        self.btn_giangvien.setObjectName(u"btn_giangvien")
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
        self.groupBox_2 = QGroupBox(HocVien)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(10, 20, 211, 171))
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
        self.groupBox_6 = QGroupBox(HocVien)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(230, 200, 1021, 511))
        self.result_table = QTableWidget(self.groupBox_6)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEnabled(True)
        self.result_table.setGeometry(QRect(10, 30, 1001, 471))
        QWidget.setTabOrder(self.diachi, self.mahocvien)
        QWidget.setTabOrder(self.mahocvien, self.ten)
        QWidget.setTabOrder(self.ten, self.Gioitinh)
        QWidget.setTabOrder(self.Gioitinh, self.sodienthoai)
        QWidget.setTabOrder(self.sodienthoai, self.socccd)
        QWidget.setTabOrder(self.socccd, self.email)

        self.retranslateUi(HocVien)

        QMetaObject.connectSlotsByName(HocVien)
    # setupUi

    def retranslateUi(self, HocVien):
        HocVien.setWindowTitle(QCoreApplication.translate("HocVien", u"\u0110\u0103ng K\u00ed H\u1ecdc Vi\u00ean", None))
        self.btn_them.setText(QCoreApplication.translate("HocVien", u"Add", None))
        self.btn_xoa.setText(QCoreApplication.translate("HocVien", u"Delete", None))
        self.btn_capnhat.setText(QCoreApplication.translate("HocVien", u"update", None))
        self.btn_xoathongtin.setText(QCoreApplication.translate("HocVien", u"Clear", None))
        self.btn_tim.setText(QCoreApplication.translate("HocVien", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("HocVien", u"Nh\u1eadp Th\u00f4ng Tin H\u1ecdc Vi\u00ean", None))
        self.diachi.setPlaceholderText(QCoreApplication.translate("HocVien", u"\u0110\u1ecba Ch\u1ec9", None))
        self.mahocvien.setPlaceholderText(QCoreApplication.translate("HocVien", u"M\u00e3 h\u1ecdc vi\u00ean", None))
        self.ten.setPlaceholderText(QCoreApplication.translate("HocVien", u"H\u1ecd v\u00e0 T\u00ean", None))
        self.Gioitinh.setItemText(0, QCoreApplication.translate("HocVien", u"Gi\u1edbi T\u00ednh", None))
        self.Gioitinh.setItemText(1, QCoreApplication.translate("HocVien", u"Nam", None))
        self.Gioitinh.setItemText(2, QCoreApplication.translate("HocVien", u"N\u1eef", None))
        self.Gioitinh.setItemText(3, QCoreApplication.translate("HocVien", u"Kh\u00e1c", None))

        self.Gioitinh.setPlaceholderText(QCoreApplication.translate("HocVien", u"Gi\u1edbi T\u00ednh", None))
        self.socccd.setPlaceholderText(QCoreApplication.translate("HocVien", u"S\u1ed1 C\u0103n C\u01b0\u1edbc", None))
        self.sodienthoai.setPlaceholderText(QCoreApplication.translate("HocVien", u"S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i", None))
        self.email.setPlaceholderText(QCoreApplication.translate("HocVien", u"Email", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("HocVien", u"Ch\u1ee9c N\u0103ng", None))
        self.btn_doanhthu.setText(QCoreApplication.translate("HocVien", u"Doanh Thu", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("HocVien", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_tailieu.setText(QCoreApplication.translate("HocVien", u"T\u00e0i Li\u1ec7u", None))
        self.btn_hocvien.setText(QCoreApplication.translate("HocVien", u"H\u1ecdc Vi\u00ean", None))
        self.btn_lophoc.setText(QCoreApplication.translate("HocVien", u"L\u1edbp H\u1ecdc", None))
        self.btn_giangvien.setText(QCoreApplication.translate("HocVien", u"Gi\u1ea3ng Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("HocVien", u"Th\u00f4ng Tin Chung", None))
        self.btn_khoahoc.setText(QCoreApplication.translate("HocVien", u"Kh\u00f3a H\u1ecdc", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("HocVien", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("HocVien", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("HocVien", u"Role", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("HocVien", u"Name", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("HocVien", u"Th\u00f4ng Tin H\u1ecdc Vi\u00ean", None))
    # retranslateUi

