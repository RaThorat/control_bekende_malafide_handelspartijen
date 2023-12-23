# control_bekende_malafide_handelspartijen
match email domains from an input Excel file with a list of known domains of malafide practices


This Python script utilizes Pandas to match email domains from an input Excel file with a list of known domains, generating an output of the matched domains in a separate Excel file.
Functionality Overview

The script performs the following steps:

    Reads email addresses from an input Excel file.
    Extracts domains from the email addresses using the extract_domain() function.
    Reads a separate Excel file containing known domain names.
    Merges the dataframes based on the domain column.
    Filters and extracts matched domains.
    Writes the matched domains to an output Excel file.

Requirements

    Python 3.x
    Pandas library

Usage

    Install the necessary Python packages:

    bash

pip install pandas

Prepare your input files:

    Ensure the input Excel file (input_file.xlsx) contains an 'EMAIL' column.
    Have a separate Excel file (Bekende malafide handelspartijen.xlsx) with a list of known domains.

Run the script:

bash

    python email_domain_matcher.py

Example

python

import pandas as pd

# Function to extract domain from email
def extract_domain(email):
    # (Function definition remains unchanged)

# Read the Excel file containing email addresses
emails_df = pd.read_excel('input_file.xlsx')

# (Rest of your provided code)
# ... (code snippet continues)

Note

    Ensure column names and file paths match your actual file setup.

