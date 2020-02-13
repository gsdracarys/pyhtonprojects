import re

txt = "192.168.1.20,10.44.11.20,265.230.221.200"
x = re.findall(r'\S',txt)
print(x)