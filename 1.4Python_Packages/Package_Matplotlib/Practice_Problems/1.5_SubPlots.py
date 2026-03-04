'''
Create a single figure with 3 subplots:
    Line plot for y1.
    Bar chart for y2.
    Scatter plot for y3.
Add titles to each subplot.
Adjust layout so graphs don’t overlap.
'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]   # y = x^2
y2 = [1, 8, 27, 64, 125] # y = x^3
y3 = [1, 2, 3, 4, 5]     # y = x
fig,ax=plt.subplots(1,3,figsize=(12,5))
fig.supxlabel("Common X Axis")
fig.supylabel("Common Y Axis")

ax[0].set_title("Line Graph")
ax[0].plot(x,y1,color='blue',marker="o",label="y=x*x",linestyle="--",linewidth=2)
ax[0].legend()
# ax[0].set_xlabel("X Axis")
# ax[0].set_ylabel("Y Axis")
ax[0].grid(color="gray",linestyle="--")

ax[1].set_title("Bar Graph")
ax[1].bar(x,y2,color=['red','yellow','orange','pink','maroon'],label="y=x*x*x")
ax[1].legend()
# ax[1].set_xlabel("X Axis")
# ax[1].set_ylabel("Y Axis")

ax[2].set_title("Scatter Plot")
ax[2].scatter(x,y3,color="purple",marker="^",label="y=x")
ax[2].legend()
# ax[2].set_xlabel("X Axis")
# ax[2].set_ylabel("Y Axis")
ax[2].grid(color="gray",linestyle="--")

plt.tight_layout()
plt.suptitle("Subplots Example",y=1)
plt.savefig("sub_plot.png",dpi=300,bbox_inches="tight")
plt.show()