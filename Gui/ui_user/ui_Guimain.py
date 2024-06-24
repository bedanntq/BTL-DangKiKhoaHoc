# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuimaingLRffI.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Guimain_User(object):
    def setupUi(self, Guimain):
        if not Guimain.objectName():
            Guimain.setObjectName(u"Guimain")
        Guimain.resize(1244, 719)
        Guimain.setStyleSheet(u"/* Global Font */\n"
"*{\n"
"	font: 700 11pt \"Times New Roman\";\n"
"}\n"
"\n"
"/* Main Widget Background */\n"
"QWidget#Guimain {\n"
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
"    background-color: #FFFAC0;"
                        "\n"
"    color: #9DE6E8;\n"
"    padding: 5px;\n"
"    border: 1px solid #c4c4c4;\n"
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
""
                        "}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"}\n"
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
"    padding: 10"
                        "px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #FFD79A;\n"
"    border: 2px solid #FFD79A;\n"
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
"    font-size: 13pt; /* T\u0103ng c\u1ee1 ch\u1eef l\u00ea"
                        "n 16pt */\n"
"    color: #000000; /* M\u00e0u ch\u1eef \u0111en */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
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
        self.groupBox = QGroupBox(Guimain)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QRect(250, 10, 981, 691))
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QRect(0, 20, 981, 671))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.groupBox_5 = QGroupBox(Guimain)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 200, 231, 281))
        self.groupBox_3 = QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 20, 211, 141))
        self.btn_tracuuhocvien = QPushButton(self.groupBox_3)
        self.btn_tracuuhocvien.setObjectName(u"btn_tracuuhocvien")
        self.btn_tracuuhocvien.setGeometry(QRect(0, 80, 211, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.btn_tracuuhocvien.setFont(font1)
        self.btn_thongtinchung = QPushButton(self.groupBox_3)
        self.btn_thongtinchung.setObjectName(u"btn_thongtinchung")
        self.btn_thongtinchung.setEnabled(False)
        self.btn_thongtinchung.setGeometry(QRect(0, 20, 211, 31))
        self.btn_thongtinchung.setFont(font1)
        self.btn_tracuukhoahoc = QPushButton(self.groupBox_3)
        self.btn_tracuukhoahoc.setObjectName(u"btn_tracuukhoahoc")
        self.btn_tracuukhoahoc.setEnabled(True)
        self.btn_tracuukhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_tracuukhoahoc.setFont(font1)
        self.btn_tracuulophoc = QPushButton(self.groupBox_3)
        self.btn_tracuulophoc.setObjectName(u"btn_tracuulophoc")
        self.btn_tracuulophoc.setGeometry(QRect(0, 110, 211, 31))
        self.btn_tracuulophoc.setFont(font1)
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 160, 211, 111))
        self.btn_dangkikhoahoc = QPushButton(self.groupBox_4)
        self.btn_dangkikhoahoc.setObjectName(u"btn_dangkikhoahoc")
        self.btn_dangkikhoahoc.setEnabled(True)
        self.btn_dangkikhoahoc.setGeometry(QRect(0, 50, 211, 31))
        self.btn_dangkikhoahoc.setFont(font1)
        self.btn_lichsudangki = QPushButton(self.groupBox_4)
        self.btn_lichsudangki.setObjectName(u"btn_lichsudangki")
        self.btn_lichsudangki.setEnabled(True)
        self.btn_lichsudangki.setGeometry(QRect(0, 80, 211, 31))
        self.btn_lichsudangki.setFont(font1)
        self.btn_dangkihocvien = QPushButton(self.groupBox_4)
        self.btn_dangkihocvien.setObjectName(u"btn_dangkihocvien")
        self.btn_dangkihocvien.setEnabled(True)
        self.btn_dangkihocvien.setGeometry(QRect(0, 20, 211, 31))
        self.btn_dangkihocvien.setFont(font1)
        self.groupBox_2 = QGroupBox(Guimain)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(10, 20, 231, 171))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.groupBox_2.setFont(font2)
        self.btn_dangxuat = QPushButton(self.groupBox_2)
        self.btn_dangxuat.setObjectName(u"btn_dangxuat")
        self.btn_dangxuat.setGeometry(QRect(50, 130, 111, 31))
        self.btn_dangxuat.setFont(font1)
        self.btn_dangxuat.setStyleSheet(u"")
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 70, 201, 51))
        self.infor_role = QLineEdit(self.groupBox_6)
        self.infor_role.setObjectName(u"infor_role")
        self.infor_role.setEnabled(False)
        self.infor_role.setGeometry(QRect(0, 20, 201, 31))
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 20, 201, 51))
        self.groupBox_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_7.setAutoFillBackground(False)
        self.infor_username = QLineEdit(self.groupBox_7)
        self.infor_username.setObjectName(u"infor_username")
        self.infor_username.setEnabled(False)
        self.infor_username.setGeometry(QRect(0, 20, 201, 31))

        self.retranslateUi(Guimain)

        QMetaObject.connectSlotsByName(Guimain)
    # setupUi

    def retranslateUi(self, Guimain):
        Guimain.setWindowTitle(QCoreApplication.translate("Guimain", u"Trang Ch\u1ee7 Nh\u00e2n Vi\u00ean", None))
        self.groupBox.setTitle(QCoreApplication.translate("Guimain", u"Gi\u1edbi Thi\u1ec7u V\u1ec1 \u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Guimain", u"\u0110\u0103ng k\u00fd kh\u00f3a h\u1ecdc l\u00e0 m\u1ed9t quy tr\u00ecnh quan tr\u1ecdng gi\u00fap h\u1ecdc vi\u00ean c\u00f3 th\u1ec3 ch\u00ednh th\u1ee9c tham gia v\u00e0o c\u00e1c ch\u01b0\u01a1ng tr\u00ecnh h\u1ecdc t\u1eadp t\u1ea1i c\u00e1c tr\u01b0\u1eddng h\u1ecdc, trung t\u00e2m \u0111\u00e0o t\u1ea1o, ho\u1eb7c c\u00e1c t\u1ed5 ch\u1ee9c gi\u00e1o d\u1ee5c kh\u00e1c. Qu\u00e1 tr\u00ecnh n\u00e0y kh\u00f4ng ch\u1ec9 gi\u00fap x\u00e1c nh\u1eadn danh s\u00e1ch h\u1ecdc vi\u00ean tham gia m\u00e0 c\u00f2n cung c\u1ea5p th\u00f4ng tin chi ti\u1ebft v\u1ec1 kh\u00f3a h\u1ecdc, th\u1eddi gian, \u0111\u1ecba \u0111i\u1ec3m, v\u00e0 c\u00e1c y\u00eau c\u1ea7u c\u1ea7n thi\u1ebft. D\u01b0\u1edbi \u0111\u00e2y l\u00e0 m\u1ed9t b\u00e0i gi\u1edbi thi\u1ec7u chi ti\u1ebft v\u1ec1 quy tr\u00ecnh v\u00e0 \u00fd ngh\u0129a c\u1ee7a vi\u1ec7c \u0111\u0103ng k\u00fd kh\u00f3a h\u1ecdc.\n"
"Quy Tr\u00ecnh \u0110\u0103ng K\u00fd Kh\u00f3a H\u1ecdc\n"
"1.T\u00ecm hi\u1ec3u th\u00f4ng tin v\u1ec1 kh\u00f3a h\u1ecdc:\n"
""
                        "   Tr\u01b0\u1edbc khi \u0111\u0103ng k\u00fd, h\u1ecdc vi\u00ean c\u1ea7n t\u00ecm hi\u1ec3u k\u1ef9 v\u1ec1 c\u00e1c kh\u00f3a h\u1ecdc m\u00e0 m\u00ecnh quan t\u00e2m. Th\u00f4ng tin n\u00e0y th\u01b0\u1eddng \u0111\u01b0\u1ee3c cung c\u1ea5p tr\u00ean website c\u1ee7a tr\u01b0\u1eddng ho\u1eb7c trung t\u00e2m \u0111\u00e0o t\u1ea1o, bao g\u1ed3m m\u1ee5c ti\u00eau kh\u00f3a h\u1ecdc, ch\u01b0\u01a1ng tr\u00ecnh h\u1ecdc, gi\u1ea3ng vi\u00ean, h\u1ecdc ph\u00ed, v\u00e0 th\u1eddi gian h\u1ecdc.\n"
"2. Chu\u1ea9n b\u1ecb h\u1ed3 s\u01a1 \u0111\u0103ng k\u00fd:\n"
"   H\u1ed3 s\u01a1 \u0111\u0103ng k\u00fd th\u01b0\u1eddng bao g\u1ed3m c\u00e1c gi\u1ea5y t\u1edd c\u00e1 nh\u00e2n nh\u01b0 ch\u1ee9ng minh nh\u00e2n d\u00e2n, gi\u1ea5y khai sinh, b\u1eb1ng c\u1ea5p, v\u00e0 c\u00e1c gi\u1ea5y t\u1edd kh\u00e1c theo y\u00eau c\u1ea7u c\u1ee7a t\u1eebng kh\u00f3a h\u1ecdc c\u1ee5 th\u1ec3. M\u1ed9t s\u1ed1 kh\u00f3a h\u1ecdc c\u00f3 th\u1ec3 y\u00eau c\u1ea7u th\u00eam th\u01b0 gi\u1edbi thi\u1ec7u ho\u1eb7c b\u00e0"
                        "i lu\u1eadn c\u00e1 nh\u00e2n.\n"
"3. N\u1ed9p \u0111\u01a1n \u0111\u0103ng k\u00fd:\n"
"   H\u1ecdc vi\u00ean c\u1ea7n \u0111i\u1ec1n \u0111\u1ea7y \u0111\u1ee7 th\u00f4ng tin v\u00e0o \u0111\u01a1n \u0111\u0103ng k\u00fd v\u00e0 n\u1ed9p k\u00e8m theo c\u00e1c gi\u1ea5y t\u1edd \u0111\u00e3 chu\u1ea9n b\u1ecb. \u0110\u01a1n \u0111\u0103ng k\u00fd c\u00f3 th\u1ec3 n\u1ed9p tr\u1ef1c ti\u1ebfp t\u1ea1i v\u0103n ph\u00f2ng tuy\u1ec3n sinh ho\u1eb7c g\u1eedi qua \u0111\u01b0\u1eddng b\u01b0u \u0111i\u1ec7n, email, ho\u1eb7c th\u00f4ng qua h\u1ec7 th\u1ed1ng \u0111\u0103ng k\u00fd tr\u1ef1c tuy\u1ebfn.\n"
"4. X\u00e1c nh\u1eadn v\u00e0 \u0111\u00f3ng h\u1ecdc ph\u00ed:\n"
"   Sau khi \u0111\u01a1n \u0111\u0103ng k\u00fd \u0111\u01b0\u1ee3c ch\u1ea5p nh\u1eadn, h\u1ecdc vi\u00ean s\u1ebd nh\u1eadn \u0111\u01b0\u1ee3c th\u00f4ng b\u00e1o x\u00e1c nh\u1eadn c\u00f9ng v\u1edbi h\u01b0\u1edbng d\u1eabn v\u1ec1 vi\u1ec7c \u0111\u00f3ng h\u1ecdc ph\u00ed. H\u1ecdc ph\u00ed c\u00f3 th\u1ec3 \u0111\u01b0\u1ee3c thanh to\u00e1"
                        "n b\u1eb1ng ti\u1ec1n m\u1eb7t, chuy\u1ec3n kho\u1ea3n ng\u00e2n h\u00e0ng, ho\u1eb7c qua c\u00e1c c\u1ed5ng thanh to\u00e1n tr\u1ef1c tuy\u1ebfn.\n"
"5. Tham gia bu\u1ed5i \u0111\u1ecbnh h\u01b0\u1edbng:\n"
"   M\u1ed9t s\u1ed1 kh\u00f3a h\u1ecdc c\u00f3 t\u1ed5 ch\u1ee9c bu\u1ed5i \u0111\u1ecbnh h\u01b0\u1edbng \u0111\u1ec3 gi\u1edbi thi\u1ec7u v\u1ec1 ch\u01b0\u01a1ng tr\u00ecnh h\u1ecdc, quy \u0111\u1ecbnh c\u1ee7a nh\u00e0 tr\u01b0\u1eddng, v\u00e0 c\u00e1c d\u1ecbch v\u1ee5 h\u1ed7 tr\u1ee3 h\u1ecdc vi\u00ean. Tham gia bu\u1ed5i \u0111\u1ecbnh h\u01b0\u1edbng gi\u00fap h\u1ecdc vi\u00ean l\u00e0m quen v\u1edbi m\u00f4i tr\u01b0\u1eddng h\u1ecdc t\u1eadp v\u00e0 chu\u1ea9n b\u1ecb t\u1ed1t h\u01a1n cho qu\u00e1 tr\u00ecnh h\u1ecdc.\n"
"\u00dd Ngh\u0129a C\u1ee7a Vi\u1ec7c \u0110\u0103ng K\u00fd Kh\u00f3a H\u1ecdc\n"
"- X\u00e1c nh\u1eadn quy\u1ec1n l\u1ee3i v\u00e0 ngh\u0129a v\u1ee5: Vi\u1ec7c \u0111\u0103ng k\u00fd kh\u00f3a h\u1ecdc ch\u00ednh th\u1ee9c x\u00e1c nh\u1eadn quy\u1ec1n l\u1ee3i c\u1ee7a h"
                        "\u1ecdc vi\u00ean trong vi\u1ec7c ti\u1ebfp c\u1eadn c\u00e1c t\u00e0i nguy\u00ean h\u1ecdc t\u1eadp v\u00e0 d\u1ecbch v\u1ee5 h\u1ed7 tr\u1ee3. \u0110\u1ed3ng th\u1eddi, h\u1ecdc vi\u00ean c\u0169ng hi\u1ec3u r\u00f5 c\u00e1c ngh\u0129a v\u1ee5 v\u00e0 quy \u0111\u1ecbnh c\u1ea7n tu\u00e2n th\u1ee7 trong su\u1ed1t qu\u00e1 tr\u00ecnh h\u1ecdc.\n"
"- L\u1eadp k\u1ebf ho\u1ea1ch h\u1ecdc t\u1eadp: \u0110\u0103ng k\u00fd kh\u00f3a h\u1ecdc gi\u00fap h\u1ecdc vi\u00ean l\u1eadp k\u1ebf ho\u1ea1ch h\u1ecdc t\u1eadp r\u00f5 r\u00e0ng v\u00e0 c\u00f3 t\u1ed5 ch\u1ee9c. Vi\u1ec7c bi\u1ebft tr\u01b0\u1edbc th\u1eddi gian v\u00e0 n\u1ed9i dung kh\u00f3a h\u1ecdc gi\u00fap h\u1ecdc vi\u00ean c\u00f3 s\u1ef1 chu\u1ea9n b\u1ecb t\u1ed1t h\u01a1n, t\u1eeb \u0111\u00f3 \u0111\u1ea1t hi\u1ec7u qu\u1ea3 h\u1ecdc t\u1eadp cao h\u01a1n.\n"
"- Giao l\u01b0u v\u00e0 m\u1edf r\u1ed9ng m\u1ea1ng l\u01b0\u1edbi: Tham gia v\u00e0o m\u1ed9t kh\u00f3a h\u1ecdc m\u1edbi mang l\u1ea1i c\u01a1 h\u1ed9i giao l\u01b0u, k\u1ebft n\u1ed1i v\u1edb"
                        "i gi\u1ea3ng vi\u00ean v\u00e0 c\u00e1c b\u1ea1n h\u1ecdc kh\u00e1c. \u0110\u00e2y l\u00e0 c\u01a1 h\u1ed9i tuy\u1ec7t v\u1eddi \u0111\u1ec3 m\u1edf r\u1ed9ng m\u1ea1ng l\u01b0\u1edbi quan h\u1ec7 c\u00e1 nh\u00e2n v\u00e0 ngh\u1ec1 nghi\u1ec7p.\n"
"- Ph\u00e1t tri\u1ec3n k\u1ef9 n\u0103ng v\u00e0 ki\u1ebfn th\u1ee9c: M\u1ee5c ti\u00eau ch\u00ednh c\u1ee7a vi\u1ec7c \u0111\u0103ng k\u00fd kh\u00f3a h\u1ecdc l\u00e0 n\u00e2ng cao ki\u1ebfn th\u1ee9c v\u00e0 k\u1ef9 n\u0103ng trong m\u1ed9t l\u0129nh v\u1ef1c c\u1ee5 th\u1ec3. \u0110i\u1ec1u n\u00e0y kh\u00f4ng ch\u1ec9 gi\u00fap h\u1ecdc vi\u00ean ph\u00e1t tri\u1ec3n b\u1ea3n th\u00e2n m\u00e0 c\u00f2n m\u1edf ra nhi\u1ec1u c\u01a1 h\u1ed9i ngh\u1ec1 nghi\u1ec7p trong t\u01b0\u01a1ng lai.\n"
"K\u1ebft Lu\u1eadn\n"
"\u0110\u0103ng k\u00fd kh\u00f3a h\u1ecdc l\u00e0 b\u01b0\u1edbc \u0111\u1ea7u ti\u00ean quan tr\u1ecdng tr\u00ean con \u0111\u01b0\u1eddng h\u1ecdc t\u1eadp v\u00e0 ph\u00e1t tri\u1ec3n c\u00e1 nh\u00e2n. Th\u1ef1c hi\u1ec7n \u0111\u00fang quy tr\u00ec"
                        "nh \u0111\u0103ng k\u00fd kh\u00f4ng ch\u1ec9 gi\u00fap h\u1ecdc vi\u00ean n\u1eafm v\u1eefng th\u00f4ng tin v\u1ec1 kh\u00f3a h\u1ecdc m\u00e0 c\u00f2n \u0111\u1ea3m b\u1ea3o quy\u1ec1n l\u1ee3i v\u00e0 ngh\u0129a v\u1ee5 trong su\u1ed1t qu\u00e1 tr\u00ecnh h\u1ecdc t\u1eadp. B\u1eb1ng c\u00e1ch ch\u1ecdn l\u1ef1a kh\u00f3a h\u1ecdc ph\u00f9 h\u1ee3p v\u00e0 tham gia nghi\u00eam t\u00fac, h\u1ecdc vi\u00ean s\u1ebd c\u00f3 c\u01a1 h\u1ed9i ph\u00e1t tri\u1ec3n to\u00e0n di\u1ec7n v\u00e0 \u0111\u1ea1t \u0111\u01b0\u1ee3c nh\u1eefng th\u00e0nh c\u00f4ng m\u1edbi trong s\u1ef1 nghi\u1ec7p v\u00e0 cu\u1ed9c s\u1ed1ng.", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Guimain", u"Giao Di\u1ec7n C\u00e1c Ch\u1ee9c N\u0103ng", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Guimain", u"Tra C\u1ee9u", None))
        self.btn_tracuuhocvien.setText(QCoreApplication.translate("Guimain", u"Tra C\u1ee9u H\u1ecdc Vi\u00ean", None))
        self.btn_thongtinchung.setText(QCoreApplication.translate("Guimain", u"Th\u00f4ng Tin Chung", None))
        self.btn_tracuukhoahoc.setText(QCoreApplication.translate("Guimain", u"Tra C\u1ee9u Kh\u00f3a H\u1ecdc", None))
        self.btn_tracuulophoc.setText(QCoreApplication.translate("Guimain", u"Tra C\u1ee9u L\u1edbp H\u1ecdc", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Guimain", u"Ch\u1ee9c N\u0103ng \u0110\u0103ng K\u00ed", None))
        self.btn_dangkikhoahoc.setText(QCoreApplication.translate("Guimain", u"\u0110\u0103ng K\u00ed Kh\u00f3a H\u1ecdc", None))
        self.btn_lichsudangki.setText(QCoreApplication.translate("Guimain", u"L\u1ecbch S\u1eed \u0110\u0103ng K\u00ed", None))
        self.btn_dangkihocvien.setText(QCoreApplication.translate("Guimain", u"\u0110\u0103ng K\u00ed H\u1ecdc Vi\u00ean", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Guimain", u"Th\u00f4ng Tin C\u00e1 Nh\u00e2n", None))
        self.btn_dangxuat.setText(QCoreApplication.translate("Guimain", u"\u0110\u0103ng Xu\u1ea5t", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Guimain", u"Role", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Guimain", u"Name", None))
    # retranslateUi

