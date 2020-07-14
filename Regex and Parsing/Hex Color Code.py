import re


pat = r'(?<!^)#[0-9A-Fa-f]{3,6}'
l = int(input())
for _ in range(l):
    for _ in re.findall(pat, input()):
        print(_)
