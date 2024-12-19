import pandas as pd

# Load the Excel file
file_path = 'Forbes-2021.xlsx'

# Read the relevant sheet from the file
details_df = pd.read_excel(file_path, sheet_name='Details')

# Extract the company names into a list
company_names = details_df['Name'].tolist()

# Save the company names to a text file
output_file_path = 'company_names.txt'
with open(output_file_path, 'w') as file:
    for name in company_names:
        file.write(name + '\n')

print(f"Company names have been saved to {output_file_path}")
