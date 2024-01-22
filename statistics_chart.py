from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sqlite3
from PyQt5.QtCore import Qt



class Ui_MainWindowStat(object):
    def __init__(self):
        # Initialize attributes, including canvas
        self.central_widget = None
        self.layout = None
        self.figure = None
        self.canvas = None
        self.ax_pie = None
        self.total_member_lineEdit = None
        self.chapter_lineEdits = {}



        # Create a Matplotlib figure and add a subplot for the pie chart
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        # self.ax_pie = self.figure.add_subplot(621)
        self.figure.patch.set_facecolor('#2e2d2d')
      

        
  
       
    def total_chapter(self):
        conn = sqlite3.connect('sjmc.db')
        cursor = conn.cursor()

        # Execute SQL query to count distinct chapters
        cursor.execute("SELECT COUNT(DISTINCT current_chapter) FROM sjmc_table")

        # Fetch the result
        total_distinct_chapters = cursor.fetchone()[0]
        self.total_chapter_lineEdit.setText(str(total_distinct_chapters))



    def display_total_chapter_members(self):
        # Connect to the database
        conn = sqlite3.connect('sjmc.db')
        cursor = conn.cursor()

        # Execute SQL query to get the total members for each chapter
        cursor.execute("SELECT current_chapter, COUNT(*) as total_members FROM sjmc_table GROUP BY current_chapter")

        # Fetch all the results
        chapter_member_counts = cursor.fetchall()

        # Display the total members in the corresponding QLineEdit widgets
        for chapter, total_members in chapter_member_counts:
            if chapter == "ABUNG":  
                self.Abung_lineEdit.setText(str(total_members))
            if chapter == "BALAGBAG": 
                self.balagbag_lineEdit.setText(str(total_members))
            if chapter == "BUHAYNASAPA": 
                self.buhaynasapa_lineEdit.setText(str(total_members))
            if chapter == "BULSA": 
                self.bulsa_lineEdit.setText(str(total_members))
            if chapter == "CALICANTO": 
                self.calicanto_lineEdit.setText(str(total_members))
            if chapter == "CALITCALIT": 
                self.calitcalit_lineEdit.setText(str(total_members))
            if chapter == "CALUBCUB": 
                self.calubcub_lineEdit.setText(str(total_members))
            if chapter == "HUGOM": 
                self.hugom_lineEdit.setText(str(total_members))
            if chapter == "IMELDA": 
                self.imelda_lineEdit.setText(str(total_members))
            if chapter == "LAIYA APLAYA": 
                self.aplaya_lineEdit.setText(str(total_members))
            if chapter == "LAIYA IBABAO": 
                self.ibabao_lineEdit.setText(str(total_members))
            if chapter == "MABALANOY": 
                self.mabalanoy_lineEdit.setText(str(total_members))
            if chapter == "MARAYKIT": 
                self.maraykit_lineEdit.setText(str(total_members))
            if chapter == "PALAHANAN": 
                self.palahanan_lineEdit.setText(str(total_members))
            if chapter == "POBLACION": 
                self.poblacion_lineEdit.setText(str(total_members))
            if chapter == "PUTING BUHANGIN": 
                self.putingbuhangin_lineEdit.setText(str(total_members))
            if chapter == "SAMPIRO": 
                self.sampiro_lineEdit.setText(str(total_members))
            if chapter == "SAPANGAN": 
                self.sapangan_lineEdit.setText(str(total_members))
            if chapter == "SICO": 
                self.sico_lineEdit.setText(str(total_members))
            if chapter == "TALAHIBAN": 
                self.talahiban_lineEdit.setText(str(total_members))
            if chapter == "TICALAN": 
                self.ticalan_lineEdit.setText(str(total_members))
            if chapter == "TIPAZ":  
                self.tipaz_lineEdit.setText(str(total_members))
            # Add more conditions for other chapters if needed

        # Close the connection
        conn.close()
                    



    def total_member(self):
        self.conn = sqlite3.connect("sjmc.db")
        cur = self.conn.cursor()
        cur.execute("SELECT *  FROM sjmc_table")
        member = cur.fetchall()
        counter = len(member)
        self.total_member_lineEdit.setText(str(counter))

    def stat(self):
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
        # self.ax_pie.set_label_colors(['black' for _ in labels])
        self.ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Draw the canvas
        self.canvas.draw()



    def setupUi(self, MainWindowStat):
        MainWindowStat.setObjectName("MainWindowStat")
        MainWindowStat.resize(1011, 940)
        self.centralwidget = QtWidgets.QWidget(MainWindowStat)
        self.centralwidget.setObjectName("centralwidget")
        MainWindowStat.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowStat.setWindowIcon(icon)

        
        self.total_member_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.total_member_lineEdit.setGeometry(QtCore.QRect(40, 50, 121, 31))
        self.total_member_lineEdit.setObjectName("total_member_lineEdit")
        self.total_member_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.total_member_lineEdit.setEnabled(False)

        self.total_member_label = QtWidgets.QLabel(self.centralwidget)
        self.total_member_label.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.total_member_label.setObjectName("total_member_label")
        self.total_member_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.total_frame = QtWidgets.QFrame(self.centralwidget)
        self.total_frame.setGeometry(QtCore.QRect(20, 20, 311, 81))
        self.total_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.total_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.total_frame.setObjectName("total_frame")

        
        #BACKGROUND LABEL
        self.back_label = QtWidgets.QLabel(self.centralwidget)
        self.back_label.setGeometry(QtCore.QRect(-10, 0, 1400, 980))
        self.back_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.back_label.setText("")
        self.back_label.setPixmap(QtGui.QPixmap("logo/back_pic.jpg"))
        self.back_label.setScaledContents(True)
        self.back_label.setObjectName("back_label")
     
        ################### --PIE CHART-- ############################
        # Create a layout for the central widget
        self.centralwidget_layout = QVBoxLayout(self.centralwidget)

        # Add a stretch before the canvas (adjust the value as needed)
        self.centralwidget_layout.addStretch(1)

        # Add a stretch after the canvas (adjust the value as needed)
        self.centralwidget_layout.addStretch(1)
   
        

        self.total_chapter_lineEdit = QtWidgets.QLineEdit(self.total_frame)
        self.total_chapter_lineEdit.setGeometry(QtCore.QRect(170, 30, 121, 31))
        self.total_chapter_lineEdit.setObjectName("total_chapter_lineEdit")
        self.total_chapter_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.total_chapter_lineEdit.setEnabled(False)
        self.total_chapter_label = QtWidgets.QLabel(self.total_frame)
        self.total_chapter_label.setGeometry(QtCore.QRect(170, 10, 91, 16))
        self.total_chapter_label.setObjectName("total_chapter_label")
        self.total_chapter_label.setStyleSheet("color: rgb(255, 199, 4);")
        

        self.member_chapter_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.member_chapter_frame_2.setGeometry(QtCore.QRect(20, 170, 971, 241))
        self.member_chapter_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.member_chapter_frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.member_chapter_frame_2.setObjectName("member_chapter_frame_2")

       
        self.Abung_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.Abung_lineEdit.setGeometry(QtCore.QRect(20, 40, 131, 20))
        self.Abung_lineEdit.setObjectName("Abung_lineEdit")
        self.Abung_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.Abung_lineEdit.setEnabled(False)
        self.abung_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.abung_label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.abung_label.setObjectName("abung_label")
        self.abung_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.buhaynasapa_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.buhaynasapa_lineEdit.setGeometry(QtCore.QRect(20, 140, 131, 20))
        self.buhaynasapa_lineEdit.setText("")
        self.buhaynasapa_lineEdit.setObjectName("buhaynasapa_lineEdit")
        self.buhaynasapa_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.buhaynasapa_lineEdit.setEnabled(False)
        self.buhaynasapa_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.buhaynasapa_label.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.buhaynasapa_label.setObjectName("buhaynasapa_label")
        self.buhaynasapa_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.balagbag_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.balagbag_lineEdit.setGeometry(QtCore.QRect(20, 90, 131, 20))
        self.balagbag_lineEdit.setText("")
        self.balagbag_lineEdit.setObjectName("balagbag_lineEdit")
        self.balagbag_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.balagbag_lineEdit.setEnabled(False)
        self.balagbag_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.balagbag_label.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.balagbag_label.setObjectName("balagbag_label")
        self.balagbag_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.calitcalit_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.calitcalit_label.setGeometry(QtCore.QRect(180, 70, 131, 16))
        self.calitcalit_label.setObjectName("calitcalit_label")
        self.calitcalit_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.calitcalit_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.calitcalit_lineEdit.setGeometry(QtCore.QRect(180, 90, 131, 20))
        self.calitcalit_lineEdit.setText("")
        self.calitcalit_lineEdit.setObjectName("calitcalit_lineEdit")
        self.calitcalit_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.calitcalit_lineEdit.setEnabled(False)

        self.bulsa_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.bulsa_label.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.bulsa_label.setObjectName("bulsa_label")
        self.bulsa_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.bulsa_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.bulsa_lineEdit.setGeometry(QtCore.QRect(20, 190, 131, 20))
        self.bulsa_lineEdit.setText("")
        self.bulsa_lineEdit.setObjectName("bulsa_lineEdit")
        self.bulsa_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.bulsa_lineEdit.setEnabled(False)

        self.calicanto_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.calicanto_label.setGeometry(QtCore.QRect(180, 20, 131, 16))
        self.calicanto_label.setObjectName("calicanto_label")
        self.calicanto_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.calicanto_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.calicanto_lineEdit.setGeometry(QtCore.QRect(180, 40, 131, 20))
        self.calicanto_lineEdit.setText("")
        self.calicanto_lineEdit.setObjectName("calicanto_lineEdit")
        self.calicanto_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.calicanto_lineEdit.setEnabled(False)

        self.calubcub_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.calubcub_lineEdit.setGeometry(QtCore.QRect(180, 140, 131, 20))
        self.calubcub_lineEdit.setText("")
        self.calubcub_lineEdit.setObjectName("calubcub_lineEdit")
        self.calubcub_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.calubcub_lineEdit.setEnabled(False)
        self.calubcub_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.calubcub_label.setGeometry(QtCore.QRect(180, 120, 131, 16))
        self.calubcub_label.setObjectName("calubcub_label")
        self.calubcub_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.hugom_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.hugom_lineEdit.setGeometry(QtCore.QRect(180, 190, 131, 20))
        self.hugom_lineEdit.setText("")
        self.hugom_lineEdit.setObjectName("hugom_lineEdit")
        self.hugom_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.hugom_lineEdit.setEnabled(False)
        self.hugom_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.hugom_label.setGeometry(QtCore.QRect(180, 170, 131, 16))
        self.hugom_label.setObjectName("hugom_label")
        self.hugom_label.setStyleSheet("color: rgb(255, 199, 4);")

        self.imelda_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.imelda_label.setGeometry(QtCore.QRect(340, 20, 131, 16))
        self.imelda_label.setObjectName("imelda_label")
        self.imelda_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.imelda_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.imelda_lineEdit.setGeometry(QtCore.QRect(340, 40, 131, 20))
        self.imelda_lineEdit.setText("")
        self.imelda_lineEdit.setObjectName("imelda_lineEdit")
        self.imelda_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.imelda_lineEdit.setEnabled(False)

        self.aplaya_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.aplaya_label.setGeometry(QtCore.QRect(340, 70, 131, 16))
        self.aplaya_label.setObjectName("aplaya_label")
        self.aplaya_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.aplaya_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.aplaya_lineEdit.setGeometry(QtCore.QRect(340, 90, 131, 20))
        self.aplaya_lineEdit.setText("")
        self.aplaya_lineEdit.setObjectName("aplaya_lineEdit")
        self.aplaya_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.aplaya_lineEdit.setEnabled(False)
        
        self.ibabao_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.ibabao_label.setGeometry(QtCore.QRect(340, 120, 131, 16))
        self.ibabao_label.setObjectName("ibabao_label")
        self.ibabao_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.ibabao_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.ibabao_lineEdit.setGeometry(QtCore.QRect(340, 140, 131, 20))
        self.ibabao_lineEdit.setText("")
        self.ibabao_lineEdit.setObjectName("ibabao_lineEdit")
        self.ibabao_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.ibabao_lineEdit.setEnabled(False)

        self.mabalanoy_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.mabalanoy_label.setGeometry(QtCore.QRect(340, 170, 131, 16))
        self.mabalanoy_label.setObjectName("mabalanoy_label")
        self.mabalanoy_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.mabalanoy_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.mabalanoy_lineEdit.setGeometry(QtCore.QRect(340, 190, 131, 20))
        self.mabalanoy_lineEdit.setText("")
        self.mabalanoy_lineEdit.setObjectName("mabalanoy_lineEdit")
        self.mabalanoy_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.mabalanoy_lineEdit.setEnabled(False)

        self.maraykit_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.maraykit_label.setGeometry(QtCore.QRect(500, 20, 131, 16))
        self.maraykit_label.setObjectName("maraykit_label")
        self.maraykit_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.maraykit_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.maraykit_lineEdit.setGeometry(QtCore.QRect(500, 40, 131, 20))
        self.maraykit_lineEdit.setText("")
        self.maraykit_lineEdit.setObjectName("maraykit_lineEdit")
        self.maraykit_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.maraykit_lineEdit.setEnabled(False)

        self.palahanan_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.palahanan_label.setGeometry(QtCore.QRect(500, 70, 131, 16))
        self.palahanan_label.setObjectName("palahanan_label")
        self.palahanan_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.palahanan_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.palahanan_lineEdit.setGeometry(QtCore.QRect(500, 90, 131, 20))
        self.palahanan_lineEdit.setText("")
        self.palahanan_lineEdit.setObjectName("palahanan_lineEdit")
        self.palahanan_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.palahanan_lineEdit.setEnabled(False)

        self.poblacion_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.poblacion_label.setGeometry(QtCore.QRect(500, 120, 131, 16))
        self.poblacion_label.setObjectName("poblacion_label")
        self.poblacion_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.poblacion_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.poblacion_lineEdit.setGeometry(QtCore.QRect(500, 140, 131, 20))
        self.poblacion_lineEdit.setText("")
        self.poblacion_lineEdit.setObjectName("poblacion_lineEdit")
        self.poblacion_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.poblacion_lineEdit.setEnabled(False)

        self.putingbuhangin_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.putingbuhangin_label.setGeometry(QtCore.QRect(500, 170, 131, 16))
        self.putingbuhangin_label.setObjectName("putingbuhangin_label")
        self.putingbuhangin_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.putingbuhangin_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.putingbuhangin_lineEdit.setGeometry(QtCore.QRect(500, 190, 131, 20))
        self.putingbuhangin_lineEdit.setText("")
        self.putingbuhangin_lineEdit.setObjectName("putingbuhangin_lineEdit")
        self.putingbuhangin_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.putingbuhangin_lineEdit.setEnabled(False)

        self.sampiro_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.sampiro_label.setGeometry(QtCore.QRect(660, 20, 131, 16))
        self.sampiro_label.setObjectName("sampiro_label")
        self.sampiro_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.sampiro_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.sampiro_lineEdit.setGeometry(QtCore.QRect(660, 40, 131, 20))
        self.sampiro_lineEdit.setText("")
        self.sampiro_lineEdit.setObjectName("sampiro_lineEdit")
        self.sampiro_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.sampiro_lineEdit.setEnabled(False)

        self.sapangan_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.sapangan_label.setGeometry(QtCore.QRect(660, 70, 131, 16))
        self.sapangan_label.setObjectName("sapangan_label")
        self.sapangan_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.sapangan_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.sapangan_lineEdit.setGeometry(QtCore.QRect(660, 90, 131, 20))
        self.sapangan_lineEdit.setText("")
        self.sapangan_lineEdit.setObjectName("sapangan_lineEdit")
        self.sapangan_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.sapangan_lineEdit.setEnabled(False)

        self.sico_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.sico_label.setGeometry(QtCore.QRect(660, 120, 131, 16))
        self.sico_label.setObjectName("sico_label")
        self.sico_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.sico_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.sico_lineEdit.setGeometry(QtCore.QRect(660, 140, 131, 20))
        self.sico_lineEdit.setText("")
        self.sico_lineEdit.setObjectName("sico_lineEdit")
        self.sico_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.sico_lineEdit.setEnabled(False)

        self.talahiban_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.talahiban_label.setGeometry(QtCore.QRect(660, 170, 131, 16))
        self.talahiban_label.setObjectName("talahiban_label")
        self.talahiban_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.talahiban_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.talahiban_lineEdit.setGeometry(QtCore.QRect(660, 190, 131, 20))
        self.talahiban_lineEdit.setText("")
        self.talahiban_lineEdit.setObjectName("talahiban_lineEdit")
        self.talahiban_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.talahiban_lineEdit.setEnabled(False)

        self.ticalan_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.ticalan_label.setGeometry(QtCore.QRect(820, 20, 131, 16))
        self.ticalan_label.setObjectName("ticalan_label")
        self.ticalan_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.ticalan_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.ticalan_lineEdit.setGeometry(QtCore.QRect(820, 40, 131, 20))
        self.ticalan_lineEdit.setText("")
        self.ticalan_lineEdit.setObjectName("ticalan_lineEdit")
        self.ticalan_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.ticalan_lineEdit.setEnabled(False)

        self.tipaz_label = QtWidgets.QLabel(self.member_chapter_frame_2)
        self.tipaz_label.setGeometry(QtCore.QRect(820, 70, 131, 16))
        self.tipaz_label.setObjectName("tipaz_label")
        self.tipaz_label.setStyleSheet("color: rgb(255, 199, 4);")
        self.tipaz_lineEdit = QtWidgets.QLineEdit(self.member_chapter_frame_2)
        self.tipaz_lineEdit.setGeometry(QtCore.QRect(820, 90, 131, 20))
        self.tipaz_lineEdit.setText("")
        self.tipaz_lineEdit.setObjectName("tipaz_lineEdit")
        self.tipaz_lineEdit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.tipaz_lineEdit.setEnabled(False)

      
        self.total_member_of_chapter_label = QtWidgets.QLabel(self.centralwidget)
        self.total_member_of_chapter_label.setGeometry(QtCore.QRect(20, 140, 201, 16))
        self.total_member_of_chapter_label.setObjectName("total_member_of_chapter_label")
        self.total_member_of_chapter_label.setStyleSheet("color: rgb(255, 199, 4);")

      
        self.total_frame.raise_()
        self.total_member_lineEdit.raise_()
        self.total_member_label.raise_()
        self.member_chapter_frame_2.raise_()
        self.total_member_of_chapter_label.raise_()
        
        self.stat()
        self.centralwidget_layout.addWidget(self.canvas)

        MainWindowStat.setCentralWidget(self.centralwidget)
        self.total_member()
        self.total_chapter()
        self.display_total_chapter_members()
        # self.create_chapter_line_edits()
        self.statusbar = QtWidgets.QStatusBar(MainWindowStat)
        self.statusbar.setObjectName("statusbar")
        MainWindowStat.setStatusBar(self.statusbar)
       
    
        self.retranslateUi(MainWindowStat)
        QtCore.QMetaObject.connectSlotsByName(MainWindowStat)

    

    def retranslateUi(self, MainWindowStat):
        _translate = QtCore.QCoreApplication.translate
        MainWindowStat.setWindowTitle(_translate("MainWindowStat", "STATISTICS"))
        self.total_member_label.setText(_translate("MainWindowStat", "Total Members"))
        self.total_chapter_label.setText(_translate("MainWindowStat", "Total Chapters"))
        self.abung_label.setText(_translate("MainWindowStat", "ABUNG"))
        self.buhaynasapa_label.setText(_translate("MainWindowStat", "BUHAYNASAPA "))
        self.balagbag_label.setText(_translate("MainWindowStat", "BALAGBAG "))
        self.calitcalit_label.setText(_translate("MainWindowStat", "CALITCALIT "))
        self.bulsa_label.setText(_translate("MainWindowStat", "BULSA "))
        self.calicanto_label.setText(_translate("MainWindowStat", "CALICANTO "))
        self.calubcub_label.setText(_translate("MainWindowStat", "CALUBCUB 1.0 "))
        self.hugom_label.setText(_translate("MainWindowStat", "HUGOM "))
        self.imelda_label.setText(_translate("MainWindowStat", "IMELDA"))
        self.aplaya_label.setText(_translate("MainWindowStat", "LAIYA APLAYA"))
        self.ibabao_label.setText(_translate("MainWindowStat", "LAIYA IBABAO"))
        self.mabalanoy_label.setText(_translate("MainWindowStat", "MABALANOY"))
        self.maraykit_label.setText(_translate("MainWindowStat", "MARAYKIT"))
        self.palahanan_label.setText(_translate("MainWindowStat", "PALAHANAN"))
        self.poblacion_label.setText(_translate("MainWindowStat", "POBLACION"))
        self.putingbuhangin_label.setText(_translate("MainWindowStat", "PUTING BUHANGIN"))
        self.sampiro_label.setText(_translate("MainWindowStat", "SAMPIRO"))
        self.sapangan_label.setText(_translate("MainWindowStat", "SAPANGAN"))
        self.sico_label.setText(_translate("MainWindowStat", "SICO 1.0"))
        self.talahiban_label.setText(_translate("MainWindowStat", "TALAHIBAN 1.0"))
        self.ticalan_label.setText(_translate("MainWindowStat", "TICALAN"))
        self.tipaz_label.setText(_translate("MainWindowStat", "TIPAZ"))
        self.total_member_of_chapter_label.setText(_translate("MainWindowStat", "TOTAL MEMBERS OF EACH CHAPTERS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowStat()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())