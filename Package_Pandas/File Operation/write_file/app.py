import pandas as pd
data={
    'Name':['Subho','Priyanka','Sopno','Soumya'],
    'Age':[17,18,13,17],
    'City':['Purnea','Hyderabad','Shantipur','Ranaghat']
}

df=pd.DataFrame(data)
print(df)

df.to_csv("data.csv",index=False)
df.to_excel("data.xlsx",index=False)
df.to_json("data.json",index=False,indent=4)