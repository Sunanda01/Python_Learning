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

# Add Column Mathod 1
df["Bonus"]=df["Salary"]*0.1
print("Added Bonus Column")
print(df)

# Add Column Mathod 2 {add olumn @specific position}
df.insert(0,"Employee_Id",["E01","E02","E03","E04","E05","E06","E07","E08","E09","E10"])
print("Added Column Employee_Id")
print(df)