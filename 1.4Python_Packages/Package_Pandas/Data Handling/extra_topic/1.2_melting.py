'''
Dataset: Wide-format sales data
region   Q1   Q2   Q3   Q4
East     120  150  100  180
West     200  220  210  230

Melt this into long format (region, quarter, sales).
Sort by quarter and find which region had the highest sales each quarter.
Group melted data to find total annual sales per region.
'''
import pandas as pd
data_sales = {
    'region': ['East', 'West'],
    'Q1': [120, 200],
    'Q2': [150, 220],
    'Q3': [100, 210],
    'Q4': [180, 230]
}
df=pd.DataFrame(data_sales)
print("\nOriginal Dataset")
print(df)

# Melt this into long format (region, quarter, sales)
print('\n\nMelt into long format (region, quarter, sales)')
melted_data=df.melt(id_vars='region',var_name="quarter",value_name="sales")
print(melted_data)

# Sort by quarter and find which region had the highest sales each quarter
print("\n\nSort by quarter and display region that had highest sales each quarter")
print(melted_data.sort_values(['quarter','sales'],ascending=[True,False]))
print("\n")
print(melted_data.sort_values(['quarter','sales'],ascending=[True,False]).groupby('quarter').head(1))

# Group melted data to find total annual sales per region
print("\n\nGroup melted data to find total annual sales per region")
print(melted_data.groupby('region')['sales'].sum())