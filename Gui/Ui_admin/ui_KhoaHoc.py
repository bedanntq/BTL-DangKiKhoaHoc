# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KhoaHocapdVKQ.ui'
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

class Ui_KhoaHoc_Admin(object):
    def setupUi(self, KhoaHoc):
        if not KhoaHoc.objectName():
            KhoaHoc.setObjectName(u"KhoaHoc")
        KhoaHoc.resize(1244, 715)
        KhoaHoc.setStyleSheet(u"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"QWidget#KhoaHoc {\n"
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
"    border-radius: 3px;\n"
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
"    subcontrol-origin: marg"
                        "in;\n"
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
        self.frame_fucntion = QFrame(KhoaHoc)
        self.frame_fucntion.setObjectName(u"frame_fucntion")
        self.frame_fucntion.setGeometry(QRect(230, 120, 1001, 51))
        self.frame_fucntion.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fucntion.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_fucntion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 10, 911, 37))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_3.addWidget(self.btn_them)

        self.btn_xoa = QPushButton(self.layoutWidget)
        self.btn_xoa.setObjectName(u"btn_xoa")
        icon1 = QIcon()
        icon1.addFile(u"../../icon/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoa.setIcon(icon1)
#if QT_CONFIG(shortcut)
        self.btn_xoa.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_xoa)

        self.btn_capnhat = QPushButton(self.layoutWidget)
        self.btn_capnhat.setObjectName(u"btn_capnhat")
        icon2 = QIcon()
        icon2.addFile(u"../../icon/update.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_capnhat.setIcon(icon2)
#if QT_CONFIG(shortcut)
        self.btn_capnhat.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_capnhat)

        self.btn_xoathongtin = QPushButton(self.layoutWidget)
        self.btn_xoathongtin.setObjectName(u"btn_xoathongtin")
        icon3 = QIcon()
        icon3.addFile(u"../../icon/clearall.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_xoathongtin.setIcon(icon3)
#if QT_CONFIG(shortcut)
        self.btn_xoathongtin.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_xoathongtin)

        self.btn_tim = QPushButton(self.layoutWidget)
        self.btn_tim.setObjectName(u"btn_tim")
        icon4 = QIcon()
        icon4.addFile(u"../../icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tim.setIcon(icon4)
#if QT_CONFIG(shortcut)
        self.btn_tim.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_3.addWidget(self.btn_tim)

        self.groupBox = QGroupBox(KhoaHoc)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(230, 10, 1001, 111))
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 70, 981, 33))
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
        self.layoutWidget2.setGeometry(QRect(10, 30, 981, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.makhoahoc = QLineEdit(self.layoutWidget2)
        self.makhoahoc.setObjectName(u"makhoahoc")

        self.horizontalLayout.addWidget(self.makhoahoc)

        self.thoiluong = QLineEdit(self.layoutWidget2)
        self.thoiluong.setObjectName(u"thoiluong")

        self.horizontalLayout.addWidget(self.thoiluong)

        self.groupBox_5 = QGroupBox(KhoaHoc)
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
        self.btn_giangvien.setGeometry(QRect(10, 150, 191, 31))
        self.btn_giangvien.setFont(font)
        self.btn_thongtinchung = QPushButton(self.groupBox_5)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(True)
        self.btn_thongtinchung.setGeometry(QRect(10, 30, 191, 31))
        self.btn_thongtinchung.setFont(font)
        self.btn_khoahoc = QPushButton(self.groupBox_5)
        self.btn_khoahoc.setObjectName(u"btn_khoahoc")
        self.btn_khoahoc.setEnabled(False)
        self.btn_khoahoc.setGeometry(QRect(10, 70, 191, 31))
        self.btn_khoahoc.setFont(font)
        self.groupBox_2 = QGroupBox(KhoaHoc)
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
        self.groupBox_6 = QGroupBox(KhoaHoc)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(230, 170, 1001, 531))
        self.result_table = QTableWidget(self.groupBox_6)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEnabled(True)
        self.result_table.setGeometry(QRect(10, 30, 981, 491))

        self.retranslateUi(KhoaHoc)

        QMetaObject.connectSlotsByName(KhoaHoc)
    # setupUi

    def retranslateUi(self, KhoaHoc):
        KhoaHoc.setWindowTitle(QCoreApplication.translate("KhoaHoc", u"Qu\u1ea3n L\u00fdKh\u00f3a H\u1ecdc", None))
        self.btn_them.setText(QCoreApplication.translate("KhoaHoc", u"Add", None))
        self.btn_xoa.setText(QCoreApplication.translate("KhoaHoc", u"Delete", None))
        self.btn_capnhat.setText(QCoreApplication.translate("KhoaHoc", u"update", None))
        self.btn_xoathongtin.setText(QCoreApplication.translate("KhoaHoc", u"Clear", None))
        self.btn_tim.setText(QCoreApplication.translate("KhoaHoc", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("KhoaHoc", u"Nh\u1eadp Th\u00f4ng Tin Kh\u00f3a H\u1ecdc", None))
        self.tenkhoahoc.setPlaceholderText(QCoreApplication.translate("KhoaHoc", u"T\u00ean Kh\u00f3a H\u1ecdc", None))
        self.hocphi.setPlaceholderText(QCoreApplication.translate("KhoaHoc", u"H\u1ecdc Ph\u00ed", None))
        self.makhoahoc.setPlaceholderText(QCoreApplication.translate("KhoaHoc", u"M\u00e3 Kh\u00f3a h\u1ecdc", None))
        self.thoiluong.setPlaceholderText(QCoreApplication.translate("KhoaHoc", u"Th\u1eddi L\u01b0\u1ee3ng", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("KhoaHoc", u"Ch\u1ee9c N\u0103ng", None))
        self.btn_doanhthu.setText(QCoreApplication.translate("KhoaHoc", u"Doanh Thu", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("KhoaHoc", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_tailieu.setText(QCoreApplication.translate("KhoaHoc", u"T\u00e0i Li\u1ec7u", None))
        self.btn_hocvien.setText(QCoreApplication.translate("KhoaHoc", u"H\u1ecdc Vi\u00ean", None))
        self.btn_lophoc.setText(QCoreApplication.translate("KhoaHoc", u"L\u1edbp H\u1ecdc", None))
        self.btn_giangvien.setText(QCoreApplication.translate("KhoaHoc", u"Gi\u1ea3ng Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("KhoaHoc", u"Th\u00f4ng Tin Chung", None))
        self.btn_khoahoc.setText(QCoreApplication.translate("KhoaHoc", u"Kh\u00f3a H\u1ecdc", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("KhoaHoc", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("KhoaHoc", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("KhoaHoc", u"Role", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("KhoaHoc", u"Name", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("KhoaHoc", u"Th\u00f4ng Tin Kh\u00f3a H\u1ecdc", None))
    # retranslateUi

