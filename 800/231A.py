# https://codeforces.com/problemset/problem/231/A

n = int(input())
scr = []
for i in range(n):
    scr.append(list(map(int, input().split())))

print(sum([1 for i in scr if sum(i) > 1]))
