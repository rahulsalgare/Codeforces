# https://codeforces.com/problemset/problem/148/A

op = []
for i in range(4):
    op.append(int(input()))

no = int(input())

lst = [i for i in range(1, no + 1)]

lst = [i for i in lst if i % op[0] != 0]

if len(lst) != 0:
    lst = [i for i in lst if i % op[1] != 0]

if len(lst) != 0:
    lst = [i for i in lst if i % op[2] != 0]

if len(lst) != 0:
    lst = [i for i in lst if i % op[3] != 0]

print(no - len(lst))
