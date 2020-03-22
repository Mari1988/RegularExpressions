"""
caret (^) symbol is used to match beginning of a string
dollar ($) symbol is used to match end of a string
"""

import re

begin_re_obj = re.compile(r'^Hello')

begin_re_obj.search('Hi Hello')  # returns None
begin_re_obj.search('Helloooo')  # returns Match object

end_re_obj = re.compile(r'Hello$')

end_re_obj.search('Hi Hello')  # returns Match object
end_re_obj.search('Helloooo')  # returns None

""" begin and end with a certain pattern """
begin_end_re_obj = re.compile(r'^\d+$')  # begin with one or more digits and end with the same patter
begin_end_re_obj.search('1234567890')  # <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
begin_end_re_obj.search('1234x567890')  # None
