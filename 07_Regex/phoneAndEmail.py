#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the cilpboard
import re

import pyperclip

phoneRegex = re.compile(
    r"""(
   (\d{3})? first 3 digits
   (-|\s)? first hypen or space
   (\d{4}) middle numbers
   (-|\s) hypen or space
   (\d{4}) last numbers
   )""",
    re.VERBOSE,
)

# Create email regex.
emailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name (\.[a-zA-Z]{2,4})       # dot-something
    )""",
    re.VERBOSE,
)
