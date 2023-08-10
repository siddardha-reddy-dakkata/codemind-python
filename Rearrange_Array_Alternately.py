for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = []
    c = 1
    for i in range(n):
        if c % 2 != 0:
            ans.append(max(l))
            l.remove(max(l))
        else:
            ans.append(min(l))
            l.remove(min(l))
        c += 1
    print(*ans)