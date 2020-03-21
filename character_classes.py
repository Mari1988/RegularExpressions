"""
\d - mathces decimal digits 0-9
\D - matches everything other than digits 0-9
\w - matches alphabets, digits and the underscore
\W - matches everything other than alphabets, digits and the underscore
\s - matches spaces such as space, tab, etc
\S - matches everything other than spaces
"""

# example : The Twelve Days of Christmas song
song = """12 Drummers Drumming 11 Pipers Piping 10 Lords a Leaping 9 Ladies Dancing 8 Maids a Milking"""
import re

re_obj = re.compile(r'\d+\s\w+')
re_obj.findall(song)

# making our own character classes - use square brackets
re_obj_vowels = re.compile(r'[aeiouAEIOU]')
re_obj_vowels.findall('Robocop eats baby food')  # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

# matching two vowels in a row
re_obj_2_vowels = re.compile(r'[aeiouAEIOU]{2}')
re_obj_2_vowels.findall('Robocop eats baby food')  # ['ea', 'oo']

# negation of own character classes (add a carat character at the begining of own-character class)
re_obj_non_vowels = re.compile(r'[^aeiouAEIOU]')
re_obj_non_vowels.findall('Robocop eats baby food')  # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ',
# 'f', 'd']
