import re

""" find all method from re module returns the list of strings that matched the pattern we specified"""

# example
txt = 'Hi, your current phone number is 899-875-0947 and your old number was 812-901-5111'
digit_matcher = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
digit_matcher.findall(txt)  # finds all occurrences also returns the list of strings that matched the regexp

