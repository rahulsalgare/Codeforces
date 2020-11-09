# https://codeforces.com/problemset/problem/266/A

n = int(input())
strn = input()

cnt = 0
prev = strn[0]

for i in range(1, n):
    if strn[i] == prev:
        cnt += 1
    else:
        prev = strn[i]

print(cnt)
