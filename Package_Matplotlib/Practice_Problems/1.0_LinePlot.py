'''
Plot temperature vs. months as a line graph.
Add markers on each point.
Title: "Monthly Temperature Trend".
X-axis label: "Month", Y-axis label: "Temperature (°C)".
Add grid lines.
'''
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [15, 18, 21, 25, 30, 35, 33, 31, 28, 24, 20, 16]
plt.title("Monthly Temperature Trend")
plt.plot(months,temperature,marker='o',label="Temperature",color="blue")
plt.legend()
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(color='gray')
plt.show()