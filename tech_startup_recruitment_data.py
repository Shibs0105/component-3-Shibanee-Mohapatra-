# Import necessary packages
import pandas as pd
from plotnine import ggplot, aes, geom_bar

# Read the data from CSV to a DataFrame
recruitment_data = pd.read_csv('recruitment_data.csv')

# Take a closer look at the data using the head() function
print(recruitment_data.head())

# Check the columns to ensure they are as expected
print(recruitment_data.columns)