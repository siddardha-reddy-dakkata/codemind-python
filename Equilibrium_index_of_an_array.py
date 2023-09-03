for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    
    ans = -1
    tempSum = 0
    tot = sum(l)
    for i in range(n):
        if tempSum == tot - tempSum - l[i]:
            ans = i
            break
        tempSum += l[i]
    print(ans)