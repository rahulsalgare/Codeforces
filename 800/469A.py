# https://codeforces.com/problemset/problem/469/A

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

p = x.pop(0)
q = y.pop(0)

if len(set(x).union(set(y))) >= n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
