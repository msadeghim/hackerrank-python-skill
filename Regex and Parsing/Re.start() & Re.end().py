import re
s, k = input(), input()
m = re.finditer('(?=('+k+'))', s, )
if k in s:
    [print(tuple([elm.start(), elm.start() + len(k) - 1])) for elm in m]
else:
    print(tuple([-1,-1]))
