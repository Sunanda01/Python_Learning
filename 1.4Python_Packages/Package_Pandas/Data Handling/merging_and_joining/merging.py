import pandas as pd
employees = pd.DataFrame({
    'EmpID': [101, 102, 103, 104, 105, 106],
    'Name': ['Subho', 'Priyanka', 'Sopno', 'Soumya', 'Riya', 'Rekha'],
    'DeptID': [1, 2, 1, 3, 2, 4]
})
departments = pd.DataFrame({
    'DeptID': [1, 2, 3],
    'DeptName': ['HR', 'Finance', 'IT'],
    'Location': ['Delhi', 'Mumbai', 'Kolkata']
})

print(employees)
print(departments)

print("Inner Join")
inner_merge_data=pd.merge(employees,departments,on="DeptID",how="inner")
print(inner_merge_data)

print("Outer Join")
outer_merge_data=pd.merge(employees,departments,on="DeptID",how="outer")
print(outer_merge_data)

print("Left Join")
left_merge_data=pd.merge(employees,departments,on="DeptID",how="left")
print(left_merge_data)

print("Right Join")
right_merge_data=pd.merge(employees,departments,on="DeptID",how="right")
print(right_merge_data)