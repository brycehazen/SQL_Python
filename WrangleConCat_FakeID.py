## Here I am trying to concatenate together some sort of an ID. I will then do the same in SQL to try and find more matches ##

import pandas as pd
import re

# Function to extract the first set of digits from a string
def extract_first_digits(s):
    if pd.isna(s):
        return ''
    s = str(s)  # Convert to string in case the input is not a string
    match = re.search(r'\d+', s)
    return match.group() if match else ''

# Load CSV using the specified encoding
csv_data = pd.read_csv('RDE_DuplicateRemoved.csv', encoding='ISO-8859-1')

# Create 'FakeID'
csv_data['FakeID'] = csv_data['FirstName'].str.cat(csv_data['LastName'], sep='') + csv_data['AddrLines'].apply(extract_first_digits)

# Select the columns you need
output_data = csv_data[['ConsID', 'AddrLines', 'FakeID']]

# Save to a new CSV file with the specified encoding
output_data.to_csv('FakeID_ConsID_AddrLines.csv', index=False, encoding='ISO-8859-1')
