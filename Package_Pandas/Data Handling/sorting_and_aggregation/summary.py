import pandas as pd
data = {
    'Name': [
        'Subho', 'Priyanka', 'Sopno', 'Soumya',
        'Riya', 'Arjun', 'Madhav', 'Sneha',
        'Karan'
    ],
    'Age': [
        17, 18, 13, 17,
        20, 22, 19, 21,
        23
    ],
    'City': [
        'Purnea', 'Hyderabad', 'Shantipur', 'Ranaghat',
        'Kolkata', 'Delhi', 'Patna', 'Mumbai',
        'Bangalore'
    ],
    'Salary': [
        15000, 22000, 12000, 18000,
        25000, 30000, 24000, 28000,
        35000,
    ]
}
df=pd.DataFrame(data)
print(df)
print(f"Average Salary = {round(df['Salary'].mean(),2)}\nMaximum Salary = {df['Salary'].max()}\nMinimum Salary = {df['Salary'].min()}\nSalary Count = {df['Salary'].count()}\nTotal Salary Sum = {df['Salary'].sum()}")