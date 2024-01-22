from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import QDate, Qt
import sqlite3
from PIL import Image
import os
from PyQt5.QtGui import QPixmap, QColor
# from datetime import datetime
import random
from cert import Ui_MainClear
from statistics_chart import Ui_MainWindowStat




class Ui_MainWindow(object):
 

    def open_window(self):
        """ Open the cert form window"""
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowStat()
        self.ui.setupUi(self.window)
        self.window.show()


    def info_col(self):
        
        x = self.lname_lineEdit.text()
        y = self.fname_lineEdit.text()
        gt = self.gt_lineEdit.text()
        root = self.root_chapter_lineEdit.text()
        batch = self.batch_name_lineEdit.text()
        z = (y +" "+ x)
        tbirth = self.tbirt_dateEdit.text()       
        self.ui.ir_edit.setText(tbirth)
        self.ui.name_edit.setText(z)
        self.ui.gt_edit.setText(gt)
        self.ui.chapter_edit.setText(root)
        self.ui.batch_edit.setText(batch)


          
    def open_col(self):
        """ Open the cert form window"""
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainClear()
        self.ui.setupUi(self.window)
        #MainWindow.close()
        self.window.show()
        self.info_col()
  

        # chart_window = MyMainWindow(self)
        # chart_window.setGeometry(200, 200, 800, 600)
        # chart_window.exec_()
   
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
        

    # def create_database(self):
    #     conn = sqlite3.connect("sjmc.db")
    #     cur = conn.cursor()

    #     # Create the projecttau3 table if it doesn't exist
    #     cur.execute('''
    #         CREATE TABLE IF NOT EXISTS sjmc_table (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             last_name TEXT,
    #             first_name TEXT,
    #             middle_name TEXT,
    #             T_birth DATE,
    #             email TEXT,
    #             phone TEXT,
    #             aka TEXT,
    #             gt TEXT,
    #             batch_name TEXT,
    #             current_chapter TEXT,
    #             root_chapter TEXT,
    #             stat TEXT,
    #             address TEXT,
    #             custom_member_id TEXT,
    #             photo BLOB
                   
    #         )
    #     ''')

    #     self.messageBox("Information", "database created")

    #     # Commit the changes and close the connection
    #     conn.commit()
    #     conn.close()

    def default_pic(self):
        self.addPic_edit.setText("logo/Men.png")
        self.picture_label.setPixmap(QtGui.QPixmap("logo/Men.png")) 
        pass

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
        
            #GENERATE CUSTOM MEMBER ID
            name_initials = f"{lname[:1]}{fname[:1]}{mname[:1]}".upper()
            tbirth_part = tbirth.toString("yyyyMMdd")
            random_digits = str(random.randint(1000, 9999))
            custom_member_id = f"{name_initials}{tbirth_part}{random_digits}"

            mem_id = str(custom_member_id)

            # Connect to SQLite3 database
            self.conn = sqlite3.connect("sjmc.db")

            query = ("INSERT INTO sjmc_table(last_name, first_name, middle_name, T_birth, email, phone, aka, gt, batch_name,  \
                     current_chapter, root_chapter, stat, address, photo, custom_member_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)")
            cur = self.conn.cursor()
            data = cur.execute(query, (lname.upper(), fname.upper(), mname.upper(), var_date, email, phone, aka.upper(), gt.upper(), \
                                       batch.upper(),  current_chapter.upper(), root_chapter.upper(), status.upper(), address.upper(), m, mem_id))


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
                    self.save_btn.setEnabled(False)
                    self.add_btn.setEnabled(True)
                    self.cancel()
                    self.loadData()
                    # self.total_res()

   
    def update(self):
        """Update information and save information to the database"""

        p = self.addPic_edit.text()
        im = Image.open(p)
        im.save(p, quality=95)
        with open(p, 'rb') as f:
            m = f.read()

        id = self.id_lineEdit.text()
        mem_id = self.mem_id_lineEdit.text()
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
        current = self.current_chapter_lineEdit.text()
        root = self.root_chapter_lineEdit.text()
        status = self.status_comboBox.currentText()
        address = self.address_lineEdit.text()

        self.conn = sqlite3.connect("sjmc.db")
        cur = self.conn.cursor()

        sql = "UPDATE sjmc_table SET custom_member_id=?, last_name=?, first_name=?, middle_name=?, T_birth=?, email=?, phone=?, aka=?, gt=?, \
                batch_name=?,  current_chapter=?, root_chapter=?, stat=?, address=?, photo=? WHERE id=?"

        try:
            cur.execute(sql, (mem_id, lname.upper(), fname.upper(), mname.upper(), str(var_date), email, phone, aka.upper(), gt.upper(), \
                              batch.upper(),  current.upper(), root.upper(), status.upper(), address.upper(), m, id))
            self.conn.commit()
            self.messageBox("Tau Gamma Phi", "Member Data Updated")
            self.loadData()
            self.cell_click_disabledTextbox()
            self.update_btn.hide()
        except sqlite3.Error as e:
            self.messageBox("Error", f"An error occurred: {e}")
        finally:
            self.conn.close()



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
                    

    def edit(self):
        """ Edit the specific person in the database"""
        mem_id = self.id_lineEdit.text()
        if len(mem_id) == 0:
            self.messageBox("Tau Gamma Phi", "No Data Found")
            return
        else:
            self.lname_lineEdit.setEnabled(True)
            self.fname_lineEdit.setEnabled(True)
            self.mname_lineEdit.setEnabled(True)
            self.tbirt_dateEdit.setEnabled(True)
            self.email_lineEdit.setEnabled(True)
            self.phone_lineEdit.setEnabled(True)
            self.aka_lineEdit.setEnabled(True)
            self.gt_lineEdit.setEnabled(True)
            self.batch_name_lineEdit.setEnabled(True)
            self.current_chapter_lineEdit.setEnabled(True)
            self.root_chapter_lineEdit.setEnabled(True)
            self.status_comboBox.setEnabled(True)
            self.address_lineEdit.setEnabled(True)

            self.cancel_btn.setEnabled(True)
            self.add_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            self.edit_btn.setEnabled(False)
            self.add_photo_btn.setEnabled(True)
            self.update_btn.show()
            self.save_btn.hide()

            self.lname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.fname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.mname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.tbirt_dateEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.email_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.phone_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.aka_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.gt_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.batch_name_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.current_chapter_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.root_chapter_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.status_comboBox.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.address_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            
        

    def cell_click(self, columnCount, rowCount):
        """Get specific information when clicking the member ID field"""

        try:
            # Connect to SQLite3 database
            conn = sqlite3.connect("sjmc.db")
            cur = conn.cursor()

            items = self.tableWidget.selectedItems()

            if not items:
                return  # No item selected, nothing to do

            selected_text = items[0].text()

            if not selected_text.isdigit():
                # print(f"Invalid value: {selected_text}")
                return  # Not a valid integer, handle accordingly

            i = int(selected_text)

            if rowCount != 0:
                return
            else:
                cur.execute("SELECT * FROM sjmc_table WHERE id=?", (i,))
                col = cur.fetchone()

                lname, fname, mname, tbirth, email, phone, aka1, gt, batch, current, root, status, adde, mem_id, pic = col[1:16]

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
                self.cell_click_disabledTextbox()

                # Save the image to a file and display it
                with open('logo/pic.png', 'wb') as f:
                    f.write(pic)
                self.addPic_edit.setText('logo/pic.png')
                self.picture_label.setPixmap(QPixmap("logo/pic.png"))

        except sqlite3.Error as e:
            print("Error Occurred:", e)
        finally:
            # Close the database connection in the finally block
            conn.close()

    
    def cell_click_disabledTextbox(self):
        """ return to view mode"""
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.update_btn.hide()
        self.save_btn.show()

        self.lname_lineEdit.setEnabled(False)
        self.fname_lineEdit.setEnabled(False)
        self.mname_lineEdit.setEnabled(False)
        self.tbirt_dateEdit.setEnabled(False)
        self.email_lineEdit.setEnabled(False)
        self.phone_lineEdit.setEnabled(False)
        self.aka_lineEdit.setEnabled(False)
        self.gt_lineEdit.setEnabled(False)
        self.batch_name_lineEdit.setEnabled(False)
        self.current_chapter_lineEdit.setEnabled(False)
        self.root_chapter_lineEdit.setEnabled(False)
        self.status_comboBox.setEnabled(False)
        self.address_lineEdit.setEnabled(False)
        # self.camera_btn.setEnabled(False)

    def add(self):
        """ activate or enable all the fields """
        self.lname_lineEdit.setEnabled(True)
        self.fname_lineEdit.setEnabled(True)
        self.mname_lineEdit.setEnabled(True)
        self.tbirt_dateEdit.setEnabled(True)
        self.email_lineEdit.setEnabled(True)
        self.phone_lineEdit.setEnabled(True)
        self.aka_lineEdit.setEnabled(True)
        self.gt_lineEdit.setEnabled(True)
        self.batch_name_lineEdit.setEnabled(True)
        self.current_chapter_lineEdit.setEnabled(True)
        self.root_chapter_lineEdit.setEnabled(True)
        self.status_comboBox.setEnabled(True)
        self.address_lineEdit.setEnabled(True)

        self.edit_btn.setEnabled(False)
        self.add_btn.setEnabled(False)
        self.save_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)
        self.refresh_btn.setEnabled(False)
        self.add_photo_btn.setEnabled(True)

        self.lname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.fname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.mname_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.tbirt_dateEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.email_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.phone_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.aka_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.gt_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.batch_name_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.current_chapter_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.root_chapter_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.status_comboBox.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.address_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")

        self.lname_lineEdit.clear()
        self.fname_lineEdit.clear()
        self.mname_lineEdit.clear()
        self.tbirt_dateEdit.setDate(QDate.currentDate())
        self.email_lineEdit.clear()
        self.phone_lineEdit.clear()
        self.aka_lineEdit.clear()
        self.gt_lineEdit.clear()
        self.batch_name_lineEdit.clear()
        self.current_chapter_lineEdit.clear()
        self.root_chapter_lineEdit.clear()
        default_status = "ACTIVE"  # Change this to your actual default status
        self.status_comboBox.setCurrentText(default_status)
        self.address_lineEdit.clear()
        self.mem_id_lineEdit.clear()
        self.default_pic()


    def cancel(self):
        """Return to default """
        self.lname_lineEdit.setEnabled(False)
        self.fname_lineEdit.setEnabled(False)
        self.mname_lineEdit.setEnabled(False)
        self.tbirt_dateEdit.setEnabled(False)
        self.email_lineEdit.setEnabled(False)
        self.phone_lineEdit.setEnabled(False)
        self.aka_lineEdit.setEnabled(False)
        self.gt_lineEdit.setEnabled(False)
        self.batch_name_lineEdit.setEnabled(False)
        self.current_chapter_lineEdit.setEnabled(False)
        self.root_chapter_lineEdit.setEnabled(False)
        self.status_comboBox.setEnabled(False)
        self.address_lineEdit.setEnabled(False)

        self.edit_btn.setEnabled(True)
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.save_btn.show()
        self.update_btn.hide()
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.add_photo_btn.setEnabled(False)

        self.lname_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.fname_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.mname_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.tbirt_dateEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.email_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.phone_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.aka_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.gt_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.batch_name_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.current_chapter_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.root_chapter_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.status_comboBox.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.address_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")

        self.lname_lineEdit.clear()
        self.fname_lineEdit.clear()
        self.mname_lineEdit.clear()
        self.tbirt_dateEdit.setDate(QDate.currentDate())
        self.email_lineEdit.clear()
        self.phone_lineEdit.clear()
        self.aka_lineEdit.clear()
        self.gt_lineEdit.clear()
        self.batch_name_lineEdit.clear()
        self.current_chapter_lineEdit.clear()
        self.root_chapter_lineEdit.clear()
        self.status_comboBox.currentText()
        self.address_lineEdit.clear()
        self.mem_id_lineEdit.clear()
        self.default_pic()

    
    def refresh(self):
        """ Clear all the fields"""
        self.id_lineEdit.clear()
        self.lname_lineEdit.clear()
        self.fname_lineEdit.clear()
        self.mname_lineEdit.clear()
        self.tbirt_dateEdit.setDate(QDate.currentDate())
        self.email_lineEdit.clear()
        self.phone_lineEdit.clear()
        self.aka_lineEdit.clear()
        self.gt_lineEdit.clear()
        self.batch_name_lineEdit.clear()
        self.current_chapter_lineEdit.clear()
        self.root_chapter_lineEdit.clear()
        self.status_comboBox.currentText()
        self.address_lineEdit.clear()
        self.mem_id_lineEdit.clear()
        self.search_lineEdit.clear()
        self.advance_search_lname_lineEdit.clear()
        self.advance_search_fname_lineEdit.clear()
        
        self.lname_lineEdit.setEnabled(False)
        self.fname_lineEdit.setEnabled(False)
        self.mname_lineEdit.setEnabled(False)
        self.tbirt_dateEdit.setEnabled(False)
        self.email_lineEdit.setEnabled(False)
        self.phone_lineEdit.setEnabled(False)
        self.aka_lineEdit.setEnabled(False)
        self.gt_lineEdit.setEnabled(False)
        self.batch_name_lineEdit.setEnabled(False)
        self.current_chapter_lineEdit.setEnabled(False)
        self.root_chapter_lineEdit.setEnabled(False)
        default_status = "ACTIVE"  # Change this to your actual default status
        self.status_comboBox.setCurrentText(default_status)
        self.address_lineEdit.setEnabled(False)

        self.edit_btn.setEnabled(True)
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.add_photo_btn.setEnabled(False)
        self.default_pic()
        self.loadData()


    def search_radio(self):
        self.search_btn.show()
        self.search_lineEdit.show()
        self.advance_search_btn.hide()
        self.advance_search_lname_lineEdit.hide()
        self.advance_search_fname_lineEdit.hide()
        self.advance_search_lname_lineEdit.clear()
        self.advance_search_fname_lineEdit.clear()


    def advance_radio(self):
        self.search_btn.hide()
        self.search_lineEdit.hide()
        self.advance_search_btn.show()
        self.advance_search_lname_lineEdit.show()
        self.advance_search_fname_lineEdit.show()
        self.search_lineEdit.clear()

    def search(self):
        """Return a person name or a chapter"""
        try:
            lname = self.search_lineEdit.text().strip()

            if not lname:
                self.messageBox("Information", "Search input cannot be empty.")
                return

            # Connect to SQLite3 database
            conn = sqlite3.connect("sjmc.db")
            cur = conn.cursor()

            # Use placeholders in the SQL query
            cur.execute("SELECT * FROM sjmc_table WHERE UPPER(last_name) = UPPER(?) OR UPPER(current_chapter) = UPPER(?)", (lname, lname))
            result = cur.fetchall()

            # counter = len(result)
            # self.total_res_edit.setText(str(counter))
            # if counter == 0:
            #     self.messageBox("Information", "No results found.")
            # else:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except sqlite3.Error as e:
            print("Error Occurred:", e)


    def advance_search(self):
        """ return specific person"""
        row = 0
       
        mydb =sqlite3.connect("sjmc.db")
            
        mycursor = mydb.cursor()
        lname = self.advance_search_lname_lineEdit.text()
        fname= self.advance_search_fname_lineEdit.text()
        mycursor.execute("SELECT * FROM sjmc_table WHERE last_name = '"+lname.upper()+"' AND first_name = '"+fname.upper()+"'");
        result = mycursor.fetchall()
        if len(lname) == 0 or len(fname) == 0:
            self.messageBox("Information", " Last Name or First Neme Field  Cannot be empty!")

        else:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 972)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #BACKGROUND LABEL
        self.back_label = QtWidgets.QLabel(self.centralwidget)
        self.back_label.setGeometry(QtCore.QRect(-10, 0, 1400, 980))
        self.back_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.back_label.setText("")
        self.back_label.setPixmap(QtGui.QPixmap("logo/back_pic.jpg"))
        self.back_label.setScaledContents(True)
        self.back_label.setObjectName("back_label")
       
        ###########----------TABLE-----------########
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 180, 1281, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        
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
        self.title_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.photo_frame = QtWidgets.QFrame(self.centralwidget)
        self.photo_frame.setGeometry(QtCore.QRect(20, 550, 221, 221))
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
        self.mem_id_label.setStyleSheet("color: rgb(255, 199, 4);")
        

        self.mem_id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mem_id_lineEdit.setGeometry(QtCore.QRect(20, 790, 221, 21))
        self.mem_id_lineEdit.setObjectName("mem_id_lineEdit")
        font = QtGui.QFont()
        self.mem_id_lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        # font = QFont("Arial", 12)  # Specify the font name and size
        self.mem_id_lineEdit.setFont(font)
        self.mem_id_lineEdit.setEnabled(False)
        

        self.add_photo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_photo_btn.setGeometry(QtCore.QRect(20, 820, 111, 41))
        self.add_photo_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.add_photo_btn.setObjectName("add_photo_btn")
        self.add_photo_btn.clicked.connect(self.browse_image)
        self.add_photo_btn.setEnabled(False)
        
        self.col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.col_btn.setGeometry(QtCore.QRect(140, 820, 101, 41))
        self.col_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.col_btn.setObjectName("col_btn")
        self.col_btn.clicked.connect(self.open_col)
        

        self.member_info_frame = QtWidgets.QFrame(self.centralwidget)
        self.member_info_frame.setGeometry(QtCore.QRect(250, 550, 1111, 311))
        self.member_info_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.member_info_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.member_info_frame.setObjectName("member_info_frame")


        self.lname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.lname_lineEdit.setGeometry(QtCore.QRect(20, 40, 191, 31))
        # self.lname_lineEdit.setStyleSheet("background-color:\
        # qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        # stop:1 rgba(255, 255, 255, 255));")
    
        font.setPointSize(10)
        self.lname_lineEdit.setFont(font)
        self.lname_lineEdit.setObjectName("lineEdit")
        self.lname_lineEdit.setEnabled(False)
        self.lname_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.lname_label = QtWidgets.QLabel(self.member_info_frame)
        self.lname_label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lname_label.setObjectName("lname_label")
        self.lname_label.setStyleSheet("color: rgb(255, 199, 4);")



        self.fname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.fname_lineEdit.setGeometry(QtCore.QRect(240, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_lineEdit.setFont(font)
        self.fname_lineEdit.setObjectName("fname_lineEdit")
        self.fname_lineEdit.setEnabled(False)
        self.fname_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.Fname_label = QtWidgets.QLabel(self.member_info_frame)
        self.Fname_label.setGeometry(QtCore.QRect(240, 20, 71, 16))
        self.Fname_label.setObjectName("Fname_label")
        self.Fname_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.mname_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.mname_lineEdit.setGeometry(QtCore.QRect(460, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mname_lineEdit.setFont(font)
        self.mname_lineEdit.setObjectName("mname_lineEdit")
        self.mname_lineEdit.setEnabled(False)
        self.mname_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.mname_label = QtWidgets.QLabel(self.member_info_frame)
        self.mname_label.setGeometry(QtCore.QRect(460, 20, 71, 16))
        self.mname_label.setObjectName("mname_label")
        self.mname_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.current_chapter_label = QtWidgets.QLabel(self.member_info_frame)
        self.current_chapter_label.setGeometry(QtCore.QRect(680, 20, 101, 16))
        self.current_chapter_label.setObjectName("current_chapter_label")
        self.current_chapter_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.current_chapter_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.current_chapter_lineEdit.setGeometry(QtCore.QRect(680, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_chapter_lineEdit.setFont(font)
        self.current_chapter_lineEdit.setObjectName("current_chapter_lineEdit")
        self.current_chapter_lineEdit.setEnabled(False)
        self.current_chapter_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.root_chapter_label = QtWidgets.QLabel(self.member_info_frame)
        self.root_chapter_label.setGeometry(QtCore.QRect(900, 20, 101, 16))
        self.root_chapter_label.setObjectName("root_chapter_label")
        self.root_chapter_label.setStyleSheet("color: rgb(255, 199, 4);")
        

        self.root_chapter_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.root_chapter_lineEdit.setGeometry(QtCore.QRect(900, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.root_chapter_lineEdit.setFont(font)
        self.root_chapter_lineEdit.setObjectName("root_chapter_lineEdit")
        self.root_chapter_lineEdit.setEnabled(False)
        self.root_chapter_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


        self.aka_label = QtWidgets.QLabel(self.member_info_frame)
        self.aka_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.aka_label.setObjectName("aka_label")
        self.aka_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.aka_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.aka_lineEdit.setGeometry(QtCore.QRect(20, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aka_lineEdit.setFont(font)
        self.aka_lineEdit.setObjectName("aka_lineEdit")
        self.aka_lineEdit.setEnabled(False)
        self.aka_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


        self.tbirt_dateEdit = QtWidgets.QDateEdit(self.member_info_frame)
        self.tbirt_dateEdit.setGeometry(QtCore.QRect(240, 110, 191, 31))
        self.tbirt_dateEdit.setObjectName("tbirt_dateEdit")
        self.tbirt_dateEdit.setEnabled(False)
        self.tbirt_dateEdit.setDate(QDate.currentDate())
        self.tbirt_dateEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.tbirt_label = QtWidgets.QLabel(self.member_info_frame)
        self.tbirt_label.setGeometry(QtCore.QRect(240, 90, 101, 16))
        self.tbirt_label.setObjectName("aka_label_2")
        self.tbirt_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.gt_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.gt_lineEdit.setGeometry(QtCore.QRect(460, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gt_lineEdit.setFont(font)
        self.gt_lineEdit.setObjectName("gt_lineEdit")
        self.gt_lineEdit.setEnabled(False)
        self.gt_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.gt_label = QtWidgets.QLabel(self.member_info_frame)
        self.gt_label.setGeometry(QtCore.QRect(460, 90, 101, 16))
        self.gt_label.setObjectName("gt_label")
        self.gt_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.phone_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.phone_lineEdit.setGeometry(QtCore.QRect(20, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phone_lineEdit.setFont(font)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.phone_lineEdit.setEnabled(False)
        self.phone_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")

        self.phone_label = QtWidgets.QLabel(self.member_info_frame)
        self.phone_label.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.phone_label.setObjectName("phone_label")
        self.phone_label.setStyleSheet("color: rgb(255, 199, 4);")


        self.email_label = QtWidgets.QLabel(self.member_info_frame)
        self.email_label.setGeometry(QtCore.QRect(240, 160, 101, 16))
        self.email_label.setObjectName("email_label")
        self.email_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.email_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(240, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.email_lineEdit.setEnabled(False)
        self.email_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


        self.address_label = QtWidgets.QLabel(self.member_info_frame)
        self.address_label.setGeometry(QtCore.QRect(20, 230, 101, 16))
        self.address_label.setObjectName("address_label")
        self.address_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.address_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.address_lineEdit.setGeometry(QtCore.QRect(20, 250, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_lineEdit.setFont(font)
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.address_lineEdit.setEnabled(False)
        self.address_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


        self.batch_name_label = QtWidgets.QLabel(self.member_info_frame)
        self.batch_name_label.setGeometry(QtCore.QRect(460, 160, 101, 16))
        self.batch_name_label.setObjectName("batch_name_label")
        self.batch_name_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.batch_name_lineEdit = QtWidgets.QLineEdit(self.member_info_frame)
        self.batch_name_lineEdit.setGeometry(QtCore.QRect(460, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batch_name_lineEdit.setFont(font)
        self.batch_name_lineEdit.setObjectName("batch_name_lineEdit")
        self.batch_name_lineEdit.setEnabled(False)
        self.batch_name_lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


        self.search_frame = QtWidgets.QFrame(self.member_info_frame)
        self.search_frame.setGeometry(QtCore.QRect(680, 110, 411, 101))
        self.search_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.search_frame.setObjectName("search_frame")


        self.search_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.search_radioButton.setGeometry(QtCore.QRect(210, 10, 71, 17))
        self.search_radioButton.setObjectName("search_radioButton")
        self.search_radioButton.toggled.connect(self.search_radio)
        self.search_radioButton.setStyleSheet("color: rgb(255, 199, 4);")

        self.advance_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.advance_radioButton.setGeometry(QtCore.QRect(290, 10, 111, 20))
        self.advance_radioButton.setObjectName("advance_radioButton")
        self.advance_radioButton.toggled.connect(self.advance_radio)
        self.advance_radioButton.setStyleSheet("color: rgb(255, 199, 4);")

        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.search_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search)

        self.advance_search_btn = QtWidgets.QPushButton(self.search_frame)
        self.advance_search_btn.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.advance_search_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.advance_search_btn.setObjectName("advance_search_btn")
        self.advance_search_btn.hide()
        self.advance_search_btn.clicked.connect(self.advance_search)

        #SEARCH
        self.search_lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.search_lineEdit.setGeometry(QtCore.QRect(10, 50, 191, 31))
        self.search_lineEdit.setObjectName("search_lineEdit")


        #ADVANCE SEARCH
        self.advance_search_lname_lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.advance_search_lname_lineEdit.setGeometry(QtCore.QRect(10, 50, 191, 31))
        self.advance_search_lname_lineEdit.setObjectName("advance_search_lname_lineEdit")
        self.advance_search_lname_lineEdit.hide()

        self.advance_search_fname_lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.advance_search_fname_lineEdit.setGeometry(QtCore.QRect(210, 50, 191, 31))
        self.advance_search_fname_lineEdit.setObjectName("advance_search_fname_lineEdit")
        self.advance_search_fname_lineEdit.hide()
        

        self.status_label = QtWidgets.QLabel(self.member_info_frame)
        self.status_label.setGeometry(QtCore.QRect(680, 230, 101, 16))
        self.status_label.setObjectName("status_label")
        self.status_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.status_comboBox = QtWidgets.QComboBox(self.member_info_frame)
        self.status_comboBox.setGeometry(QtCore.QRect(680, 250, 191, 31))
        self.status_comboBox.setObjectName("status_comboBox")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.setEnabled(False)
        self.status_comboBox.setStyleSheet("color: rgb(0, 0, 0);")


        self.voluntas_label = QtWidgets.QLabel(self.member_info_frame)
        self.voluntas_label.setGeometry(QtCore.QRect(880, 205, 231, 121))
        self.voluntas_label.setText("")
        self.voluntas_label.setPixmap(QtGui.QPixmap("logo/vol.png"))
        self.voluntas_label.setScaledContents(True)
        self.voluntas_label.setObjectName("label")


        self.statistics_btn = QtWidgets.QPushButton(self.centralwidget)
        self.statistics_btn.setGeometry(QtCore.QRect(20, 890, 221, 41))
        self.statistics_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.statistics_btn.setObjectName("statistics_btn_btn")
        self.statistics_btn.clicked.connect(self.open_window)


        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(310, 890, 151, 41))
        self.add_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(490, 890, 151, 41))
        self.save_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.insert_data)
        self.save_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon)
      

        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(490, 890, 151, 41))
        self.update_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update)
        self.update_btn.hide()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon)
        

        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(670, 890, 151, 41))
        self.cancel_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cancel_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon)

        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(850, 890, 151, 41))
        self.edit_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)

        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(1030, 890, 151, 41))
        self.refresh_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.refresh)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon)
        

        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(1210, 890, 151, 41))
        self.exit_btn.setStyleSheet("background-color:\
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
        stop:1 rgba(255, 255, 255, 255));")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit_app)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)


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
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SJBMC DATABASE MANAGEMENT SYSTEM"))
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
        item.setText(_translate("MainWindow", "CHAPTER"))
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
        self.search_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Last Name or Chapter"))
        self.advance_search_lname_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Last Name"))
        self.advance_search_fname_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter First Name"))
        self.advance_search_btn.setText(_translate("MainWindow", "ADVANCE SEARCH"))
        self.status_label.setText(_translate("MainWindow", "STATUS"))
        self.status_comboBox.setItemText(0, _translate("MainWindow", "ACTIVE"))
        self.status_comboBox.setItemText(1, _translate("MainWindow", "INACTIVE"))
        self.status_comboBox.setItemText(2, _translate("MainWindow", "EXPELLED"))
        self.add_btn.setText(_translate("MainWindow", "  ADD NEW"))
        self.statistics_btn.setText(_translate("MainWindow", "  STATISTICS"))
        self.save_btn.setText(_translate("MainWindow", "  SAVE"))
        self.update_btn.setText(_translate("MainWindow", "  UPDATE"))
        self.cancel_btn.setText(_translate("MainWindow", "  CANCEL"))
        self.edit_btn.setText(_translate("MainWindow", "  EDIT"))
        self.refresh_btn.setText(_translate("MainWindow", "  REFRESH"))
        self.exit_btn.setText(_translate("MainWindow", "  EXIT"))


   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
