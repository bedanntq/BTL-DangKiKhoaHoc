import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pymysql
from datetime import datetime
from Gui.Ui_admin.ui_login import Ui_DangNhap
from Gui.Ui_admin.ui_register import Ui_DangKi
from Gui.Ui_admin.ui_Guimain import Ui_GuiMain_Admin
from Gui.Ui_admin.ui_KhoaHoc import Ui_KhoaHoc_Admin
from Gui.Ui_admin.ui_TaiLieu import Ui_Tailieu_Admin
from Gui.Ui_admin.ui_GiangVien import Ui_GiangVien_Admin
from Gui.Ui_admin.ui_LopHoc import Ui_LopHoc_Admin
from Gui.Ui_admin.ui_HocVien import Ui_HocVien_Admin    
from Gui.Ui_admin.ui_LichSuThaoTac import Ui_LichSuThaoTac_Admin
from Gui.Ui_admin.ui_DoanhThu import Ui_DoanhThu_Admin
from Gui.ui_user.ui_Guimain import Ui_Guimain_User
from Gui.ui_user.ui_TraCuuKhoaHoc import Ui_TraCuuKhoaHoc_User  
from Gui.ui_user.ui_TraCuuHocVien import Ui_TraCuuHocVien_User
from Gui.ui_user.ui_TraCuuLopHoc import Ui_TraCuuLopHoc_User
from Gui.ui_user.ui_DangKiHocVien import Ui_DangKiHocVien_User
from Gui.ui_user.ui_DangKiKhoaHoc import Ui_Dangkikhoahoc_User
from Gui.ui_user.ui_LichSuDangKi import Ui_LichSuDangKi_User
#Giao diện đăng nhập
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangNhap()
        self.ui.setupUi(self)
        self.ui.btn_dn.clicked.connect(self.check_login)
        self.ui.btn_dn_to_dk.clicked.connect(self.open_register_window)
    # Thực hiện hành động chuyển trang  
    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()
    # Thực hiện hành động chuyển trang  
    def open_Guimain_admin_window(self):
        self.Guimain_window = GuiMainAdminWindow()
        self.Guimain_window.show()
        self.hide()
    # Thực hiện hành động chuyển trang  
    def open_Guimain_user_window(self):
        self.Guimain_window = GuiMainUserWindow()
        self.Guimain_window.show()
        self.hide()
#Giao diện đăng kí
class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangKi() 
        self.ui.setupUi(self)
        self.ui.btn_dk.clicked.connect(self.register)
        self.ui.btn_dk_to_dn.clicked.connect(self.open_login_window)
    # Thực hiện hành động chuyển trang  
    def open_login_window(self):
        # Mở cửa sổ đăng nhập
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()
#Phần giao diện bên admin
#Giao diện thông tin chung
class GuiMainAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GuiMain_Admin()
        self.ui.setupUi(self)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
        
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
#Giao diện thông tin của Khóa Học
class KhoaHocAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_KhoaHoc_Admin()
        self.ui.setupUi(self)
        #Liên kết các nút đến chức năng của nó
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window) 
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
#Giao diện thông tin của Quản Lý Tài Liệu
class TailieuAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tailieu_Admin()
        self.ui.setupUi(self)
        # Thiết lập tiêu đề cột cho QTableWidget
        self.ui.result_table.setColumnCount(4)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Tài Liệu", "Tên Tài Liệu", "Loại Tài Liệu", "Tác Giả"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Chọn cả dòng
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.result_table.verticalHeader().setVisible(False)
        # Tăng chiều cao của dòng
        self.ui.result_table.verticalHeader().setDefaultSectionSize(20)
        # Connect the table selection change to a function
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
        
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
#Giao diện thông tin của Quản Lý Giảng Viên
class GiangVienAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GiangVien_Admin()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(7)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Giảng Viên", "Tên Giảng Viên", "Giới Tính", "Ngày Sinh", "Email", "Số Điện Thoại", "Địa Chỉ"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Connect the table selection change to a function
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
    
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
#Giao diện thông tin của Quản Lý Lớp Học
class LopHocAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LopHoc_Admin()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(5)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Lớp", "Tên Lớp", "Mã Giảng Viên", "Mã Khóa Học", "Số Lượng Học Viên"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Gọi hàm để tải dữ liệu
        self.load_data()
        self.load_data_to_magiangvien()
        self.load_data_to_makhoahoc()
        # Connect the table selection change to a function
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
    
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
#Giao diện thông tin của Quản Lý Học Viên
class HocVienAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HocVien_Admin()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(8)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Học Viên", "Tên Học Viên", "Giới Tính", "Ngày Sinh", "Email","CCCD", "Số Điện Thoại", "Địa Chỉ"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.result_table.resizeColumnsToContents()
        self.ui.result_table.verticalHeader().setVisible(False)
        # Connect the table selection change to a function
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
    
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
    #Hàm dùng để load dữ liệu
