import re

""" match zero or one time in the text """

regex_obj = re.compile(r'bat(wo)?man')
regex_obj.search('batwoman')  # works
regex_obj.search('batwowoman')  # doesn't work
regex_obj.search('batman')  # works

""" match zero or more times in the text """

regex_obj = re.compile(r'bat(wo)*man')
regex_obj.search('batwoman')  # works
regex_obj.search('batwowoman')  # works
regex_obj.search('batwowowowowowowowowowoman')  # works
regex_obj.search('batman')  # works

""" match one or more times in the text """

regex_obj = re.compile(r'bat(wo)+man')
regex_obj.search('batwoman')  # works
regex_obj.search('batwowoman')  # works
regex_obj.search('batwowowowowowowowowowoman')  # works
regex_obj.search('batman')  # does not work (returns None)

""" match specific number of times in the text """
regex_obj = re.compile(r'bat(wo){3}man')
regex_obj.search('batwoman')  # doesn't work
regex_obj.search('batwowowoman')  # works

regex_obj = re.compile(r'(ha){3}')
regex_obj.search('I said hahaha')

regex_obj = re.compile(r'(\d\d\d(\d)?(-)?){3}')
regex_obj.search('My phone number is 812-901-1234')  # the problem here is the area code is not bounded to 3 digits

""" match at least x times and at max y times using {x, y} """
""" here x or y is optional which implies there is no lower or upper bound respectively """

""" greedy match """
re_greedy = re.compile(r'(\d){3,5}')  # match text containing 3 to 5 digits
re_greedy.search('123456789')  # notice it returns 12345 (by default Python matches maximum no of characters - greedy)

""" non greedy (add a ? after the curly brace) """
re_non_greedy = re.compile(r'(\d){3,5}?')  # match text containing 3 to 5 digits
re_non_greedy.search('123456789')  # notice it returns 12345 (by default Python matches maximum no of characters - greedy)

