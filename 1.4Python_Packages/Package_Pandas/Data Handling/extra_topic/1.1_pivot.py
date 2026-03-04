'''
Dataset: Employee work hours
Columns: employee, day, hours_worked

Pivot to see hours worked by each employee across days (Mon–Fri).
Find total hours per employee (use aggfunc='sum').
Pivot to get the maximum hours in a day per employee.
'''

import pandas as pd
data_hours = {
    'employee': ['E1','E1','E1','E2','E2','E2','E3','E3','E3'],
    'day': ['Mon','Tue','Wed','Mon','Tue','Wed','Mon','Tue','Wed'],
    'hours_worked': [8, 7, 9, 6, 8, 7, 9, 9, 8]
}
df=pd.DataFrame(data_hours)
print(df)

# Pivot to see hours worked by each employee across days (Mon–Fri)
print("\n\nPivot to see hours worked by each employee across days (Mon–Fri)")
print(df.pivot(index='employee',columns='day',values='hours_worked'))

# Find total hours per employee (use aggfunc='sum')
print("\n\nFind total hours per employee (use aggfunc='sum')")
sum_table=df.pivot_table(index='employee',values='hours_worked',aggfunc='sum')
print(sum_table)

# Pivot to get the maximum hours in a day per employee.
print("\n\nPivot to get the maximum hours in a day per employee.")
max_hours_pivot=df.pivot_table(index="employee",values="hours_worked",aggfunc='max')
print(max_hours_pivot)