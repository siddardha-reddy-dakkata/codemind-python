n = int(input())
l = list(map(int,input().split()))

res = []
for i in l:
    if i == l.count(i):
        if i not in res:
            res.append(i)
if res:
    print(* res)
else:
    print(-1)