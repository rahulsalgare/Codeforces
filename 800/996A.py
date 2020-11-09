# https://codeforces.com/problemset/problem/996/A

n = int(input())
cnt = 0
lst = [1, 5, 10, 20, 100]

for i in sorted(lst, reverse=True):
    cnt += n // i
    n = n % i

print(cnt)
