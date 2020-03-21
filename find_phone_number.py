import re

txt = 'Hi, your current phone number is 899-875-0947 and your old number was 812-901-5111'

# find the phone numbers from above text
regex_obj = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # create an re object with the pattern to be found
print(type(regex_obj))  # <class '_sre.SRE_Pattern'>

match_obj = regex_obj.search(txt)  # returns a match object
print(match_obj.group())  # finds just the first occurrence

print(regex_obj.findall(txt))  # finds all occurrences

""" grouping the regular expressions using paranthesis """
"""
Group first 3 digits of the phone number  into a group (which represents the area code of the phone number)
"""
regex_obj = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # create an re object with the pattern to be found
match_obj = regex_obj.search(txt)
print('The area code is {}'.format(match_obj.group(1)))  # returns the area code

""" using pipe character to match one of many groups """
regex_obj_pipe = re.compile(r'bat(man|lady|mobile)')
match_obj_pipe = regex_obj_pipe.search('Im a batman')
print(match_obj_pipe.group())

match_obj_pipe = regex_obj_pipe.search('I have a batmobile!')
print(match_obj_pipe.group())