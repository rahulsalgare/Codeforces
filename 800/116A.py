# https: // codeforces.com/problemset/problem/116/A

lst = []
n = int(input())
maxm = 0
prev = 0
for i in range(n):
    lst.append(list(map(int, input().split())))

for i in lst:
    if prev - i[0] + i[1] > maxm:
        maxm = prev - i[0] + i[1]

    prev = prev - i[0] + i[1]

print(maxm)
