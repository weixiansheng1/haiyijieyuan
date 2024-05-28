import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class SQLiteViewer(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SQLite Viewer')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.loadTable()

        self.setLayout(self.layout)
        
    # def queryRecord(self):
    #   room_id = int(self.room_Edit.text())
    #   date_id = self.date_Edit.text()
    #   self.model.setFilter(("CATEGORY = '%d'" % (room_id)))
    #   self.model.setFilter(("SHORTDESC = '%s'" % (date_id)))
    #   self.model.select()

    def loadTable(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.db_path)

        if not db.open():
            print("Failed to open database.")
            return

        query = QSqlQuery(db)
        query.exec_("SELECT name FROM sqlite_master WHERE type='table';")

        tables = []
        while query.next():
            tables.append(query.value(0))

        if not tables:
            print("No tables found in the database.")
            return

        table_name = tables[0]

        query.exec_(f"SELECT * FROM {table_name};")

        rows = []
        while query.next():
            row = [str(query.value(i)) for i in range(query.record().count())]
            rows.append(row)

        if not rows:
            print("No data found in the table.")
            return

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(rows[0]))

        headers = [query.record().fieldName(i) for i in range(query.record().count())]
        self.table.setHorizontalHeaderLabels(headers)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                self.table.setItem(i, j, item)

        db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = SQLiteViewer('洁源隐患数据库2024.db')  # Replace with your database file path
    viewer.show()
    sys.exit(app.exec_())