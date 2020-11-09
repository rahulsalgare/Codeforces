# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())

price = sum([i*k for i in range(1, w+1)])

print(price-n) if price > n else print(0)
