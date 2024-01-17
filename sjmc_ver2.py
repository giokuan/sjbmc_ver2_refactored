from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem, QStyledItemDelegate
from PyQt5.QtCore import QDate, Qt
import sqlite3
from PIL import Image
import os
from PyQt5.QtGui import QPixmap, QFont
from datetime import datetime
import random



# class ImageDelegate(QStyledItemDelegate):
#       def paint(self, painter, option, index):
#         value = index.data(14)  # Use the correct index for the photo column
#         if value is not None:
#             pixmap = QtGui.QPixmap()
#             pixmap.loadFromData(value)
#             painter.drawPixmap(option.rect, pixmap)
#         else:
#             super().paint(painter, option, index)

class Ui_MainWindow(object):
 
   
    # def drop_database(database_file):
    #     try:
    #         os.remove(database_file)
    #         print(f"Database '{database_file}' dropped successfully.")
    #     except FileNotFoundError:
    #         print(f"Database '{database_file}' not found.")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")

    # database_file = 'sjmc.db'
    # drop_database(database_file)
        

    def create_database(self):
        conn = sqlite3.connect("sjmc.db")
        cur = conn.cursor()

        # Create the projecttau3 table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS sjmc_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                T_birth DATE,
                email TEXT,
                phone TEXT,
                aka TEXT,
                gt TEXT,
                batch_name TEXT,
                current_chapter TEXT,
                root_chapter TEXT,
                stat TEXT,
                address TEXT,
                custom_member_id TEXT,
                photo BLOB
                   
            )
        ''')

        self.messageBox("Information", "database created")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()



    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 5px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.resize(600, 600)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 


    def exit_app(self):
        """ close or exit the app"""
        msg=QMessageBox()
        msg.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75); \
            border-radius: 5px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 170, 127);}') 
        msg.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you wan't to Exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.resize(600, 600)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            sys.exit()
        if res == QMessageBox.Cancel:
            pass 

    
    def browse_image(self):
        """ enable you to choose or browse image in your computer file"""
        filename = QFileDialog.getOpenFileName( caption = "Open file", directory=None, filter="Image (*.png * .jpg);;All Files(*.*)")   
        self.addPic_edit.setText(filename[0])
        self.load_image()


    def load_image(self):
        """Load image from your computer"""
        p = self.addPic_edit.text()
        self.picture_label.setPixmap(QtGui.QPixmap(p)) 

    
    
    # def generate_custom_member_id(self, lname, fname, mname, tbirth):
    #     """Generate a custom member ID based on name initials, tbirth, and random 4 digits"""
    #     name_initials = f"{lname[:4]}{fname[:4]}{mname[:4]}".upper()
    #     tbirth_part = tbirth.replace("-", "")
    #     random_digits = str(random.randint(1000, 9999))

    #     custom_member_id = f"{name_initials}{tbirth_part}{random_digits}"
    #     return custom_member_id


    def insert_data(self):
        """ Save the information in the database"""

        # Generate custom member ID

   

        p = self.addPic_edit.text()
        im = Image.open(p)
        im.save(p, quality=95)

        if len(p) == 0:
            self.messageBox("Add Photo", "You have no photo selected, \n Default Photo will be used!")
            self.default()
        else:
            with open(p, 'rb') as f:
                m = f.read()

            lname = self.lname_lineEdit.text()
            fname = self.fname_lineEdit.text()
            mname = self.mname_lineEdit.text()
            tbirth = self.tbirt_dateEdit.date()
            var_date = tbirth.toPyDate()
            email = self.email_lineEdit.text()
            phone = self.phone_lineEdit.text()
            aka = self.aka_lineEdit.text()
            gt = self.gt_lineEdit.text()
            batch = self.batch_name_lineEdit.text()
            current_chapter = self.current_chapter_lineEdit.text()
            root_chapter = self.root_chapter_lineEdit.text()
            status = self.status_comboBox.currentText()
            address = self.address_lineEdit.text()
        

            name_initials = f"{lname[:1]}{fname[:1]}{mname[:1]}".upper()
            # tbirth_part = tbirth.replace("-", "")
            tbirth_part = tbirth.toString("yyyyMMdd")
            random_digits = str(random.randint(1000, 9999))
            custom_member_id = f"{name_initials}{tbirth_part}{random_digits}"

            print("custom_member_id:", custom_member_id)


            mem_id = str(custom_member_id)

           


            # current = self.current_edit.text()
            # root = self.root_edit.text()
            # status = self.status_combobox.currentText()
            # address = self.address_edit.text()

            # Connect to SQLite3 database
            self.conn = sqlite3.connect("sjmc.db")

            query = ("INSERT INTO sjmc_table(last_name, first_name, middle_name, T_birth, email, phone, aka, gt, batch_name,  current_chapter, root_chapter, stat, address, photo, custom_member_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)")
            cur = self.conn.cursor()
            data = cur.execute(query, (lname.upper(), fname.upper(), mname.upper(), var_date, email, phone, aka.upper(), gt.upper(), batch.upper(),  current_chapter.upper(), root_chapter.upper(), status.upper(), address.upper(), m, mem_id))

            # # Commit the changes
            # self.conn.commit()

            # # Close the database connection
            # self.conn.close()

            if (data):
                msg=QMessageBox()
                if    len(lname) == 0:
                    self.messageBox("Information", " Last Name Cannot be empty!")
                    return
                elif  len(fname) == 0:
                    self.messageBox("Information", " First Name Cannot be empty!")
                    return
                elif  len(mname) == 0:
                    self.messageBox("Information", " Middle Name Cannot be empty!")
                    return
                
                elif  len(aka)  == 0:
                    self.messageBox("Information", " A.K.A Cannot be empty!")
                    return
                elif  len(batch) == 0:
                    self.messageBox("Information", " Batch Name Cannot be empty!")
                    return
                elif  tbirth.isNull():
                    self.messageBox("Information", " Triskelion Birth Cannot be empty!")
                    return
                elif  len(email) == 0:
                    self.messageBox("Information", " Email Name Cannot be empty!")
                    return
                elif  len(phone) == 0:
                    self.messageBox("Information", " Phone Cannot be empty!")
                    return
                elif  len(current_chapter)== 0:
                    self.messageBox("Information", " Current Chapter Cannot be empty!")
                    return
                elif  len(root_chapter)== 0:
                    self.messageBox("Information", " Root Chapter Cannot be empty!")
                    return
                elif  len(status)== 0:
                    self.messageBox("Information", " Status Cannot be empty!")
                    return
                elif  len(address) == 0:
                    self.messageBox("Information", " Address Cannot be empty!")
                    return
                

                else:
                    self.messageBox("Tau Gamma Phi", " Member Data Saved")
                    self.conn.commit()
                    #self.Savebutton.setEnabled(False)
                    #self.addbuttom.setEnabled(True)
                    # self.cancel()
                    self.loadData()
                    # self.total_res()

    # def insert_data(self, last_name, first_name, middle_name, T_birth, email, phone, aka, gt, batch_name, current_chapter, root_chapter, stat, address,):
    #     try:
    #         # Connect to SQLite3 database
    #         conn = sqlite3.connect("sjmc.db")
    #         cur = conn.cursor()

    #         # Generate custom member ID
    #         custom_member_id = self.generate_custom_member_id(last_name, first_name, middle_name, T_birth)

    #         p = self.addPic_edit.text()
    #         if len(p) == 0:
    #             self.messageBox("Add Photo", "You have no photo selected, \n Default Photo will be used!")
    #             self.default()
    #         else:
    #             with open(p, 'rb') as f:
    #                 m = f.read()

    #         last_name = self.lname_lineEdit.text()
    #         first_name = self.fname_lineEdit.text()
    #         middle_name = self.mname_lineEdit.text()
    #         tbirth = self.tbirt_dateEdit.date()
    #         T_birth = tbirth.toPyDate()
    #         email = self.email_lineEdit.text()
    #         phone = self.phone_lineEdit.text()
    #         aka = self.aka_lineEdit.text()
    #         gt = self.gt_lineEdit.text()
    #         batch_name = self.batch_name_lineEdit.text()
    #         current_chapter = self.current_chapter_lineEdit.text()
    #         root_chapter = self.root_chapter_lineEdit.text()
    #         stat = self.status_comboBox.currentText()
    #         address = self.address_lineEdit.text()
          

    #         # Insert data into the sjmc_table with the auto-incrementing primary key
    #         cur.execute('''
    #             INSERT INTO sjmc_table (
    #                 last_name, first_name, middle_name, T_birth, email, phone, aka, gt,
    #                 batch_name, current_chapter, root_chapter, stat, address, photo, custom_member_id
    #             ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #         ''', (last_name, first_name, middle_name, T_birth, email, phone, aka, gt,
    #               batch_name, current_chapter, root_chapter, stat, address, custom_member_id, m))

    #         self.messageBox("Information", "Data inserted successfully")

    #     except sqlite3.Error as e:
    #         print("Error Occurred:", e)
    #         self.messageBox("Error", f"Error occurred: {e}")

    #     finally:
    #         # Commit the changes and close the connection
    #         conn.commit()
    #         conn.close()
    #         self.loadData()

    def loadData(self):
        """Load data into the table"""

        try:
            # Connect to SQLite3 database
            conn = sqlite3.connect("sjmc.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM sjmc_table ORDER BY last_name ASC")
            result = cur.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except sqlite3.Error as e:
            print("Error Occurred:", e)
                    

    # def loadData(self):
    #     """Load data into the table"""

    #     try:
    #         # Connect to SQLite3 database
    #         with sqlite3.connect("sjmc.db") as conn:
    #             cur = conn.cursor()

    #             query = "SELECT * FROM sjmc_table ORDER BY last_name ASC"
    #             cur.execute(query)

    #             self.tableWidget.setRowCount(0)

    #             while True:
    #                 row_data = cur.fetchone()
    #                 if not row_data:
    #                     break

    #                 row_number = self.tableWidget.rowCount()
    #                 self.tableWidget.insertRow(row_number)

 
    #                 for column_number, data in enumerate(row_data):
    #                     self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

               


        # except sqlite3.Error as e:
        #     print("Error Occurred:", e)
                    
    # def loadData(self):
    #     """Load data into the table"""

    #     try:
    #         # Connect to SQLite3 database
    #         conn = sqlite3.connect("sjmc.db")
    #         cur = conn.cursor()

    #         cur.execute("SELECT * FROM sjmc_table ORDER BY last_name ASC")
    #         result = cur.fetchall()

    #         self.tableWidget.setRowCount(0)

    #         for row_number, row_data in enumerate(result):
    #             self.tableWidget.insertRow(row_number)

    #             for column_number, data in enumerate(row_data):
    #                 item = QTableWidgetItem()
    #                 if column_number == 15:  # Replace PHOTO_COLUMN_INDEX with the actual index of the 'photo' column
    #                     # Set a custom role to distinguish from other roles
    #                     item.setData(QtCore.Qt.UserRole + 1, data)
    #                 else:
    #                     item.setData(QtCore.Qt.DisplayRole, data)

    #                 self.tableWidget.setItem(row_number, column_number, item)

    #     except sqlite3.Error as e:
    #         print("Error Occurred:", e)


    # def cell_click(self, columnCount, rowCount):
    #     """Get specific information when clicking the member ID field"""

    #     try:
    #         # Connect to SQLite3 database
    #         conn = sqlite3.connect("sjmc.db")
    #         cur = conn.cursor()

    #         item = self.tableWidget.selectedItems()
    #         i = int(item[0].text())

    #         if rowCount != 0:
    #             return
    #         else:
    #             cur.execute("SELECT * FROM sjmc_table WHERE id=?", (i,))
    #             col = cur.fetchone()

    #             mem_id, lname, fname, mname, tbirth, email, phone, aka, gt, batch, current, root, status, adde, pic = col[1:16]

    #             # Set values in the UI elements
    #             self.id_lineEdit.setText(str(i))
    #             self.mem_id_lineEdit.setText(str(mem_id))
    #             self.lname_lineEdit.setText(lname)
    #             self.fname_lineEdit.setText(fname)
    #             self.mname_lineEdit.setText(mname)

    #             # Check for valid date before setting it in QDateEdit
    #             tbirth_date = None
    #             try:
    #                 tbirth_date = datetime.strptime(tbirth, '%Y-%m-%d').date()
    #             except ValueError as ve:
    #                 print(f"Error parsing tbirth: {ve}")
    #                 # Handle the case where tbirth is not in the expected format
    #                 # You might want to provide a default date or handle it based on your application logic

    #             if tbirth_date:
    #                 self.tbirt_dateEdit.setDate(tbirth_date)
    #             else:
    #                 print("Invalid tbirth date:", tbirth)

    #             # Continue setting other values in the UI elements
    #             self.email_lineEdit.setText(email)
    #             self.phone_lineEdit.setText(phone)
    #             self.aka_lineEdit.setText(aka)
    #             self.gt_lineEdit.setText(gt)
    #             self.batch_name_lineEdit.setText(batch)
    #             self.current_chapter_lineEdit.setText(current)
    #             self.root_chapter_lineEdit.setText(root)
    #             self.status_comboBox.setCurrentText(status)
    #             self.address_lineEdit.setText(adde)



    #             # Save the image to a file and display it
    #             with open('logo/pic.png', 'wb') as f:
    #                 f.write(pic)
    #             # with open("logo/pic.png", "wb") as f:
    #             #     f.write(pic.encode('utf-8') if isinstance(pic, str) else pic)
    #             self.addPic_edit.setText('logo/pic.png')
    #             self.picture_label.setPixmap(QPixmap("logo/pic.png"))
    #             # print("mem_id:", mem_id)
            



    #     except sqlite3.Error as e:
    #         print("Error Occurred:", e)
            
    def cell_click(self, columnCount, rowCount):
        """Get specific information when clicking the member ID field"""

        try:
            # Connect to SQLite3 database
            conn = sqlite3.connect("sjmc.db")
            cur = conn.cursor()

            item = self.tableWidget.selectedItems()
            i = int(item[0].text())

            if rowCount != 0:
                return
            else:
                cur.execute("SELECT * FROM sjmc_table WHERE id=?", (i,))
                # cur.execute ("SELECT * from projecttau3 WHERE member_id=" +str(i))
                col = cur.fetchone()

                lname, fname, mname, tbirth, email, phone, aka1, gt, batch,  current, root, status, adde, mem_id, pic = col[1:16]

                # Set values in the UI elements
                self.id_lineEdit.setText(str(i))
                self.lname_lineEdit.setText(lname)
                self.fname_lineEdit.setText(fname)
                self.mname_lineEdit.setText(mname)
                tbirth_date = QDate.fromString(tbirth, "yyyy-MM-dd")
                self.tbirt_dateEdit.setDate(tbirth_date)
                self.email_lineEdit.setText(email)
                self.phone_lineEdit.setText(phone)
                self.aka_lineEdit.setText(aka1)
                self.gt_lineEdit.setText(gt)
                self.batch_name_lineEdit.setText(batch)
                self.current_chapter_lineEdit.setText(current)
                self.root_chapter_lineEdit.setText(root)
                self.status_comboBox.setCurrentText(status)
                self.address_lineEdit.setText(adde)
                self.mem_id_lineEdit.setText(str(mem_id))





                # Save the image to a file and display it
                with open('logo/pic.png', 'wb') as f:
                    f.write(pic)
                self.addPic_edit.setText('logo/pic.png')
                self.picture_label.setPixmap(QPixmap("logo/pic.png"))
              
        except sqlite3.Error as e:
            print("Error Occurred:", e)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 972)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setWindowFlags( QtCore.Qt.WindowMaximizeButtonHint )
        MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
    


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 180, 1281, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.loadData()
        self.tableWidget.cellClicked.connect(self.cell_click)
     
        


        self.addPic_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.addPic_edit.setGeometry(QtCore.QRect(90, 530, 71, 21))
        self.addPic_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.addPic_edit.setObjectName("addPic_edit")
        self.addPic_edit.setText("logo/Men.png")
        self.addPic_edit.hide()


        self.table_frame = QtWidgets.QFrame(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(20, 150, 1341, 381))
        self.table_frame.setAutoFillBackground(False)
        self.table_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_frame.setObjectName("table_frame")


        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(20, 10, 131, 131))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        


        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(170, 20, 1161, 101))
        font = QtGui.QFont()
        font.setFamily("Neo Tech")
        font.setPointSize(64)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")


        self.photo_frame = QtWidgets.QFrame(self.centralwidget)
        self.photo_frame.setGeometry(QtCore.QRect(20, 550, 221, 221))
        self.photo_frame.setStyleSheet("rgb (0, 170, 255)")
        self.photo_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.photo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photo_frame.setObjectName("photo_frame")


        self.picture_label = QtWidgets.QLabel(self.photo_frame)
        self.picture_label.setGeometry(QtCore.QRect(1, 1, 220, 220))
        self.picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.picture_label.setScaledContents(True)
        self.picture_label.setPixmap(QtGui.QPixmap("logo/Men.png")) 
       

        self.id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lineEdit.setGeometry(QtCore.QRect(20, 780, 221, 31))
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.id_lineEdit.hide()


        self.mem_id_label = QtWidgets.QLabel(self.centralwidget)
        self.mem_id_label.setGeometry(QtCore.QRect(20, 770, 221, 21))
        self.mem_id_label.setObjectName("mem_id__label")

        self.mem_id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mem_id_lineEdit.setGeometry(QtCore.QRect(20, 790, 221, 21))
        self.mem_id_lineEdit.setObjectName("mem_id_lineEdit")
        font = QtGui.QFont()
        # font = QFont("Arial", 12)  # Specify the font name and size
        self.mem_id_lineEdit.setFont(font)
        



        self.add_photo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_photo_btn.setGeometry(QtCore.QRect(20, 820, 111, 41))
        self.add_photo_btn.setObjectName("add_photo_btn")
        self.add_photo_btn.clicked.connect(self.browse_image)

        self.col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.col_btn.setGeometry(QtCore.QRect(140, 820, 101, 41))
        self.col_btn.setObjectName("col_btn")
        
        self.member_info_frame = QtWidgets.QFrame(self.centralwidget)
        self.member_info_frame.setGeometry(QtCore.QRect(250, 550, 1111, 311))
        self.member_info_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.member_info_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.member_info_frame.setObjectName("member_info_frame")


        self.lname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.lname_lineEdit.setGeometry(QtCore.QRect(20, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_lineEdit.setFont(font)
        self.lname_lineEdit.setObjectName("lineEdit")

        self.lname_label = QtWidgets.QLabel(self.member_info_frame)
        self.lname_label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lname_label.setObjectName("lname_label")


        self.fname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.fname_lineEdit.setGeometry(QtCore.QRect(240, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_lineEdit.setFont(font)
        self.fname_lineEdit.setObjectName("fname_lineEdit")

        self.Fname_label = QtWidgets.QLabel(self.member_info_frame)
        self.Fname_label.setGeometry(QtCore.QRect(240, 20, 71, 16))
        self.Fname_label.setObjectName("Fname_label")


        self.mname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.mname_lineEdit.setGeometry(QtCore.QRect(460, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mname_lineEdit.setFont(font)
        self.mname_lineEdit.setObjectName("mname_lineEdit")

        self.mname_label = QtWidgets.QLabel(self.member_info_frame)
        self.mname_label.setGeometry(QtCore.QRect(460, 20, 71, 16))
        self.mname_label.setObjectName("mname_label")


        self.current_chapter_label = QtWidgets.QLabel(self.member_info_frame)
        self.current_chapter_label.setGeometry(QtCore.QRect(680, 20, 101, 16))
        self.current_chapter_label.setObjectName("current_chapter_label")

        self.current_chapter_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.current_chapter_lineEdit.setGeometry(QtCore.QRect(680, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_chapter_lineEdit.setFont(font)
        self.current_chapter_lineEdit.setObjectName("current_chapter_lineEdit")

        self.root_chapter_label = QtWidgets.QLabel(self.member_info_frame)
        self.root_chapter_label.setGeometry(QtCore.QRect(900, 20, 101, 16))
        self.root_chapter_label.setObjectName("root_chapter_label")

        self.root_chapter_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.root_chapter_lineEdit.setGeometry(QtCore.QRect(900, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.root_chapter_lineEdit.setFont(font)
        self.root_chapter_lineEdit.setObjectName("root_chapter_lineEdit")


        self.aka_label = QtWidgets.QLabel(self.member_info_frame)
        self.aka_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.aka_label.setObjectName("aka_label")

        self.aka_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.aka_lineEdit.setGeometry(QtCore.QRect(20, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aka_lineEdit.setFont(font)
        self.aka_lineEdit.setObjectName("aka_lineEdit")


        self.tbirt_dateEdit = QtWidgets.QDateEdit(self.member_info_frame)
        self.tbirt_dateEdit.setGeometry(QtCore.QRect(240, 110, 191, 31))
        self.tbirt_dateEdit.setObjectName("tbirt_dateEdit")

        self.tbirt_label = QtWidgets.QLabel(self.member_info_frame)
        self.tbirt_label.setGeometry(QtCore.QRect(240, 90, 101, 16))
        self.tbirt_label.setObjectName("aka_label_2")


        self.gt_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.gt_lineEdit.setGeometry(QtCore.QRect(460, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gt_lineEdit.setFont(font)
        self.gt_lineEdit.setObjectName("gt_lineEdit")

        self.gt_label = QtWidgets.QLabel(self.member_info_frame)
        self.gt_label.setGeometry(QtCore.QRect(460, 90, 101, 16))
        self.gt_label.setObjectName("gt_label")


        self.phone_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.phone_lineEdit.setGeometry(QtCore.QRect(20, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_lineEdit.setFont(font)
        self.phone_lineEdit.setObjectName("phone_lineEdit")

        self.phone_label = QtWidgets.QLabel(self.member_info_frame)
        self.phone_label.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.phone_label.setObjectName("phone_label")


        self.email_label = QtWidgets.QLabel(self.member_info_frame)
        self.email_label.setGeometry(QtCore.QRect(240, 160, 101, 16))
        self.email_label.setObjectName("email_label")

        self.email_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(240, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName("email_lineEdit")


        self.address_label = QtWidgets.QLabel(self.member_info_frame)
        self.address_label.setGeometry(QtCore.QRect(20, 230, 101, 16))
        self.address_label.setObjectName("address_label")

        self.address_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.address_lineEdit.setGeometry(QtCore.QRect(20, 250, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_lineEdit.setFont(font)
        self.address_lineEdit.setObjectName("address_lineEdit")


        self.batch_name_label = QtWidgets.QLabel(self.member_info_frame)
        self.batch_name_label.setGeometry(QtCore.QRect(460, 160, 101, 16))
        self.batch_name_label.setObjectName("batch_name_label")

        self.batch_name_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.batch_name_lineEdit.setGeometry(QtCore.QRect(460, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batch_name_lineEdit.setFont(font)
        self.batch_name_lineEdit.setObjectName("batch_name_lineEdit")


        self.search_frame = QtWidgets.QFrame(self.member_info_frame)
        self.search_frame.setGeometry(QtCore.QRect(680, 110, 411, 101))
        self.search_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.search_frame.setObjectName("search_frame")


        self.search_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.search_radioButton.setGeometry(QtCore.QRect(210, 10, 71, 17))
        self.search_radioButton.setObjectName("search_radioButton")


        self.advance_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.advance_radioButton.setGeometry(QtCore.QRect(290, 10, 111, 20))
        self.advance_radioButton.setObjectName("advance_radioButton")


        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.search_btn.setObjectName("search_btn")


        self.advance_search_lname_lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.advance_search_lname_lineEdit.setGeometry(QtCore.QRect(10, 50, 191, 31))
        self.advance_search_lname_lineEdit.setObjectName("advance_search_lname_lineEdit")
        self.advance_search_fname_lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.advance_search_fname_lineEdit.setGeometry(QtCore.QRect(210, 50, 191, 31))
        self.advance_search_fname_lineEdit.setObjectName("advance_search_fname_lineEdit")


        self.status_label = QtWidgets.QLabel(self.member_info_frame)
        self.status_label.setGeometry(QtCore.QRect(680, 230, 101, 16))
        self.status_label.setObjectName("status_label")

        self.status_comboBox = QtWidgets.QComboBox(self.member_info_frame)
        self.status_comboBox.setGeometry(QtCore.QRect(680, 250, 191, 31))
        self.status_comboBox.setObjectName("status_comboBox")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")


        self.voluntas_label = QtWidgets.QLabel(self.member_info_frame)
        self.voluntas_label.setGeometry(QtCore.QRect(880, 240, 231, 41))
        self.voluntas_label.setText("")
        self.voluntas_label.setPixmap(QtGui.QPixmap("logo/voluntas.png"))
        self.voluntas_label.setScaledContents(True)
        self.voluntas_label.setObjectName("label")


        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 890, 191, 41))
        self.add_btn.setObjectName("add_btn")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(240, 890, 201, 41))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.insert_data)
      


        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(470, 890, 201, 41))
        self.cancel_btn.setObjectName("cancel_btn")

        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(700, 890, 201, 41))
        self.edit_btn.setObjectName("edit_btn")

        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(930, 890, 201, 41))
        self.refresh_btn.setObjectName("refresh_btn")
        # self.refresh_btn.clicked.connect(self.create_database)
     
        

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(1160, 890, 201, 41))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit_app)


        self.member_info_frame.raise_()
        self.table_frame.raise_()
        self.tableWidget.raise_()
        self.logo_label.raise_()
        self.title_label.raise_()
        self.mem_id_label.raise_()
        self.photo_frame.raise_()
        self.id_lineEdit.raise_()
        self.add_photo_btn.raise_()
        self.col_btn.raise_()
        self.add_btn.raise_()
        self.save_btn.raise_()
        self.cancel_btn.raise_()
        self.edit_btn.raise_()
        self.refresh_btn.raise_()
        self.exit_btn.raise_()
        self.addPic_edit.raise_()


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SJBMC DATABASE MANAGEMENT SYSTEM"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "PHOTO"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FIELD ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LAST NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FIRST NAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MIDDLE NAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T-BIRTH"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PHONE"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "AKA"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GT"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "BATCH NAME"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "CURR CHAPTER"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "ROOT CHAPTER"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "STATUS"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "ADDRESS"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "MEM ID"))
        self.title_label.setText(_translate("MainWindow", "SAN JUAN MUNICIPAL COUNCIL"))
        self.add_photo_btn.setText(_translate("MainWindow", "ADD PHOTO"))
        self.col_btn.setText(_translate("MainWindow", "COL"))
        self.lname_label.setText(_translate("MainWindow", "LAST NAME"))
        self.Fname_label.setText(_translate("MainWindow", "FIRST NAME"))
        self.mname_label.setText(_translate("MainWindow", "MIDDLE NAME"))
        self.mem_id_label.setText(_translate("MainWindow", "MEMBER ID"))
        self.current_chapter_label.setText(_translate("MainWindow", "CURRENT CHAPTER"))
        self.root_chapter_label.setText(_translate("MainWindow", "ROOT CHAPTER"))
        self.aka_label.setText(_translate("MainWindow", "AKA"))
        self.tbirt_label.setText(_translate("MainWindow", "T-BIRTH"))
        self.gt_label.setText(_translate("MainWindow", "GT"))
        self.phone_label.setText(_translate("MainWindow", "PHONE"))
        self.email_label.setText(_translate("MainWindow", "EMAIL"))
        self.address_label.setText(_translate("MainWindow", "ADDRESS"))
        self.batch_name_label.setText(_translate("MainWindow", "BATCH NAME"))
        self.search_radioButton.setText(_translate("MainWindow", "SEARCH"))
        self.advance_radioButton.setText(_translate("MainWindow", "ADVANCE SEARCH"))
        self.search_btn.setText(_translate("MainWindow", "SEARCH"))
        self.status_label.setText(_translate("MainWindow", "STATUS"))
        self.status_comboBox.setItemText(0, _translate("MainWindow", "ACTIVE"))
        self.status_comboBox.setItemText(1, _translate("MainWindow", "INACTIVE"))
        self.add_btn.setText(_translate("MainWindow", "ADD NEW"))
        self.save_btn.setText(_translate("MainWindow", "SAVE"))
        self.cancel_btn.setText(_translate("MainWindow", "CANCEL"))
        self.edit_btn.setText(_translate("MainWindow", "EDIT"))
        self.refresh_btn.setText(_translate("MainWindow", "REFRESH"))
        self.exit_btn.setText(_translate("MainWindow", "EXIT"))


   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
