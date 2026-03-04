import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,11,2)
y=np.random.randint(1,15,size=5)
fig,ax=plt.subplots(1,2,figsize=(10,5))
ax[0].plot(x,y,color='blue')
ax[0].set_title("Line Graph")

ax[1].bar(x,y,color='orange')
ax[1].set_title("Bar Graph")

fig.suptitle("SubPlot")
plt.tight_layout()
plt.savefig("graph.png",dpi=300,bbox_inches="tight")
plt.show()