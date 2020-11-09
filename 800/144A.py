# https://codeforces.com/problemset/problem/144/A
n = int(input())
lst = list(map(int, input().split()))

min_pos = max(loc for loc, val in enumerate(lst) if val == min(lst))
max_pos = min(loc for loc, val in enumerate(lst) if val == max(lst))

print(max_pos + n - 1 -
      min_pos) if max_pos < min_pos else print(max_pos + n - 1 - min_pos - 1)
