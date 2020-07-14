import re
a = int(input())
for i in range(a):
    print(bool(re.match(r'^[-+]?\d*\.\d+$', input())))
