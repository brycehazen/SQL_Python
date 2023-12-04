## Here I am trying to concatenate together some sort of an ID. I will then do the same in SQL to try and find more matches ##

import pandas as pd
import re

# Function to extract the first set of digits from a string
def extract_first_digits(s):
    match = re.search(r'\d+', s)
    return match.group() if match else ''

# Filename of the CSV
csv_filename = 'RDE_DuplicateRemoved.csv'

# Load CSV using a relative path
csv_data = pd.read_csv(csv_filename)

# Create 'FakeID'
csv_data['FakeID'] = csv_data['FirstName'].str.cat(csv_data['LastName'], sep='') + csv_data['AddrLines'].apply(extract_first_digits)

# Output the first few rows to verify
print(csv_data.head())
