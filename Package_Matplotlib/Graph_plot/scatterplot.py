import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(1,13,size=12)
y=np.arange(10,22)
print(x,y)
plt.scatter(x,y,color='green',marker='o',label='ScatterPlot')
plt.title("ScatterPlot")
plt.legend()
plt.xlabel("X")
plt.ylabel('Y')
plt.grid(color='gray')
plt.show()