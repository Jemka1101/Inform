import re
text = str(input())
print(len(re.findall("\w[\w-]*\w*", text)))