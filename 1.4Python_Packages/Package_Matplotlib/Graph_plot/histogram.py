import matplotlib.pyplot as plt
import numpy as np
data=np.random.randint(25,100,size=30)
print(data)
plt.hist(data,bins=5,color='yellow',edgecolor="red",linestyle='--',linewidth=2)
plt.show()