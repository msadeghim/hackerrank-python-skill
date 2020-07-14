import re

l = int(input())

for i in range(l):
    text = input()
    a = re.sub(r'(?<= )(\|\|)(?= )', 'or', text)
    b = re.sub(r'(?<= )(\&\&)(?= )', 'and', a)
    print(b)
