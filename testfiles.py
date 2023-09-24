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
 
 # Define the email domain
email_domain = "gmail.com"

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
    
    # Take the first letter of the first name and concatenate it with the last name
    email = f"{last_name[0].lower()}{first_name.lower()}@{email_domain}"
    
    return email

# Apply the generate_email function to create email addresses
df['Email Address'] = df['Student Name'].apply(lambda x: generate_email(x, email_domain))

# Display the DataFrame with the newly generated email addresses
print(df[['Student Name', 'Email Address']])
