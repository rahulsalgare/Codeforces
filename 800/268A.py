# https://codeforces.com/problemset/problem/268/A

n = int(input())
lst = []
cnt = 0
for i in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        if lst[i][0] == lst[j][1]:
            cnt += 1

        if lst[i][1] == lst[j][0]:
            cnt += 1

print(cnt)
