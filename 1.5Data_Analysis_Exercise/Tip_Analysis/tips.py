import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# Load Tips dataset
print("\t\t\tTIPS DATASET\n")
tips_df=sns.load_dataset("tips")
print(tips_df.head())
print(tips_df.tail())
# summary info
print("\n\t\tsummary info\n")
print(tips_df.info())
# Check for missing values
print("\n\t\tIf Missing Value\n")
print(tips_df.isnull().sum())

# Data Analysis with Pandas
print("\n\t\tData Analysis with Pandas\n")
# Find the average tip overall.
print('The average tip overall => ', round(tips_df["tip"].mean(),2))
# Find the day with the highest average total bill.
print("The day with the highest average total bill")
print(tips_df.groupby("day",observed=True)["total_bill"].mean().sort_values(ascending=False).head(1))
# Find which gender gives higher average tips.
print("Gender that gives higher average tips")
print(tips_df.groupby("sex",observed=True)["tip"].mean().sort_values(ascending=False).head(1))
# Calculate tip percentage (tip/total_bill * 100) and add it as a new column.
print("\nCalculate tip percentage (tip/total_bill * 100) and add it as a new column\n")
tips_df["tips_percent"]=round((tips_df["tip"]/tips_df["total_bill"])*100,2)
print(tips_df.sample(10))

# save data to Excel file
tips_df.to_excel("cleaned_tip.xlsx")

# Visualization with Matplotlib
print("\n\t\tVisualization with Matplotlib\n")

# 📈 Line Plot: Average tip percentage by party size (size).
points=round(tips_df.groupby("size")['tips_percent'].mean(),2)
plt.figure(figsize=(10,5))
plt.plot(points,marker="o",color="green",label="Tip % per size")
plt.legend()
plt.xlabel("Party Size")
plt.ylabel("Tips Percent")
plt.grid(color="gray",linestyle="--")
plt.title("Average tip percentage by party size (size)")
plt.savefig("lineplot.png",dpi=300,bbox_inches="tight")
plt.show()

# 📊 Bar Chart: Average total bill by day.
colors = ["skyblue", "lightgreen", "salmon", "orange"]  # one per bar
plt.figure(figsize=(10,5))
round(tips_df.groupby("day",observed=True)["total_bill"].mean(),2).plot(kind="bar",color=colors,edgecolor="black")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average total bill by day")
plt.savefig("barchart.png",dpi=300,bbox_inches="tight")
plt.show()

# ⚫ Scatter Plot: total_bill vs tip, color-coded by gender.
colors={'Male':'blue', 'Female':'red'}
plt.scatter(tips_df["total_bill"],tips_df["tip"],c=tips_df["sex"].map(colors))
plt.title("Total Bill vs Tip (by Gender)")
legend_handles = [mpatches.Patch(color=color, label=gender) 
                  for gender, color in colors.items()]
plt.legend(handles=legend_handles, title="Gender")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.grid(color='gray',linestyle="--")
plt.savefig("scatterplot.png",dpi=300,bbox_inches="tight")
plt.show()

# 📉 Histogram: Distribution of tip percentages.
plt.hist(tips_df["tips_percent"],bins=9,color='purple',edgecolor="black")
plt.title("Distribution of tip percentages")
plt.grid(color='gray',linestyle="--")
plt.xlabel("range")
plt.ylabel("tips %")
plt.savefig("histogram.png",dpi=300,bbox_inches="tight")
plt.show()