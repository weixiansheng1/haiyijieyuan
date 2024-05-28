from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class WidgetDelegate (QStyledItemDelegate):
    def __init__(self, parent,value_data):
           super(WidgetDelegate, self).__init__(parent)
           self.value_data = value_data

    def createEditor(self, parent, option, index): 
        combo = QComboBox(parent)
        for idx,label in enumerate(self.value_data):
            combo.addItem(label)
        return combo
    
    def setEditorData(self, editor, index):  
        # 从model中读数据，更新Editor的显示值 
        # 读取当前节点的值
        value = index.model().data(index, Qt.EditRole)   
        if isinstance(value,int):
            value = str(value)
        print(f"cell ({index.row()},{index.column()}) data: {value}")     
        if value:   # 如果不在combo中，添加进来。
            if not editor.findText(value):
                editor.addItem(value)
            editor.setCurrentText(value)   # 将选择值设为current
        else:
             editor.setCurrentIndex(0)

    def setModelData(self, editor, model, index):   
        # 从editor值更新model数据
        model.setData(index, editor.currentText(),  Qt.EditRole)
        
    def commitAndCloseEditor(self):
        """Commits the data and closes the editor. :) """
        editor = self.sender()
        # The commitData signal must be emitted when we've finished editing
        self.commitData.emit(editor)
        #delegate完成编辑后，应发送closeEditor ()信号通知其它组件。
        self.closeEditor.emit(editor)

class MyWin(QMainWindow):
    def __init__(self) -> None:
        super(MyWin, self).__init__()
        self.setGeometry(400, 200, 1200, 700)
        self.conn = QSqlDatabase.addDatabase("QSQLITE")
        self.conn.setDatabaseName("sqlite.db")
        ok = self.conn.open()
        if not ok: 
            print("Unable to open data source file.")
            print("Connection failed: ", self.conn.lastError().text())
            sys.exit(1) # Error code 1 - signifies error in opening fil

        self.initUI()
    
    def initUI(self):
        self.model = QSqlRelationalTableModel(None,self.conn)
        self.model.setTable("stores")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.model.select()
        headers = ['store_id','store_name','phone','state']
        for columnIndex, header in enumerate(headers):
            self.model.setHeaderData(columnIndex, Qt.Horizontal, header)
        
        # 创建 delegate对象
        slist = ['江苏', '山东', '广西', "辽宁"]
        delegate = WidgetDelegate(self,slist)      
            
        self.table_view = QTableView()
        self.table_view.setModel(self.model)      # 绑定model 
        self.table_view.setItemDelegateForColumn(3, delegate)  # 设定第4列使用自定义delegate        
        self.table_view.resizeColumnsToContents()
        self.setCentralWidget(self.table_view)
        
    
    def closeEvent(self, event):
        # 关闭数据库
        self.conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MyWin()
    win.show()
    sys.exit(app.exec_())


