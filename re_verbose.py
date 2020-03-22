""" Managing Complex Regexes """

"""matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by 
telling the re.compile() function to ignore whitespace and comments inside the regular expression string """

import re

# Now instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# you can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

"""Note how the previous example uses the triple-quote syntax (''') to create a multiline string so that you can 
spread the regular expression definition over many lines, making it much more legible. """

""" Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE using pipe operator """
# So if you want a regular expression
# 1. that’s case-insensitive
# 2. includes newlines to match the dot character
# 3. includes verbose
# you would form your re.compile() call like this:

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

