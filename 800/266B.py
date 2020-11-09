# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())
strn = input()
for i in range(t):
    strn = strn.replace('BG', 'GB')

print(strn)
