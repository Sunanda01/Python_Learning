import pandas as pd
df=pd.read_csv("../read_file/demo_dataset.csv")

# 5 Top Rows
print("Top 5 Rows\n",df.head())

# Last 5 Rows
print("Last 5 Rows\n",df.tail())

# Information about DataSet
print("Information of datafile")
print(df.info())