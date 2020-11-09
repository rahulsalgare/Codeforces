# https://codeforces.com/problemset/problem/136/A

n = int(input())
lst = list(map(int, input().split()))

dct = dict.fromkeys(sorted(lst))

for i, val in enumerate(lst):
    dct[val] = i + 1

print(*list(dct.values()))
