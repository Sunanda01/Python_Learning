import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,11,2)
y=np.random.randint(1,15,size=5)
print(x,y)
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("line chart")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar chart")

# plt.tight_layout()
plt.show()