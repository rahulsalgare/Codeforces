# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
lst = list(map(int, input().split()))
print(len([i for i in lst if i >= lst[k-1] and i > 0]))
