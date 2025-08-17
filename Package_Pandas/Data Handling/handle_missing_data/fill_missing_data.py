import pandas as pd
data = {
    'Name': [
        'Subho', 'Priyanka', 'Sopno', 'Soumya',
        'Riya', 'Arjun', 'Madhav', 'Sneha',
        'Karan', None
    ],
    'Age': [
        17, 18, 13, 17,
        20, 22, 19, 21,
        23, None
    ],
    'City': [
        'Purnea', 'Hyderabad', 'Shantipur', 'Ranaghat',
        'Kolkata', 'Delhi', 'Patna', 'Mumbai',
        'Bangalore', None
    ],
    'Salary': [
        15000, 22000, 12000, 18000,
        25000, 30000, 24000, 28000,
        35000, 27000
    ]
}
df=pd.DataFrame(data)
print(df)

# # Fill missing data with a value
# df.fillna(0,inplace=True)
# print(df)

# Guess and fill data
df['Name'].fillna('User',inplace=True)
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['City'].fillna('India',inplace=True)
print(df)