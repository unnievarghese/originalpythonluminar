#regular expression
#pattern matching
import re
matcher=re.finditer('ab','ababababababab')
# [print(i.start()) for i in matcher]
# [print(i.group())for i in matcher]
out=[(i.start(),i.group()) for i in matcher]
print(out)