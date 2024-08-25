import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.QtCharts import QChart, QLineSeries

# Data for the JPM call option spread
data = [("JPM", 200, "2023-06-17", 100, 400, 200, 5, 50, 55, 8),
        ("JPM", 200, "2023-06-17", 100, 300, 200, 5, 55, 60, 4)]

# Create a QApplication object
app = QApplication(sys.argv)

# Create a QMainWindow object
window = QMainWindow()
window.setCentralWidget(chart)
window.show()

# Create a figure and an axis object
fig, ax = plt.subplots()

# Add data points to the axis using the data from the table
for row in range(len(data)):
    symbol, strike, exp_date, credit, max_cost, max_profit, width, ask, bid, volume, PoP_buy, PoP_sell, imp_vol, delta, rho, theta, vega = data[row]
    ax.plot([strike], [max_profit], 'bo-', label='Max Profit')
    ax.plot([strike], [-max_cost], 'ro-', label='Max Cost')

# Set the labels and colors for each series
ax.set_xlabel('Strike')
ax.set_ylabel('Profit/Loss')
ax.axis([0, 300, -100, 500])
ax.legend()

# Show the plot
plt.show()

# Run the application event loop
sys.exit(app.exec_())