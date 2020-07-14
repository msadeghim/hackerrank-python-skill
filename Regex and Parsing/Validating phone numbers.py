import re
[print('YES' if len(re.findall(r'^[789]\d{9}$', input())) else 'NO') for i in range(int(input()))]
