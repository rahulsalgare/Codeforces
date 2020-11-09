# https://codeforces.com/problemset/problem/271/A/

from collections import Counter

strn = int(input()) + 1

while True:
    cnt = Counter(str(strn))
    res = [i > 1 for i in cnt.values()]
    if True in res:
        strn += 1
    else:
        break
print(strn)
