# https: // codeforces.com/problemset/problem/263/A

mat = []
for i in range(5):
    mat.append(list(map(int, input().split())))

cnt = 0
x = 0
y = 0
for i, val in enumerate(mat):
    if 1 in val:
        x = i
        y = val.index(1)

while x != 2:
    if x > 2:
        x -= 1
    else:
        x += 1

    cnt += 1

while y != 2:
    if y > 2:
        y -= 1
    else:
        y += 1

    cnt += 1

print(cnt)
