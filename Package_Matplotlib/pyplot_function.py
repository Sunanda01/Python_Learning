import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[200,100,170,300,390,280,156]
plt.title('Sale Report of Week 1')
plt.plot(x,y,color='green',linewidth=2,marker='o',linestyle='--',label='Sales Data')
plt.xlabel("Day")
plt.ylabel("Sales per day")
plt.legend(loc='upper left',fontsize=10)
plt.xlim(1,7)
plt.ylim(100,500)
plt.xticks(x,['D1','D2','D3','D4','D5','D6','D7'])
plt.grid(color='gray',linestyle=":")
plt.show()  