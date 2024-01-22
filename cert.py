from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog, QPrinter
# from PyQt5.Qt import QFileInfo
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLineEdit, QDialog ,QFileDialog, QInputDialog, QDateEdit
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QDate

class Ui_MainClear(object):

    # def handlePaintRequest(self, printer):
    #     document = QtGui.QTextDocument()
    #     #cursor = QtGui.QTextCursor(document)
    #     document.print_(printer)

    def handlePaintRequest(self, printer):
        printer.setResolution(1000)
        printer.setPageMargins(6, 5, 6, 5, QPrinter.Millimeter)
        painter = QPainter()
        painter.begin(printer)
        screenPixmap = self.centralwidget.grab()
        screenPixmap = screenPixmap.scaledToWidth(int(screenPixmap.width() *10500/screenPixmap.width()))
        painter.drawPixmap(10,10, screenPixmap)
        painter.end()


    def printPreviewListMethod(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()


   
    

    def setupUi(self, MainClear):
        MainClear.setObjectName("MainClear")
        MainClear.resize(980, 830)
        MainClear.setStatusTip("")
        MainClear.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        MainClear.setMaximumSize(QtCore.QSize(980, 830))
        MainClear.setMinimumSize(QtCore.QSize(980, 830))
        self.centralwidget = QtWidgets.QWidget(MainClear)
        self.centralwidget.setObjectName("centralwidget")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainClear.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 980, 755))
        self.label.setStyleSheet("background-color: rgb(197, 224, 179);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo/cert.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        
        self.name_edit.setAlignment(QtCore.Qt.AlignCenter)              
        #self.name_edit.textChanged.connect(self.on_text_changed)
        
        self.name_edit.setGeometry(QtCore.QRect(307, 370, 500, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: transparent;")
        self.name_edit.setFrame(False)
        self.name_edit.setObjectName("name_edit")
                
        self.ir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ir_edit.setGeometry(QtCore.QRect(395, 468, 113, 20))
        self.ir_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.ir_edit.setFrame(False)
        self.ir_edit.setObjectName("ir_edit")

        self.gt_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.gt_edit.setGeometry(QtCore.QRect(396, 488, 265, 20))
        self.gt_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.gt_edit.setFrame(False)
        self.gt_edit.setObjectName("gt_edit")
        
        self.chapter_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.chapter_edit.setEnabled(True)
        self.chapter_edit.setGeometry(QtCore.QRect(396, 508, 261, 20))
        self.chapter_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.chapter_edit.setFrame(False)
        self.chapter_edit.setObjectName("chapter_edit")
        
        
        self.batch_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.batch_edit.setEnabled(True)
        self.batch_edit.setGeometry(QtCore.QRect(396, 528, 301, 20))
        self.batch_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: rgb(0, 0, 0);")
        self.batch_edit.setFrame(False)
        self.batch_edit.setObjectName("batch_edit")
        
        self.chairman_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.chairman_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.chairman_edit.setEnabled(True)
        self.chairman_edit.setGeometry(QtCore.QRect(667, 661, 190, 20))
        self.chairman_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: transparent;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chairman_edit.setFont(font)
        self.chairman_edit.setFrame(False)
        self.chairman_edit.setObjectName("chairman_edit")
        
        self.date_issued_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_issued_edit.setAlignment(QtCore.Qt.AlignCenter) 
        self.date_issued_edit.setEnabled(True)
        self.date_issued_edit.setGeometry(QtCore.QRect(298, 661, 160, 20))
        self.date_issued_edit.setStyleSheet("color: rgb(255, 244, 136);""background-color: transparent;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_issued_edit.setFont(font)
        self.date_issued_edit.setFrame(False)
        self.date_issued_edit.setObjectName("date_issued_edit")
        # self.date_issued_edit.setDate(QDate.currentDate())
        current_date = QDate.currentDate()
        # self.date_issued_edit.setDate(current_date)
        self.date_issued_edit.setText(current_date.toString("MM-dd-yyyy"))
        
       
        
        #PRINT BUTTON
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(360, 773, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("background-color: \
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(self.printPreviewListMethod)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon)



        MainClear.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainClear)
        QtCore.QMetaObject.connectSlotsByName(MainClear)


    def retranslateUi(self, MainClear):
        _translate = QtCore.QCoreApplication.translate
        MainClear.setWindowTitle(_translate("MainClear", "Certificate of Legitimacy"))

        self.print_btn.setText(_translate("MainClear", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainClear = QtWidgets.QMainWindow()
    ui = Ui_MainClear()
    ui.setupUi(MainClear)
    MainClear.show()
    sys.exit(app.exec_())
