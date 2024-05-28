# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:53:02 2024

@author: Microsoft
"""


import win32com.client
import win32print
import win32con

from PyQt5.QtWidgets      import QMessageBox,QDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore         import Qt

class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("打印设置")
        self.setWindowModality(Qt.ApplicationModal)            # 设置窗口模态
        
        self.printer = QPrinter()
        self.dialog  = QPrintDialog(self.printer, self)
        self.printer_name = self.printer.printerName()         # 获取用户选择的打印机名称
        self.print_count  = self.printer.copyCount()           # 获取打印份数

    # 设置打印窗口
    def print_window(self):

        if self.dialog.exec_() == QPrintDialog.Accepted:
            self.printer_name = self.printer.printerName()     # 获取用户选择的打印机名称
            self.orientation  = self.printer.orientation()     # 获取用户选择的打印方向：纵向0，横向1
            self.duplex_mode  = self.printer.duplex()          # 获取用户选择的双面打印：无0，长边翻转2，短边翻转3
            self.color_mode   = self.printer.colorMode()       # 获取用户选择的打印色彩：彩色1，黑白0
            self.page_range   = self.printer.printRange()      # 获取用户选择的打印页面范围：未被勾选0,被勾选1
            self.print_count  = self.printer.copyCount()       # 获取打印份数

            self.setup_printer()                               # 设置打印机参数

    # 设置打印机参数
    def setup_printer(self):

        handle   = win32print.OpenPrinter(self.printer_name)               # 获取打印机的当前设置
        defaults = win32print.GetPrinter(handle, 9)                        # 获取打印机设置，GetPrinter：打印机的句柄（handle）和级别（level 2或8），

        if not defaults['pDevMode']:                                       # 如果未设置设备模式，无法更改打印设置
            self.show_warning_message("无法获取打印机的设备模式")
            return False

        #print(dir(defaults['pDevMode']))

        # 打印方向
        if self.orientation ==0:
            print('纵向')
            defaults['pDevMode'].Orientation = win32con.DMORIENT_PORTRAIT  # 纵向
        else:
            print('横向')
            defaults['pDevMode'].Orientation = win32con.DMORIENT_LANDSCAPE # 横向

        # 设置双面打印
        if self.duplex_mode == 0:
            print('单面打印。')
            defaults['pDevMode'].Duplex      = win32con.DMDUP_SIMPLEX      # 普通 (非双工) 打印。
        elif self.duplex_mode == 2:
            print('长边')
            defaults['pDevMode'].Duplex      = win32con.DMDUP_VERTICAL     # 长边
        else:
            print('短边')
            defaults['pDevMode'].Duplex      = win32con.DMDUP_HORIZONTAL   # 短边

        # 打印色彩
        if self.color_mode == 1:
            print('彩色')
            defaults['pDevMode'].Color       = win32con.DMCOLOR_COLOR      # 彩色
        else:
            print('单色')
            defaults['pDevMode'].Color       = win32con.DMCOLOR_MONOCHROME # 单色

        win32print.SetPrinter(handle, 9, defaults, 0)                      # 更新打印机配置

        win32print.ClosePrinter(handle)                                    # 关闭打印机的句柄

        return True


    def run_printer(self,filePath):
        i = 0
        while i<self.print_count:
            if not filePath:
                QMessageBox.warning(self, "警告", "请指定文档路径")

            if '.docx' in filePath:                                # 使用 win32com.client 打印 Word 文档
               printer_object = win32com.client.DispatchEx('Word.Application')
               object_output = printer_object.Documents.Open(filePath)
               
            elif '.xlsx' in filePath: 
                printer_object = win32com.client.DispatchEx("Excel.Application")
                object_output = printer_object.Workbooks.Open(filePath)

            else:
                QMessageBox.warning(self, "警告", "不支持这个文件类型噢.")

            printer_object.ActivePrinter = self.printer_name

            object_output.PrintOut()                                          # 打印
            object_output.Close(False)
            printer_object.Quit()
            
            i += 1

    # def closeEvent(self, event):
    #     event.ignore()
    
    #%%    显示错误提示信息
    def show_warning_message(self,show_error_str):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("{}".format(show_error_str))
        message_box.setWindowTitle("警告")
        message_box.exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainApp()
#     mainWindow.show()
#     sys.exit(app.exec_())