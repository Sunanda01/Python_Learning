import pandas as pd
batch_A=pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Subho', 'Priyanka', 'Soumya'],
    'Marks': [85, 90, 78]
})
batch_B=pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['Sopno', 'Riya', 'Ankit'],
    'Marks': [88, 76, 92]
})
print("Batch A")
print(batch_A)
print("Batch B")
print(batch_B)

print("Concatenated Batch Vertically")
print(pd.concat([batch_A,batch_B],ignore_index=True))

print("Concatenated Batch Horizontally")
print(pd.concat([batch_A,batch_B],axis=1,ignore_index=True))