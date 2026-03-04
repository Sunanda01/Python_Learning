'''
Check how many missing values in each column.
Fill missing age values with the mean.
Drop rows where embarked is missing.
Interpolate the age column.
'''
import seaborn as sns

# Load the Titanic dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Datasheet")
print(df_titanic)

# Check how many missing values in each column
print(df_titanic.isnull().sum())

# Fill missing age values with the mean
# df_titanic["age"].fillna(df_titanic['age'].mean(), inplace=True)
print(f'Number of null value in Age {df_titanic["age"].isnull().sum()}')
print("Updated Age Column with a mean val")
df_titanic.fillna({'age':round(df_titanic["age"].mean())},inplace=True)
print(df_titanic)
print(f'Number of null value in Age {df_titanic["age"].isnull().sum()}')

# Interpolate the age column
print(f'Number of null value in Age {df_titanic["age"].isnull().sum()}')
print("Updated Age Column with a Interpolate val")
df_titanic["age"]=df_titanic["age"].interpolate()
print(df_titanic)
print(f'Number of null value in Age {df_titanic["age"].isnull().sum()}')

# Drop rows where embarked is missing
print(f'Number of null value in Embarked {df_titanic["embarked"].isnull().sum()}')
df_titanic=df_titanic.dropna(subset=['embarked'])
print("Deleted Embarked row with null val")
print(df_titanic)
print(f'Check number of null value in Embarked {df_titanic["embarked"].isnull().sum()}')