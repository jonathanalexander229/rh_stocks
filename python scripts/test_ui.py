from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import numpy as np
from datetime import datetime

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Option P/L Chart")

        # Create the matplotlib Figure and FigureCanvas objects
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create the form layout
        form_layout = QtWidgets.QVBoxLayout()

        # Create the form
        self.chain_symbol_input = QtWidgets.QLineEdit()
        self.strike_price_input = QtWidgets.QLineEdit()
        self.mark_input = QtWidgets.QLineEdit()
        self.expiration_input = QtWidgets.QLineEdit()
        self.current_stock_price_input = QtWidgets.QLineEdit()
        self.delta_input = QtWidgets.QLineEdit()
        self.rho_input = QtWidgets.QLineEdit()
        self.theta_input = QtWidgets.QLineEdit()
        self.vega_input = QtWidgets.QLineEdit()

        # Add form fields to the layout
        form_layout.addWidget(QtWidgets.QLabel("Chain Symbol:"))
        form_layout.addWidget(self.chain_symbol_input)
        form_layout.addWidget(QtWidgets.QLabel("Strike Price:"))
        form_layout.addWidget(self.strike_price_input)
        form_layout.addWidget(QtWidgets.QLabel("Mark Price:"))
        form_layout.addWidget(self.mark_input)
        form_layout.addWidget(QtWidgets.QLabel("Expiration:"))
        form_layout.addWidget(self.expiration_input)
        form_layout.addWidget(QtWidgets.QLabel("Current Stock Price:"))
        form_layout.addWidget(self.current_stock_price_input)
        form_layout.addWidget(QtWidgets.QLabel("Delta:"))
        form_layout.addWidget(self.delta_input)
        form_layout.addWidget(QtWidgets.QLabel("Rho:"))
        form_layout.addWidget(self.rho_input)
        form_layout.addWidget(QtWidgets.QLabel("Theta:"))
        form_layout.addWidget(self.theta_input)
        form_layout.addWidget(QtWidgets.QLabel("Vega:"))
        form_layout.addWidget(self.vega_input)

        # Create the sliders
        self.date_slider = QtWidgets.QSlider(Qt.Horizontal)
        self.stock_price_slider = QtWidgets.QSlider(Qt.Horizontal, self)

        # Add sliders to the layout
        form_layout.addWidget(QtWidgets.QLabel("Date:"))
        form_layout.addWidget(self.date_slider)
        form_layout.addWidget(QtWidgets.QLabel("Stock Price:"))
        form_layout.addWidget(self.stock_price_slider)

        # Create the main layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(form_layout, 1)
        self.layout.addWidget(self.canvas, 2)

        # Set the layout
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Connect the sliders to the update_graph method
        self.date_slider.valueChanged.connect(self.update_graph)
        self.stock_price_slider.valueChanged.connect(self.update_graph)
        
        # Call update_graph to display the initial graph
        self.update_graph()

        self.show()

    def update_graph(self):
        # Get the selected date and stock price
        selected_date = self.date_slider.value()
        selected_stock_price = self.stock_price_slider.value()

        # Manually enter the values
        original_price = 1.52
        theta_effect = -0.1435
        delta_effect = 0.56
        original_stock_price = 200.3
        expiration_date = pd.Timestamp(2024, 4, 5)  # replace with your actual expiration date

        # Calculate the dates until expiration
        current_date = pd.Timestamp.now()
        dates = pd.date_range(start=current_date, end=expiration_date, freq='D')

        # Calculate the range of stock prices
        stock_prices = np.linspace(0.9 * original_stock_price, 1.1 * original_stock_price, 100)

        # Calculate the new option price and P/L for each date
        days = (dates - current_date).days
        # Calculate the new option price and P/L for each stock price
        #option_prices = original_price + theta_effect * days[1] + delta_effect * (stock_prices - original_stock_price
        #pl = option_prices - original_price
        # Clear the previous plot
        self.figure.clear()

        # Create the new plot
        ax = self.figure.add_subplot(111)
        ax.plot(stock_prices, 'b-')
        ax.set_xlabel('Stock Price')
        ax.set_ylabel('P/L')
        
        # Add a horizontal line at y=0
        ax.axhline(-(original_price * 100), color='r', linestyle='--')
        
        

        # Add a horizontal line at the break-even price
        break_even_price = original_stock_price + original_price
        ax.axhline(0, color='g', linestyle='--')

        # Format the x-axis to display the dates
        # ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

        # Draw the plot
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    sys.exit(app.exec_())