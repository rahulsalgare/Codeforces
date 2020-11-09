# https://codeforces.com/problemset/problem/1328/A

t = int(input())
for i in range(t):
    a, b = map(int, input().split())

    if a % b == 0:
        print(0)

    elif a > b:
        div = a // b
        print(b * (div+1) - a)

    else:
        print(b-a)
