s = input()
d = {}
ans = True
for i in s:
    if i in d:
        ans = False
        break
    else:
        d[i] = 1
print(ans)