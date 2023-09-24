import pandas as pd
import re  # Import the regular expressions library


# Specify the absolute path to your Excel file
file_path = r'C:\Users\Eric\Desktop\graphics\TestyyFilesemail.csv'

# Specify the sheet name you want to read (in this case, "3B")

# Read the specified sheet into a DataFrame
df = pd.read_csv(file_path)

# Display the data from the "3B" sheet
print(df)
 


