# Search the string to see if it starts with "The" and ends with "Spain"

import re

txt = "The rain in Japan"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")