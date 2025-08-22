'''
Create a bar chart of sales.
Use different colors for each bar.
Rotate company names on X-axis.
Add value labels on top of each bar.
'''
import matplotlib.pyplot as plt
companies = ["Google", "Amazon", "Microsoft", "Apple", "Meta"]
sales = [120, 150, 90, 200, 80]
plt.figure(figsize=(10,7))
plt.title("Company Sales")
bars=plt.bar(companies,sales,color=['yellow','aqua','green','orange','pink'],edgecolor='black',label="Sales per Company")
for bar in bars:
    yval=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2, yval+5,str(yval),ha='center',va='bottom',fontsize=10)
plt.xlabel("Companies")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.ylabel("Sales")
plt.show()
