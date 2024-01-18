import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sqlite3

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.setWindowTitle("Python GUI with Matplotlib - Customized Pie Chart")

def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.setGeometry(100, 100, 800, 600)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
