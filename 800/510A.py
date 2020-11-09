# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())
res = [['.' * m] for i in range(n)]
for i in range(0, n, 2):
    res[i] = '#' * m

cnt = 1
for i in range(1, n, 2):
    if cnt:
        res[i] = '.' * (m-1) + '#'
        cnt = 0
    else:
        res[i] = '#' + '.' * (m-1)
        cnt = 1

for i in res:
    print(i)
