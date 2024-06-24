# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
# import mysql.connector

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Hiện dữ liệu từ bảng khoahoc")
#         self.setGeometry(100, 100, 600, 400)

#         self.tableWidget = QTableWidget(self)
#         self.tableWidget.setGeometry(50, 50, 500, 300)
#         self.tableWidget.setColumnCount(4)
#         self.tableWidget.setHorizontalHeaderLabels(["Makhoahoc", "Tenkhoahoc", "ThoiLuong", "NgayBatDau"])

#         self.load_data()

#     def load_data(self):
#         try:
#             # Kết nối đến cơ sở dữ liệu MySQL
#             connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="",
#                 database="dangkikhoahoc"
#             )
            
#             cursor = connection.cursor()
#             cursor.execute("SELECT * FROM khoahoc")

#             rows = cursor.fetchall()

#             self.tableWidget.setRowCount(len(rows))

#             for row_idx, row_data in enumerate(rows):
#                 for col_idx, col_data in enumerate(row_data):
#                     self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

#             cursor.close()
#             connection.close()
#         except mysql.connector.Error as err:
#             print(f"Lỗi: {err}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
# import mysql.connector

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("ComboBox từ MySQL")
#         self.setGeometry(100, 100, 300, 200)

#         self.combo_box = QComboBox(self)

        

#         # Lấy dữ liệu từ cơ sở dữ liệu và đổ vào ComboBox
#         self.populate_combo_box()

#     def populate_combo_box(self):
#         # Kết nối đến cơ sở dữ liệu MySQL
#         self.db_connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="dangkikhoahoc"
#         )
#         cursor = self.db_connection.cursor()
#         cursor.execute("SELECT MaLop FROM lophoc")

#         # Lấy tất cả các dòng dữ liệu từ truy vấn
#         rows = cursor.fetchall()

#         # Thêm dữ liệu vào ComboBox
#         for row in rows:
#             self.combo_box.addItem(row[0])

#         cursor.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QAction, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tạo các giao diện con
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("This is Widget 1"))
        self.widget1.setLayout(layout1)

        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("This is Widget 2"))
        self.widget2.setLayout(layout2)

        # Thiết lập QPushButton với menu
        self.pushButton = QPushButton("Menu Button", self)
        self.pushButton.setGeometry(50, 50, 100, 30)

        menu = QMenu(self)
        action1 = QAction("Show Widget 1", self)
        action2 = QAction("Show Widget 2", self)
        menu.addAction(action1)
        menu.addAction(action2)

        # Gắn menu vào pushButton
        self.pushButton.setMenu(menu)
        self.pushButton.setPopupMode(QPushButton.MenuButtonPopup)

        # Đặt pushButton vào giao diện chính
        self.setCentralWidget(QWidget())
        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(self.pushButton)

        # Kết nối các hành động với các hàm chuyển đổi giao diện
        action1.triggered.connect(lambda: self.change_widget(self.widget1))
        action2.triggered.connect(lambda: self.change_widget(self.widget2))

        # Đặt widget khởi đầu
        self.setCentralWidget(self.widget1)
        self.setGeometry(100, 100, 300, 200)

    def change_widget(self, widget):
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())



