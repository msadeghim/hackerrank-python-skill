import re


pat = '^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
c = r'(.)\1{3,}'
t = int(input())
for _ in range(t):
    s = input()
    if re.search(pat, s) and not re.search(c,s.replace('-','')):
        print('Valid')
    else:
        print('Invalid')
