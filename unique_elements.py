n = int(input())
l = list(map(int,input().split()))

ans = []
for i in l:
    if i not in ans:
        ans.append(i)
print(*ans)