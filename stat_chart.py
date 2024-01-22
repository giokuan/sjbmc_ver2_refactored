import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Create a Matplotlib figure and add a subplot for the pie chart
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Add a subplot for the pie chart
        self.ax_pie = self.figure.add_subplot(121)

        # Fetch data from the database (replace this with your actual database connection and query)
        conn = sqlite3.connect('sjmc.db')
        cursor = conn.cursor()
        cursor.execute("SELECT stat, COUNT(*) FROM sjmc_table GROUP BY stat")
        data = cursor.fetchall()
        conn.close()

        # Extract data for labels and sizes
        labels, sizes = zip(*data)

        # Plot the pie chart
        self.ax_pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        self.ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        self.setWindowTitle("SJMC STATISTICS")

    def setupUi(self):
        self.lname_label = QtWidgets.QLabel(self)
        self.lname_label.setGeometry(QtCore.QRect(50, 50, 150, 30))  # Adjusted geometry
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_label.setFont(font)
        self.lname_label.setStyleSheet("color: black;")  # Changed text color for visibility
        self.lname_label.setObjectName("lname_label")
        _translate = QtCore.QCoreApplication.translate
        self.lname_label.setText("Total Member")

        # Set the label to be initially visible
        self.lname_label.setVisible(True)

        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self)
        self.lname_edit.setGeometry(QtCore.QRect(220, 140, 251, 31))
        self.lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.lname_edit.setFont(font)


    # def setupUi(self, MyMainWindow):
    #         MyMainWindow.setObjectName("MyMainWindow")
    #         MyMainWindow.resize(1129, 770)
    #         MyMainWindow.setMaximumSize(QtCore.QSize(1129, 770))
    #         MyMainWindow.setMinimumSize(QtCore.QSize(1129, 770))
    #         MyMainWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
    #         MyMainWindow.setStyleSheet("")
    #         self.centralwidget = QtWidgets.QWidget(MyMainWindow)
    #         self.centralwidget.setObjectName("centralwidget")
    #         icon = QtGui.QIcon()
    #         icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #         MyMainWindow.setWindowIcon(icon)

            
            


    def total_member(self):
        self.conn=sqlite3.connect("sjmc")
        cur=self.conn.cursor()
        cur.execute("SELECT *  FROM sjmc_table")
        member = cur.fetchall()
        #print(len(res))
        counter = len(member)
        self.total_res_edit.setText(str(counter))    






def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.setGeometry(100, 100, 800, 600)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyMainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MyMainWindow)
    MyMainWindow.show()
    sys.exit(app.exec_())