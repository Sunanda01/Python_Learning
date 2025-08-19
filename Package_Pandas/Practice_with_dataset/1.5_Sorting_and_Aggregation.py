'''
Sort Titanic passengers by age (ascending).
Sort by fare (descending).
Group by class and find the average fare.
Group by sex and get the count of survivors.
Group by both class and sex → average age.
'''
import seaborn as sns

# Load the Titanic dataset.
df_titanic=sns.load_dataset("titanic")
print("Titanic Datasheet")
print(df_titanic.head(20))

# Fill age
df_titanic.fillna({'age':round(df_titanic['age'].mean())},inplace=True)
print(df_titanic.head(20))

# Sort Titanic passengers by age (ascending)
print("Sort Titanic passengers by age (ascending)")
df_titanic.sort_values('age',ascending=True,inplace=True)
print(df_titanic.head(20))

# Sort by fare (descending)
print("Sort by fare (descending)")
df_titanic.sort_values('fare',ascending=False,inplace=True)
print(df_titanic.head(20))

# Group by class and find the average fare
average=df_titanic.groupby("class",observed=False)['fare'].mean()
print("Group by class and find the average fare", average)
# print(df_titanic.groupby("class",observed=True)['fare'].mean())

# Group by sex and get the count of survivors
group=df_titanic.groupby("sex")['survived'].sum()
print("Group by sex and get the count of survivors",group)

# Group by both class and sex → average age
group=df_titanic.groupby(["class","sex"],observed=True)['age'].mean()
print("Group by both class and sex → average age",group)
print(df_titanic.groupby(["class","sex"], observed=True,as_index=False)['age'].mean())