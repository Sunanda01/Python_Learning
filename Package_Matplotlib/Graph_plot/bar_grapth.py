import matplotlib.pyplot as plt
product=['A','B','C','D','E']
sales=[100,200,50,400,480]
plt.title("Bar Graph depicting sales of product")
plt.barh(product,sales,color="orange",linewidth=2,linestyle='--',label="Sale Analyze")
plt.xlabel("Product")
plt.ylabel("Sales per product")
plt.grid(color='gray',linestyle="--")
plt.legend()
plt.show()