'''
Load Titanic and Tips datasets.
Merge them on a fake key (create a column with passenger ID / customer ID).
Concatenate two DataFrames vertically and horizontally.
'''
import pandas as pd
import seaborn as sns
import numpy as np

# Load the Titanic and Tipx Dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Datasheet")
print(df_titanic)

df_tips=sns.load_dataset('tips')
print("Tips Dataset")
print(df_tips)

# Added Column Cust_ID
df_titanic.insert(0,"Cust_ID",np.arange(1,892))
print("After Adding Cust_Id")
print(df_titanic)

print("After Adding Cust_Id")
df_tips.insert(0,"Cust_ID",np.random.randint(1,892,size=244))
print(df_tips)

# Merging them on key Cust_ID
print("Datasets Merged on Cust_ID")
merge_dataset=pd.merge(df_titanic,df_tips,on="Cust_ID", how="inner")
print(merge_dataset)

# Concatenate two DataFrames vertically and horizontally
print("Datasets Concatenated HORIZONTALLY")
horizontally_concat=pd.concat([df_titanic,df_tips],axis=1)
print(horizontally_concat)
print("Datasets Concatenated VERTICALLY")
vertically_concat=pd.concat([df_titanic,df_tips],axis=0)
print(vertically_concat)