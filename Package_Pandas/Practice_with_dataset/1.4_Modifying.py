'''
Add a new column family_size = sibsp + parch.
Drop the deck column.
Rename the sex column → gender.
'''
import seaborn as sns

# Load the Titanic dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Datasheet")
print(df_titanic.head(20))

# Add a new column family_size = sibsp + parch
print('Added new column family_size')
df_titanic['family_size']=df_titanic['sibsp']+df_titanic['parch']
print(df_titanic.head(20))

# Drop the deck column
print("After Dropping the deck column")
df_titanic=df_titanic.drop(columns=['deck'])
print(df_titanic.head(20))

# Rename the sex column → gender
print("Rename the sex column → gender")
df_titanic.rename(columns={'sex':'gender'},inplace=True)
print(df_titanic.head())
print(df_titanic.sample(5))
print(df_titanic.tail())