import pymysql
import pandas as pd

# MySQL database connection detailss
host = 'localhost'  # or '127.0.0.1'
user = 'root'
password = '1381'  # Replace with your actual password
database = 'health_insurance'
query = 'SELECT * FROM synthetic_data'  # Adjust your query as needed

# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Execute the query and fetch the data into a DataFrame
df = pd.read_sql(query, connection)

# Save the DataFrame to a CSV file
csv_file_path = 'extracted_data.csv'
df.to_csv(csv_file_path, index=False)

# Close the database connection
connection.close()

print(f"Data extracted and saved to {csv_file_path}")

# -------------------------------------------------------------------------------------------------------------------------

# Load the CSV data into a DataFrame
csv_file_path = 'extracted_data.csv'
df = pd.read_csv(csv_file_path)

# Convert 'Date de reception' to datetime format
df['Date de reception'] = pd.to_datetime(df['Date de reception'])

# Extract the year and month from 'Date de reception'
df['Year'] = df['Date de reception'].dt.year
df['Month'] = df['Date de reception'].dt.month_name().str.slice(stop=3)

# Create a pivot table to count the number of 'Sinistre' entries per month
pivot_table = df.pivot_table(index=['Year', 'Month'], values='Sinistre', aggfunc='count')
pivot_table = pivot_table.reset_index()
pivot_table.rename(columns={'Sinistre': 'NMBR'}, inplace=True)

# Calculate the grand total
grand_total = pd.DataFrame({'Year': ['Total'], 'Month': [''], 'NMBR': [pivot_table['NMBR'].sum()]})

# Concatenate the grand total to the pivot table
pivot_table = pd.concat([pivot_table, grand_total], ignore_index=True)

# Save the pivot table to an Excel file with formatting
excel_file_path = 'results.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    pivot_table.to_excel(writer, sheet_name='Sinistres Per Month', index=False, startrow=0)

    # Get the xlsxwriter objects
    workbook = writer.book
    worksheet = writer.sheets['Sinistres Per Month']

    # Set column widths
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 10)

    # Add a format for the total row
    total_format = workbook.add_format({
        'bold': True,
        'border': 1
    })

    # Write the total row with the defined format
    last_row = len(pivot_table)  # index of the last row
    worksheet.write(last_row, 0, 'Total général', total_format)
    worksheet.write(last_row, 1, '', total_format)
    worksheet.write(last_row, 2, pivot_table['NMBR'].sum(), total_format)
