import pandas as pd

# Specify the absolute path to your Excel file
file_path = r'C:\Users\Eric\Desktop\graphics\Test Files.xlsx'

# Specify the sheet name you want to read (in this case, "3B")
sheet_name = "3B"

# Read the specified sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the data from the "3B" sheet
print(df)
