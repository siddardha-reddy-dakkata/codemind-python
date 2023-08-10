l = []
for i in range(int(input())):
    num = int(input())
    l.append(num)
t = int(input())

ans = 0
for i in l:
    if i > t:
        ans += 2
    else:
        ans += 1
print(ans)