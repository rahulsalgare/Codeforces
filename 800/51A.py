# https://codeforces.com/problemset/problem/61/A

strn1 = input()
strn2 = input()

res = ''
for i in range(len(strn1)):
    res += str(int(strn1[i]) ^ int(strn2[i]))
print(res)
