n = int(input())
l = list(map(int,input().split()))
flag = True
for i in l:
    if l.count(i) == 1:
        flag = False
        print(i, end = " ")
if flag:
    print(-1)