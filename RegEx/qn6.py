# Make a search that returns no match

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)