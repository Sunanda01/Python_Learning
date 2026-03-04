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

# Describe DataSet
print(df.describe())

# Find Shape and column
print("Shape of Dataset= ",df.shape)
print("Number of columns in Dataset= ",df.columns)

# Some operation on rows n cols

