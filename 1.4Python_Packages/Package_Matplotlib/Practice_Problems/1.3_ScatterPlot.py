'''
Create scatter plot of height vs. weight.
Use red color and circle markers.
Add regression line manually (y = 0.5x - 25 as a simple line).
Add labels and title.
'''
import matplotlib.pyplot as plt
height = [150, 160, 165, 170, 175, 180, 185, 190]
weight = [50, 55, 60, 65, 70, 75, 80, 85]
plt.title("Height vs Weight")
plt.scatter(height,weight,color="red",marker="o",label="height vs. weight")
regression_line=[0.5 * h - 25 for h in height]
plt.plot(height,regression_line,color="blue",linestyle="--",label="y=0.5x-25")
plt.legend()
plt.xlabel("height")
plt.ylabel("weight")
plt.show()