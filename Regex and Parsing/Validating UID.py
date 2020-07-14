import re


c1 = r'[A-Z].*[A-Z]'
c2 = r'\d.*\d.*\d'
c3 = '^[a-zA-Z0-9]+$'
c4 = r'(.).*\1'
c5 = '^.{10}$'

t = int(input())
for _ in range(t):
    s = input()
    if re.search(c1, s) and re.search(c2, s) and re.search(c3, s) and not re.search(c4, s) and re.search(c5, s):
        print('Valid')
    else:
        print('Invalid')
