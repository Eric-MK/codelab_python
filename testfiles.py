import pandas as pd
import re  # Import the regular expressions library


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

# Maintain a set to keep track of generated email addresses
generated_emails = set()

# Define a function to generate email addresses
def generate_unique_email(student_name, email_domain):
    # Remove special characters and spaces from the student_name
    cleaned_name = re.sub(r'[^a-zA-Z0-9 ]', '', student_name)

    # Split the cleaned name by spaces
    name_parts = cleaned_name.split()
    
    # Initialize variables for last name, first name, middle name, and forth name
    last_name = ""
    first_name = ""
    middle_name = ""
    forth_name = ""
    
    # Check the number of name parts and assign them accordingly
    if len(name_parts) >= 1:
        last_name = name_parts[0]
    if len(name_parts) >= 2:
        first_name = name_parts[1]
    if len(name_parts) >= 3:
        middle_name = name_parts[2]
    if len(name_parts) >= 4:
        forth_name = name_parts[3]

    # Take the first letter of the first name and concatenate it with the last name
    email = f"{last_name.lower()[0]}{middle_name.lower()}@{email_domain}"
    # Make the email address unique if it already exists
    suffix = 1
    while email in generated_emails:
        email = f"{last_name.lower()[0]}{middle_name.lower()}{suffix}@{email_domain}"
        suffix += 1
    
    # Add the generated email to the set
    generated_emails.add(email)
    
    return email
# Apply the generate_email function to create email addresses
df['Email Address'] = df['Student Name'].apply(lambda x: generate_unique_email(x, email_domain))

# Display the DataFrame with the newly generated email addresses
print(df[['Student Name', 'Email Address']])
