
from PyQt5.QtCore import QPropertyAnimation, QRect, pyqtSignal, Qt,QSettings,QVariant
from PyQt5.QtWidgets import  QDialog, QVBoxLayout, QCalendarWidget, QLabel, QPushButton,QComboBox

class DateRangePicker(QDialog):
    date_range_confirmed = pyqtSignal()  # 定义信号
    def __init__(self):
        super().__init__()

        # 读取设置文件
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("选择日期范围")

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("开始日期:"))
        self.start_calendar = QCalendarWidget(self)
        self.start_calendar.setGridVisible(True)
        layout.addWidget(self.start_calendar)

        layout.addWidget(QLabel("结束日期:"))
        self.end_calendar = QCalendarWidget(self)
        self.end_calendar.setGridVisible(True)
        layout.addWidget(self.end_calendar)

        layout.addWidget(QLabel("选择检查类型:"))
        categories   = self.settings.value("检查类型下拉列表"     , QVariant("")).split(',') # ["自查", "查收运","查行政与应急","海宜查", "政府部门查", "安保部查"]
        
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(categories)
        layout.addWidget(self.category_combobox)

        self.submit_button = QPushButton("确认", self)
        self.submit_button.clicked.connect(self.emit)
        layout.addWidget(self.submit_button)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(100)
        self.animation.setLoopCount(3)
        self.original_geometry = self.geometry()


        

    def confirm_dates(self):
        start_date = self.start_calendar.selectedDate().toString("yyyy-MM-dd")
        end_date   = self.end_calendar.selectedDate().toString("yyyy-MM-dd")
        select     = self.category_combobox.currentText()
        return start_date,end_date,select
    
    def emit(self):
        self.accept()
        self.date_range_confirmed.emit()  # 发射信号
    
    def eventFilter(self, obj, event):
        if event.type() == event.WindowDeactivate:
            self.animate_window()
        return super().eventFilter(obj, event)

    def animate_window(self):
        geom = self.geometry()
        self.animation.setStartValue(geom)
        new_geom = QRect(geom.x() - 10, geom.y() - 10, geom.width(), geom.height())
        self.animation.setEndValue(new_geom)
        self.animation.start()

    def closeEvent(self, event):
        event.ignore()


    # def leaveEvent(self, event):
    #     QMessageBox.warning(self, "警告", "请确认选择日期范围！", QMessageBox.Ok)



# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main Window")
#         self.setGeometry(100, 100, 400, 300)

#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         self.open_picker_button = QPushButton("Open Date Range Picker", self)
#         self.open_picker_button.setEnabled(False)
#         layout.addWidget(self.open_picker_button)

#         # 创建日期选择器
#         self.date_picker = DateRangePicker()
#         self.date_picker.date_range_confirmed.connect(lambda: self.enable_button_radio.setChecked(False))


#     def open_date_picker(self):
#         if self.date_picker.exec_() == QDialog.Accepted:
#             print("Date Range Selected Successfully")
#         else:
#             print("Date Range Selection Cancelled")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())