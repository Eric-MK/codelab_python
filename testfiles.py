import pandas as pd

# Specify the absolute path to your Excel file
file_path = r'C:\Users\Eric\Desktop\graphics\Test Files.xlsx'

# Specify the sheet name you want to read (in this case, "3B")
sheet_name = "3B"

# Read the specified sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the data from the "3B" sheet
""" print(df)
 """
 
 # Define a function to generate email addresses
def generate_email(student_name, email_domain):
    # Split the student name by commas and spaces
    name_parts = student_name.split(', ')
    
    # Extract the first and last names
    if len(name_parts) == 2:
        last_name, first_name = name_parts
    else:
        first_name = name_parts[0]
        last_name = ""
    
    # Remove spaces and special characters from the names
    first_name = ''.join(e for e in first_name if e.isalnum())
    last_name = ''.join(e for e in last_name if e.isalnum())
    
    # Combine the names and domain to create the email address
    email = f"{first_name.lower()}{last_name.lower()}@{email_domain}"
    
    return email

# Define the email domain
email_domain = "gmail.com"

# Apply the generate_email function to create email addresses
df['Email Address'] = df['Student Name'].apply(lambda x: generate_email(x, email_domain))

# Display the DataFrame with the newly generated email addresses
print(df[['Student Name', 'Email Address']])
