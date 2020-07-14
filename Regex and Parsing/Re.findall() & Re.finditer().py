import re
s = input()
pat1 = r'(?<=[^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])'
ans = re.findall(pat1, s)
if len(ans) == 0:
    print(-1)
else:
    [print(elm) for elm in ans]
