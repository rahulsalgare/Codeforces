# https://codeforces.com/problemset/problem/344/A

n = int(input())
cnt = 0
last = None
for i in range(n):
    no = input()
    if last == no[0] or last == None:
        cnt += 1
    last = no[1]
print(cnt)
