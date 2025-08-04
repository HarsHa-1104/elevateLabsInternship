import pandas as pd

# 1. Load the dataset
# Make sure 'Walmart_Sales.csv' is in the same directory as your script
df = pd.read_csv('Walmart_Sales.csv')

print("Original DataFrame head:")
print(df.head())
print("\nOriginal DataFrame info:")
print(df.info())

# 2. Check for and remove duplicate rows
num_duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {num_duplicates}")

if num_duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicate rows removed.")
    print(f"Number of rows after removing duplicates: {len(df)}")
else:
    print("No duplicate rows found.")

# 3. Convert 'Date' column to datetime format
# The format '%d-%m-%Y' is used because the dates are in 'DD-MM-YYYY' format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

print("\nDataFrame info after Date conversion:")
print(df.info())

# 4. Rename columns for uniformity: lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

print("\nDataFrame head after column renaming:")
print(df.head())
print("\nNew column names:")
print(df.columns)

# 5. Save the cleaned DataFrame to a new CSV file
output_file_name = 'cleaned_walmart_sales_data.csv'
df.to_csv(output_file_name, index=False)

print(f"\nCleaned data saved to {output_file_name}")
