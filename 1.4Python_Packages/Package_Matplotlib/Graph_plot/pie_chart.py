import matplotlib.pyplot as plt
regions=['East','West','North','South']
value=[2000,4000,6000,8080]
plt.pie(value,labels=regions,colors=['yellow','green','aqua','orange'],autopct='%1.1f%%')
plt.title('Pie Chart')
plt.legend(loc='upper left')
plt.show()