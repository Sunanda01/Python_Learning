'''
Load the Titanic dataset.
Display the first 10 rows, last 10 rows.
Show all column names & datatypes.
Get the summary statistics (describe()) for numeric columns.
Find the average age of passengers.
'''
import seaborn as sns
# Load the Titanic dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Datasheet")
print(df_titanic)
print(df_titanic.columns)

# Display the first 10 rows, last 10 rows.
print("First 10 rows of Titanic Dataset")
print(df_titanic.head(10))
print("Last 10 rows of Titanic Dataset")
print(df_titanic.tail(10))

# Show all column names & datatypes.
print("Name of Columns and their datatypes")
print(df_titanic.info())

# Get the summary statistics (describe()) for numeric columns.
print("summary statistics for numeric columns")
print(round(df_titanic.describe(),2))

# Find the average age of passengers.
print(f"Avergae of Age Column is {round(df_titanic['age'].mean(),2)}")