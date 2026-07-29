import re
words="hy everyone how are you"
print(re.findall(r"\b\w+ly\b", words))
print(re.search(r"\b\w+ow\b", words))