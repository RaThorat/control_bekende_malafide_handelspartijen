import pandas as pd

# Function to extract domain from email
def extract_domain(email):
    if pd.isnull(email):
        return None  # or any placeholder value for missing emails
    if isinstance(email, str):
        return email.split('@')[-1]
    else:
        return None  # or any placeholder value for non-string types

# Read the Excel file containing email addresses
emails_df = pd.read_excel('input_file.xlsx')

# Extract domain from 'EMAIL' column
emails_df['url'] = emails_df['EMAIL'].apply(extract_domain)

# Read the Excel file containing domain names
domains_df = pd.read_excel('Bekende malafide handelspartijen.xlsx')

# Merge dataframes on 'url' column
merged_df = pd.merge(emails_df, domains_df, how='right', on='url')

# Filter out the matched domains
matched_domains = merged_df[['EMAIL', 'url']].dropna()

# Write the matched domains to an output file
matched_domains.to_excel('matched_domains.xlsx', index=False)
