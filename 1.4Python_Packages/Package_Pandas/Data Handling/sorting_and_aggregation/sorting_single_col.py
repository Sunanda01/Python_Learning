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
print("Before Sorting")
print(df)
df.sort_values(by="Age",ascending=False,inplace=True)
print("After Sorting Age in Descending Order")
print(df)
df.sort_values(by="Age",ascending=True,inplace=True)
print("After Sorting Age in Ascending Order")
print(df)