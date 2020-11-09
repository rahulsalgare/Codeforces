# https: // codeforces.com/problemset/problem/339/A

op = input()
res = sorted([i for i in op if i.isdigit()])
print('+'.join(res))
