'''
Plot pie chart with percentages.
Highlight "Apple" slice using explode.
Title: "Smartphone Market Share".
'''
import matplotlib.pyplot as plt
brands = ["Samsung", "Apple", "Xiaomi", "Oppo", "Others"]
market_share = [30, 25, 20, 10, 15]
plt.pie(market_share,labels=brands,colors=['yellow','orange','red','pink','aqua'],autopct="%1.1f%%",explode=[0,0.1,0,0,0])
plt.title("Smartphone Market Share")
plt.show()