#Giao diện thông tin của Quản Lý Lịch Sử Thao Tác
class LichSuDangKiAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LichSuThaoTac_Admin()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(8)
        self.ui.result_table.setHorizontalHeaderLabels(["Thao Tác", "Khu Vực Thao Tác", "Nội Dung Thao Tác", "Thời Gian Thao Tác","Trạng Thái", "Lý Do", "Người Thực Hiện", "Vai Trò"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.result_table.resizeColumnsToContents()
        self.ui.result_table.verticalHeader().setVisible(False)
        # Gọi hàm để tải dữ liệu
        self.load_data()
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
        
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
#Giao diện thông tin của Doanh Thu
class DoanhThuAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DoanhThu_Admin()
        self.ui.setupUi(self)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_main_admin_window)
        self.ui.btn_khoahoc.clicked.connect(self.open_khoahoc_admin_window)
        self.ui.btn_tailieu.clicked.connect(self.open_tailieu_admin_window)
        self.ui.btn_giangvien.clicked.connect(self.open_giangvien_admin_window)
        self.ui.btn_lophoc.clicked.connect(self.open_lophoc_admin_window)
        self.ui.btn_hocvien.clicked.connect(self.open_hocvien_admin_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_lichsudangki_admin_window)
        self.ui.btn_doanhthu.clicked.connect(self.open_doanhthu_admin_window)
        
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
#Phần giao diện bên user
#Giao diện thông tin chung
class GuiMainUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Guimain_User()
        self.ui.setupUi(self)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
#Giao diện tra cứu thông tin khóa học
class TraCuuKhoaHocUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui = Ui_TraCuuKhoaHoc_User()
        self.ui.setupUi(self)
        # Thiết lập tiêu đề cột cho QTableWidget
        self.ui.result_table.setColumnCount(4)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Khóa Học", "Tên Khóa Học", "Thời Lượng", "Học Phí"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Chọn cả dòng
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Tăng chiều cao của dòng
        self.ui.result_table.verticalHeader().setDefaultSectionSize(20)
        self.ui.result_table.verticalHeader().setVisible(False)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
#Giao diện tra cứu thông tin tài liệu
class TraCuuHocVienUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TraCuuHocVien_User()
        self.ui.setupUi(self)
        # Thiết lập tiêu đề cột cho QTableWidget
        self.ui.result_table.setColumnCount(8)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Học Viên", "Tên Học Viên", "Giới Tính", "Ngày Sinh", "Email", "CCCD", "Số Điện Thoại", "Địa Chỉ"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Chọn cả dòng
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Tăng chiều cao của dòng
        self.ui.result_table.verticalHeader().setDefaultSectionSize(20)
        self.load_data()
        self.ui.btn_tim.clicked.connect(self.search_hocvien)
        self.ui.btn_xoathongtin.clicked.connect(self.clear_line_edits)
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
#Giao diện tra cứu thông tin về học phí
class TraCuuLopHocUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TraCuuLopHoc_User()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(6)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Lớp", "Tên Lớp", "Mã Giảng Viên", "Mã Khoa Học", "Số Lượng Tối Đa", "Số Lượng Hiện có"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window) 
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
#Giao diện đăng kí học viên
class DangKiHocVienUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangKiHocVien_User()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(8)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Học Viên", "Tên Học Viên", "Giới Tính", "Ngày Sinh", "Email","CCCD", "Số Điện Thoại", "Địa Chỉ"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.result_table.resizeColumnsToContents()
        # Connect the table selection change to a function
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
    #Hàm dùng để load dữ liệu
    def load_data(self):
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="dangkikhoahoc"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM hocvien")

            rows = cursor.fetchall()

            self.ui.result_table.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    self.ui.result_table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

            cursor.close()
            connection.close()
        except pymysql.connect.Error as err:
            print(f"Lỗi: {err}")
    #Hàm dùng để thêm dữ liệu từ bảng trên csdl     
    def add_hocvien(self):
        # Lấy dữ liệu từ các trường nhập liệu
        mahocvien = self.ui.mahocvien.text()
        tenhocvien = self.ui.ten.text()
        gioitinh = self.ui.Gioitinh.currentText()
        ngaysinh = self.ui.ngaysinh.text()
        email = self.ui.email.text()
        cccd = self.ui.socccd.text()
        sodienthoai = self.ui.sodienthoai.text()
        diachi = self.ui.diachi.text()

        # Thêm dữ liệu vào cơ sở dữ liệu MySQL
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="dangkikhoahoc"
            )
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO hocvien (MaHocVien, HoTen, GioiTinh, NgaySinh, Email, CCCD, SoDienThoai, DiaChi)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (mahocvien, tenhocvien, gioitinh, ngaysinh, email, cccd, sodienthoai, diachi))

            connection.commit()

            # Cập nhật giao diện để hiển thị giảng viên mới trong bảng
            row_position = self.ui.result_table.rowCount()
            self.ui.result_table.insertRow(row_position)
            self.ui.result_table.setItem(row_position, 0, QTableWidgetItem(mahocvien))
            self.ui.result_table.setItem(row_position, 1, QTableWidgetItem(tenhocvien))
            self.ui.result_table.setItem(row_position, 2, QTableWidgetItem(gioitinh))
            self.ui.result_table.setItem(row_position, 3, QTableWidgetItem(ngaysinh))
            self.ui.result_table.setItem(row_position, 4, QTableWidgetItem(email))
            self.ui.result_table.setItem(row_position, 5, QTableWidgetItem(cccd))
            self.ui.result_table.setItem(row_position, 6, QTableWidgetItem(sodienthoai))
            self.ui.result_table.setItem(row_position, 7, QTableWidgetItem(diachi))

            # Thêm bản ghi vào bảng lichsuthaotac
            thao_tac = "Thêm học viên"
            khu_vuc = "Đăng Kí Học Viên"
            noi_dung = f"Thêm học viên {tenhocvien}"
            thoi_gian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            trang_thai = "Thành công"
            ly_do = "Thêm học viên {tenhocvien} thành công"
            cursor.execute("""
                INSERT INTO lichsuthaotac (ThaoTac, KhuVuc, NoiDung, thoiGian, TrangThai, LyDo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (thao_tac, khu_vuc, noi_dung, thoi_gian, trang_thai, ly_do))

            connection.commit()

            cursor.close()
            connection.close()
        except pymysql.MySQLError as err:
            print(f"Error: {err}")

            # Thêm bản ghi vào bảng lichsuthaotac khi thất bại
            try:
                connection = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="dangkikhoahoc"
                )
                cursor = connection.cursor()
                thao_tac = "Thêm học viên"
                khu_vuc = "Đăng Kí Học Viên"
                noi_dung = f"Thêm học viên {tenhocvien}"
                thoi_gian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                trang_thai = "Thất bại"
                ly_do = str(err)
                cursor.execute("""
                    INSERT INTO lichsuthaotac (ThaoTac, KhuVuc, NoiDung, thoiGian, TrangThai, LyDo)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (thao_tac, khu_vuc, noi_dung, thoi_gian, trang_thai, ly_do))
                
                connection.commit()
                cursor.close()
                connection.close()
            except pymysql.MySQLError as err:
                print(f"Error logging to lichsuthaotac: {err}")

    #Hàm dùng để xóa dữ liệu từ bảng trên csdl
    def delete_hocvien(self):
        # Lấy hàng đã chọn
        selected_row = self.ui.result_table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "No Selection", "Please select a lecturer to delete.")
            return

        # Lấy mã học viên từ hàng đã chọn
        mahocvien_item = self.ui.result_table.item(selected_row, 0)
        if mahocvien_item is None:
            QMessageBox.warning(self, "Error", "Failed to get the selected lecturer ID.")
            return

        mahocvien = mahocvien_item.text()

        # Xóa dữ liệu từ cơ sở dữ liệu MySQL
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="dangkikhoahoc"
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM hocvien WHERE MaHocVien = %s", (mahocvien,))
            connection.commit()
            cursor.close()
            connection.close()

            # Xóa hàng đã chọn từ bảng giao diện
            self.ui.result_table.removeRow(selected_row)
        except pymysql.connect.Error as err:
            print(f"Error: {err}")
    #Hàm dùng để tìm dữ liệu từ bảng trên csdl
    def search_hocvien(self):
        # Lấy dữ liệu từ các trường nhập liệu
        mahocvien = self.ui.mahocvien.text()
        hoten = self.ui.ten.text()
        gioitinh = self.ui.Gioitinh.currentText()
        ngaysinh = self.ui.ngaysinh.text()
        email = self.ui.email.text()
        cccd = self.ui.socccd.text()
        sodienthoai = self.ui.sodienthoai.text()
        diachi = self.ui.diachi.text()

        # Tạo điều kiện tìm kiếm
        search_conditions = []
        params = []

        if mahocvien:
            search_conditions.append("MaHocVien LIKE %s")
            params.append(f"%{mahocvien}%")
        if hoten:
            search_conditions.append("HoTen LIKE %s")
            params.append(f"%{hoten}%")
        if gioitinh and gioitinh != "All":
            search_conditions.append("GioiTinh LIKE %s")
            params.append(f"%{gioitinh}%")
        if ngaysinh:
            search_conditions.append("NgaySinh LIKE %s")
            params.append(f"%{ngaysinh}%")
        if email:
            search_conditions.append("Email LIKE %s")
            params.append(f"%{email}%")
        if cccd:
            search_conditions.append("CCCD LIKE %s")
            params.append(f"%{cccd}%")
        if sodienthoai:
            search_conditions.append("SoDienThoai LIKE %s")
            params.append(f"%{sodienthoai}%")
        if diachi:
            search_conditions.append("DiaChi LIKE %s")
            params.append(f"%{diachi}%")

        if not search_conditions:
            QMessageBox.warning(self, "No Input", "Please enter at least one search criteria.")
            return

        search_query = "SELECT * FROM hocvien WHERE " + " AND ".join(search_conditions)

        try:
            # Kết nối đến cơ sở dữ liệu MySQL
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="dangkikhoahoc"
            )
            cursor = connection.cursor()
            cursor.execute(search_query, params)
            results = cursor.fetchall()
            cursor.close()
            connection.close()

            # Xóa kết quả hiện tại trong bảng
            self.ui.result_table.setRowCount(0)

            # Hiển thị kết quả tìm kiếm trong bảng
            for row_number, row_data in enumerate(results):
                self.ui.result_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.result_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except pymysql.MySQLError as err:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {err}")
        except Exception as err:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {err}")
    #Hàm dùng để cập nhật dữ liệu từ bảng trên csdl
    def update_hocvien(self):
        # Lấy dữ liệu từ các trường nhập liệu
        mahocvien = self.ui.mahocvien.text()
        tenhocvien = self.ui.ten.text()
        gioitinh = self.ui.Gioitinh.currentText()
        ngaysinh = self.ui.ngaysinh.text()
        email = self.ui.email.text()
        cccd = self.ui.socccd.text()
        sodienthoai = self.ui.sodienthoai.text()
        diachi = self.ui.diachi.text()

        # Cập nhật dữ liệu trong cơ sở dữ liệu MySQL
        try:
            # Kết nối đến cơ sở dữ liệu MySQL
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="dangkikhoahoc"
            )
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE hocvien
                SET  HoTen = %s, GioiTinh = %s, NgaySinh = %s,  Email = %s,  CCCD = %s,  SoDienThoai = %s,  DiaChi = %s
                WHERE MaHocVien = %s
            """, (tenhocvien, gioitinh, ngaysinh, email, cccd, sodienthoai, diachi, mahocvien ))

            connection.commit()
            cursor.close()
            connection.close()

            QMessageBox.information(self, "Success", "Document updated successfully.")
            self.load_data()
        except pymysql.connect.Error as err:
            print(f"Error: {err}")
            QMessageBox.warning(self, "Error", "Failed to update document.")
    #Hàm dùng để chọn dữ liệu từ bảng trên csdl
    # Phần load dữ liệu vào ô ngày sinh chưa xong
    def select_line_edits(self):    
        selected_row = self.ui.result_table.currentRow()
        if selected_row < 0:
            return

        mahocvien = self.ui.result_table.item(selected_row, 0).text()
        tenhocvien = self.ui.result_table.item(selected_row, 1).text()
        gioitinh = self.ui.result_table.item(selected_row, 2).text()
        ngaysinh = self.ui.result_table.item(selected_row, 3).text()
        email = self.ui.result_table.item(selected_row, 4).text()
        cccd = self.ui.result_table.item(selected_row, 5).text()
        sodienthoai = self.ui.result_table.item(selected_row, 6).text()
        diachi = self.ui.result_table.item(selected_row,7).text()
        
        self.ui.mahocvien.setText(mahocvien)
        self.ui.ten.setText(tenhocvien)
        self.ui.Gioitinh.setCurrentText(gioitinh)
        self.ui.email.setText(email)
        self.ui.socccd.setText(cccd)
        self.ui.sodienthoai.setText(sodienthoai)
        self.ui.diachi.setText(diachi)
        
        # Convert ngaybatdau to QDate and set it
        date_parts = ngaysinh.split('-')
        date_obj = QDate(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
        self.ui.ngaysinh.setDate(date_obj)
    # Hàm dùng để xóa dữ liệu đã nhập trong phần lineEdit
    def clear_line_edits(self):
        self.ui.mahocvien.clear()
        self.ui.ten.clear()
        self.ui.Gioitinh.setCurrentIndex(0)
        self.ui.ngaysinh.clear()
        self.ui.socccd.clear()
        self.ui.email.clear()
        self.ui.sodienthoai.clear()
        self.ui.diachi.clear()
        self.load_data()
#Giao diện đăng kí khóa học
class DangKiKhoaHocUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dangkikhoahoc_User()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(8)
        self.ui.result_table.setHorizontalHeaderLabels(["Mã Học Viên", "Tên Học Viên", "Mã Khóa Học", "Tên Khóa Học", "Mã Lớp Học", "Tên Lớp Học", "Thời Gian", "Ngày Bắt Đầu"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.result_table.resizeColumnsToContents()
        self.ui.result_table.verticalHeader().setVisible(False)
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Gọi hàm để tải dữ liệu
        self.load_data()
        self.load_data_to_mahocvien()
        self.load_data_to_tenhocvien()
        self.load_data_to_makhoahoc()
        self.load_data_to_tenkhoahoc()
        self.load_data_to_malophoc()
        self.load_data_to_tenlophoc()
        self.ui.result_table.itemSelectionChanged.connect(self.select_line_edits)
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
        self.ui.btn_tim.clicked.connect(self.search_thongtin)
        self.ui.btn_xoathongtin.clicked.connect(self.clear_line_edits)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()
#Giao diện lịch sử thao tác hệ thống
class LichSuDangKiUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LichSuDangKi_User()
        self.ui.setupUi(self)
        self.ui.result_table.setColumnCount(6)
        self.ui.result_table.setHorizontalHeaderLabels(["Thao Tác", "Khu Vực Thao Tác", "Nội Dung Thao Tác", "Thời Gian Thao Tác","Trạng Thái", "Lý Do"])
        # Thiết lập kích thước cột tự động theo tỉ lệ
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.result_table.resizeColumnsToContents()
        # Gọi hàm để tải dữ liệu
        self.load_data()
        self.ui.btn_dangxuat.clicked.connect(self.open_dangxuat_window)
        self.ui.btn_thongtinchung.clicked.connect(self.open_GuiMain_User_window)
        self.ui.btn_tracuukhoahoc.clicked.connect(self.open_TraCuuKhoaHoc_User_window)
        self.ui.btn_tracuuhocvien.clicked.connect(self.open_TraCuuHocVien_User_window)
        self.ui.btn_tracuulophoc.clicked.connect(self.open_TraCuuLopHoc_User_window)
        self.ui.btn_dangkihocvien.clicked.connect(self.open_DangKiHocVien_User_window)
        self.ui.btn_dangkikhoahoc.clicked.connect(self.open_DangKiKhoaHoc_User_window)
        self.ui.btn_lichsudangki.clicked.connect(self.open_LichSuDangKi_User_window)
    # Thực hiện hành động chuyển trang  
    def open_dangxuat_window(self):
        self.logout = LoginWindow()
        self.logout.show()
        self.hide()
    def open_GuiMain_User_window(self):
        self.Guimain_user = GuiMainUserWindow()
        self.Guimain_user.show()
        self.hide()
    def open_TraCuuKhoaHoc_User_window(self):
        self.tracuukhoahoc_user = TraCuuKhoaHocUserWindow()
        self.tracuukhoahoc_user.show()
        self.hide()
    def open_TraCuuHocVien_User_window(self):
        self.tracuuhocvien_user = TraCuuHocVienUserWindow()
        self.tracuuhocvien_user.show()
        self.hide()
    def open_TraCuuLopHoc_User_window(self):
        self.tracuulophoc_user = TraCuuLopHocUserWindow()
        self.tracuulophoc_user.show()
        self.hide()
    def open_DangKiHocVien_User_window(self):
        self.dangkihocvien_user = DangKiHocVienUserWindow()
        self.dangkihocvien_user.show()
        self.hide()
    def open_DangKiKhoaHoc_User_window(self):
        self.dangkikhoahoc_user = DangKiKhoaHocUserWindow()
        self.dangkikhoahoc_user.show()
        self.hide()
    def open_LichSuDangKi_User_window(self):
        self.lichsudangki_user = LichSuDangKiUserWindow()
        self.lichsudangki_user.show()
        self.hide()

#Hàm chạy chương trình
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())    