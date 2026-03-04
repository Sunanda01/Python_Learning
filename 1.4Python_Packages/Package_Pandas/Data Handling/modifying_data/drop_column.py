import pandas as pd
data = {
    'Name': [
        'Subho', 'Priyanka', 'Sopno', 'Soumya',
        'Riya', 'Arjun', 'Madhav', 'Sneha',
        'Karan', 'Ishita'
    ],
    'Age': [
        17, 18, 13, 17,
        20, 22, 19, 21,
        23, 18
    ],
    'City': [
        'Purnea', 'Hyderabad', 'Shantipur', 'Ranaghat',
        'Kolkata', 'Delhi', 'Patna', 'Mumbai',
        'Bangalore', 'Chennai'
    ],
    'Salary': [
        15000, 22000, 12000, 18000,
        25000, 30000, 24000, 28000,
        35000, 27000
    ]
}
df=pd.DataFrame(data)
print(df)

df["Bonus"]=df["Salary"]*0.1
df["Salary Increment"]=df['Salary']+df["Bonus"]
print('\n',df)

# Drop Single Column
print("\nAfter Deleting Column Salary Increment")
df.drop(columns=["Salary Increment"],inplace=True)
print(df)

# Drop Multiple Column
print("\nAfter Deleting Column Bonus and Age")
df.drop(columns=["Age","Bonus"],inplace=True)
print(df)