import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'C:\\Users\\Eric\\Desktop\\graphics\\Test Files.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
