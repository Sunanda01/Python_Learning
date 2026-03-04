import seaborn as sns
# Load the Titanic dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Dataset Processing\n\n")
print(df_titanic.head(20))

# Analyzing Data
print("\n\nAnalyzing Data\n\n")
print(df_titanic.info())
print(df_titanic.isna().sum())

# Handle the missing column
print("\n\nHandle the missing column\n\n")
df_titanic['age']=round(df_titanic['age'].interpolate())
df_titanic.fillna({'deck':'F'},inplace=True)
df_titanic=df_titanic.dropna(subset=['embark_town'])
print(df_titanic.head())
print(df_titanic.sample(10))
print(df_titanic.tail())

#Filtering the data
print("\n\nFiltering Data       =>     Survived Data in ascending order\n\n")
survived_data=df_titanic[df_titanic['survived']==1]

# Sorting the data
survived_data=survived_data.sort_values(by="embark_town").copy()
print(survived_data.head())
print(survived_data.sample(10))
print(survived_data.tail())

#saving the extracted data in Excel file
survived_data.to_excel("Survived Data.xlsx",index=False)

# Analyzing Filtered Data
print("\n\nAnalyzing The Extracted DataSet\n\n")
print(survived_data.groupby("who",as_index=True)['who'].count())