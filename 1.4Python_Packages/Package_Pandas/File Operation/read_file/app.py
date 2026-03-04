import pandas as pd
df=pd.read_csv("demo_dataset.csv")
print("CSV FILE\n",df)
df=pd.read_excel("demo_dataset.xlsx")
print("EXCEL FILE\n",df)
df=pd.read_json("demo.json")
print("JSON FILE\n",df)