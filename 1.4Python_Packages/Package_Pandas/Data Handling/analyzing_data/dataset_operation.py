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

# Selecting Single Column
print("Salary")
Salary=df['Salary']
print(Salary)

# Selecting Multiple Columns
subset=df[['Name','Age']]
print(subset)

# Filtering row on single condition
Salary_Filter=df[df['Salary']>25000]
print("Salary More Than 25000")
print(Salary_Filter)

# Filtering row on multiple condition
Salary_Filter=df[(df['Salary']>15000)&(df['Salary']<25000)]
print("Salary Between 15000 - 25000")
print(Salary_Filter)

Salary_Filter=df[(df['Salary']>25000)&(df['Age']>20)]
print("Salary > 25000 AND Age > 20")
print(Salary_Filter)

Salary_Filter=df[(df['Salary']>25000)|(df['Age']>20)]
print("Salary > 25000 OR Age > 20")
print(Salary_Filter)