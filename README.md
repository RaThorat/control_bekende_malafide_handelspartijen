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
