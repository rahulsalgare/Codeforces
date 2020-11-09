# https://codeforces.com/problemset/problem/486/A

n = int(input())
print(n//2) if n % 2 == 0 else print(-(n+1)//2)
