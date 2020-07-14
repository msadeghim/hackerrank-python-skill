import re


a = int(input())
for _ in range(a):
    a, b = input().split()
    if len(re.findall(r'^\<[a-zA-Z][0-9a-zA-Z\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}\>$',b)) > 0:
        print(a,b)
