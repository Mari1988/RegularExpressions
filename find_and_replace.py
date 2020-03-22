""" use substitude method sub to find and replace the pattern from a text """

import re
pattern_obj = re.compile(r'Agent \w+') # matches word characters after 'Agent ' until it finds a non word character

pattern_obj.findall('Agent Bob gave secret files to Agent Steve')

# classify their names
pattern_obj.sub('REDACTED','Agent Bob gave secret files to Agent Steve') # 'REDACTED gave secret files to REDACTED'
