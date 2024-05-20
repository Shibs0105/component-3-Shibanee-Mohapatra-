import pandas as pd

# Read the data from CSV to a DataFrame
recruitment_data = pd.read_csv('recruitment_data.csv')

# Group by 'Recruiting Source' and calculate the average Sales Number and Attrition Number
average_sales_attrition = recruitment_data.groupby('recruiting_source').agg({'sales_quota_pct': 'mean', 'attrition': 'mean'})

# Print out the average Sales Number and Attrition Number
print("Average Sales Number and Attrition Number by Recruiting Source:")
print(average_sales_attrition)
