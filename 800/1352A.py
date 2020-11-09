# https://codeforces.com/problemset/problem/1352/A

t = int(input())

for i in range(t):
    n = input()

    cnt = 0
    f = 1
    res = []
    n = n[::-1]
    for i, v in enumerate(n, 1):
        if v is not '0':
            cnt += 1
            res.append(int(v) * f)
        f *= 10

    print(cnt)
    print(*res)
