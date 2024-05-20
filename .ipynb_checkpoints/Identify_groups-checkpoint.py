import pandas as pd
from plotnine import ggplot, aes, geom_bar, theme_minimal, labs

# Read the data from CSV to a DataFrame
recruitment_data = pd.read_csv('recruitment_data.csv')

# Take a closer look at the data using the head() function
print("First few rows of the data:")
print(recruitment_data.head())

# Check the columns to ensure they are as expected
print("Column names:")
print(recruitment_data.columns)

# Group by 'recruiting_source' and count the number of occurrences
source_counts = recruitment_data['recruiting_source'].value_counts()
print("\nNumber of Candidates by Recruitment Source:")
print(source_counts)

# Find the average 'sales_number' by 'recruiting_source' if it exists
if 'sales_number' in recruitment_data.columns:
    avg_sales_by_source = recruitment_data.groupby('recruiting_source')['sales_number'].mean()
    print("\nAverage Sales Number by Recruitment Source:")
    print(avg_sales_by_source)

# Calculate the success rate by recruitment source if 'success' column exists
if 'success' in recruitment_data.columns:
    success_rate_by_source = recruitment_data.groupby('recruiting_source')['success'].mean()
    print("\nSuccess Rate by Recruitment Source:")
    print(success_rate_by_source)

# Create a bar plot for the number of candidates from each source
plot = (ggplot(recruitment_data, aes(x='recruiting_source')) +
        geom_bar() +
        theme_minimal() +
        labs(title='Number of Candidates by Recruitment Source', x='Recruiting Source', y='Number of Candidates'))
plot.show()


# Create a bar plot for the average sales number by recruitment source
if 'sales_number' in recruitment_data.columns:
    plot_avg_sales = (ggplot(recruitment_data, aes(x='recruiting_source', y='sales_number')) +
                      geom_bar(stat='summary', fun_y='mean') +
                      theme_minimal() +
                      labs(title='Average Sales Number by Recruitment Source', x='Recruiting Source', y='Average Sales Number'))
    print(plot_avg_sales)

# Create a bar plot for the success rate by recruitment source
if 'success' in recruitment_data.columns:
    plot_success_rate = (ggplot(recruitment_data, aes(x='recruiting_source', y='success')) +
                         geom_bar(stat='summary', fun_y='mean') +
                         theme_minimal() +
                         labs(title='Success Rate by Recruitment Source', x='Recruiting Source', y='Success Rate'))
    print(plot_success_rate)
