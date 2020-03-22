import re

""" dot character matching anything except the newline """
""" match any but exactly one character """
re_obj = re.compile(r'.at')
re_obj.findall('Cat on the hat sat on the mat')  # ['Cat', 'hat', 'sat', 'mat']
re_obj.findall('ate')  # empty list

""" match any but exactly one or two characters """
re_obj = re.compile(r'.{1,2}at')
re_obj.findall('Cat on the hat sat on the mat')  #  ['Cat', ' hat', ' sat', ' mat'] (notice the space here)
re_obj.findall('ate')  # empty list


""" match ANYTHIN using .* """
# . means matching anything (except newline) and * means zero or any number of times
# basically matching anything

match_anything = re.compile(r'.*')
match_anything.search('blahlabalh1232808ggfgllllllaaaaaaaaas')

""" match even the newline character """
txt = 'The job of Robocop is to \n protect the public trust \n save the innocent \n uphold the law'
print(txt)
match_new_line_too = re.compile(r'.*', re.DOTALL)
match_new_line_too.findall(txt)

""" ignore case sensitive search """
txt = 'The job of ROBOCOP is to \n protect the public trust \n save the innocent \n uphold the law'
ignore_case = re.compile(r'[aeiou]', re.IGNORECASE)
ignore_case.findall(txt)  # includes capital vowels as well
