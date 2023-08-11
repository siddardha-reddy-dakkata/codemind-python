n = int(input())
l = list(map(int,input().split()))
l = list(set(l))
m = max(l)
if(len(l) >= 3):
    l.remove(max(l))
    l.remove(max(l))
    print(max(l))
else:
    print(m)